import urllib3
import datetime
import sys
import json
http = urllib3.PoolManager()
SEASON_ID = { 
                '2009-2010' : 49,
                '2010-2011' : 50,
                '2011-2012' : 51,
                '2012-2013' : 52,
                '2013-2014' : 53,
                '2014-2015' : 54,
                '2015-2016' : 55,
                '2016-2017' : 56,
                '2017-2018' : 57,
                '2018-2019' : 58,
                '2019-2020' : 59,
            } # cdc.gov
US_STATES = [ "AL", "AK", "AS", "AZ", "AR", "CA", "CO", "CT", "DE", "DC", "FM", "FL", "GA", "GU", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MH", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "MP", "OH", "OK", "OR", "PW", "PA", "PR", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VI", "VA", "WA", "WV", "WI", "WY" ]
API_URL = "https://gis.cdc.gov/grasp/Flu8/PostPhase08ILITimeSeriesData"
SEASON_ST_LEVEL = 6


class FluStatus:
    def __init__(self, state, last_n_years, severity_level=SEASON_ST_LEVEL):
        self.state = state
        self.severity_level = severity_level
        self.details = []
        self.flu_history(last_n_years)
        self._display()

    def _get_cdc_data(self, season_id):
        post_body = {'AppVersion' : 'Public', 'SeasonID' : season_id }
        encoded_data = json.dumps(post_body).encode('utf-8')
        r = http.request('POST',
                         API_URL,
                         body=encoded_data,
                         headers={  'Accept': 'application/json, text/plain, */*',
                                    'Content-Type': 'application/json'
                                 }
                         )
        data = {}
        if r.status == 200:
            data = r.data
        return data

    def flu_history(self, last_n_years):
        now = datetime.datetime.now()
        current_year = now.year
        for year in range(current_year - last_n_years - 1, current_year + 1):
            season_id = SEASON_ID.get('{}-{}'.format(year - 1, year))
            self.details.append(self._get_cdc_data(season_id))

    def _get_mmwr_ids(self, bus_data, state_id, st_level):
        for state_data in bus_data:
            if state_data.get('stateid') == state_id and state_data.get('st_level') == st_level:
                return state_data

    def _get_mmwr_details(self, mmwr, mmwr_id):
        for d in mmwr:
            if d.get('mmwrid') == mmwr_id:
                return d

    def _display(self):
        state_id = 0
        try:
            state_id = US_STATES.index(self.state)
        except ValueError as ve:
            print("State {} value error".format(self.state))
            return
        for season in self.details:
                if season:
                    res = json.loads((season.decode('utf-8')))
                    bus_data = res.get('busdata')
                    mmwr = res.get('mmwr')
                    mmwr_start_data = self._get_mmwr_ids(bus_data, state_id, self.severity_level)                    
                    if mmwr_start_data:
                        mmwr_id = mmwr_start_data.get('mmwrid')
                        mmwr_details = self._get_mmwr_details(mmwr, mmwr_id)
                        print(
                                "State : {} :: FLU Season: {} :: Week Number :: {} :: CDC Severity level :: {}".format(
                                    US_STATES[state_id],
                                    mmwr_details.get("weekstart"),
                                    mmwr_details.get("weeknumber"),
                                    mmwr_start_data.get("st_level"))
                            )
                    

if len(sys.argv) == 4:
    state, last_n_years, severity_level = sys.argv[1].upper(), int(sys.argv[2]), int(sys.argv[3])
    re = FluStatus(state, last_n_years, severity_level)
elif len(sys.argv) == 3:
    state, last_n_years = sys.argv[1].upper(), int(sys.argv[2])
    re = FluStatus(state, last_n_years)
else:
    print(
    """
    Usage:

    > python flu.py <STATE> <LAST_N_YEARS> <CDC_SEVERITY_LEVEL>
    > python flu.py CA 3 7

    State : CA :: FLU Season: 2016-04-10 :: Week Number :: 15 :: CDC Severity level :: 7
    State : CA :: FLU Season: 2017-03-19 :: Week Number :: 12 :: CDC Severity level :: 7
    State : CA :: FLU Season: 2017-11-05 :: Week Number :: 45 :: CDC Severity level :: 7
    State : CA :: FLU Season: 2019-04-14 :: Week Number :: 16 :: CDC Severity level :: 7

    """)

