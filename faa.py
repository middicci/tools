import urllib3
import datetime
import sys
import json
http = urllib3.PoolManager()

class AirportStatus:
    def __init__(self, airport_code):
        self.API_URL = "https://soa.smext.faa.gov/asws/api/airport/status/{}"
        self.details = []
        self.airport_delays(airport_code)
        self._display()

    def _get_faa_data(self, airport_code):
        r = http.request('GET', self.API_URL.format(airport_code))
        data = {}
        if r.status == 200:
            data = r.data
        return data

    def airport_delays(self, airport_code):
        self.details.append(self._get_faa_data(airport_code))

    def _display(self):
        for airport in self.details:
            resp = json.loads((airport.decode('utf-8')))            
            print ("{}, {}, {} ::: Delays : {} \nStatus : {}\nWeather : {}".format(
                resp.get('Name'),
            	resp.get('IATA'),
            	resp.get('City'),
            	resp.get('Delay'),
            	resp.get('Status')[0].get('Reason'),
                resp.get('Weather').get('Weather'),
                )
            )


if len(sys.argv) != 3:
    airport_code = sys.argv[1].upper()
    re = AirportStatus(airport_code)
else:
    print(
    """
    Usage:

    > python faa.py JFK

    John F Kennedy Intl, JFK, New York ::: Delays : False 
    Status : No known delays for this airport
    Weather : [{'Temp': ['Mostly Cloudy']}]

    """)
