""" 
Got VAX?

COVID19 Vaccine Availability in US for Albertsons -> Safeway Pharmacies
"""

import urllib3
import datetime
import sys
import json
http = urllib3.PoolManager()

API_URL = "https://s3-us-west-2.amazonaws.com/mhc.cdn.content/vaccineAvailability.json?v=1618618362217"


class VaxStatus:
    def __init__(self, city_state):
        self.city_state = city_state
        self.details = []
        self._display()

    def _get_data(self):
        r = http.request('GET',
                         API_URL,
                         headers={  'Accept': 'application/json, text/plain, */*',
                                    'Content-Type': 'application/json'
                                 }
                         )
        data = {}
        if r.status == 200:
            data = json.loads(r.data)
        return data

    def _availibility(self):
        self.details = self._get_data()

    def _display(self):
        self._availibility()
        for record in self.details:            
            if record.get('availability') == 'yes' and self.city_state in record.get('address'):
                print('{0:<3}Yay!\n\n'.format(''))
                print(' Available @: {}\n'.format(record.get('address')))
                print(' Book @: {}\n'.format(record.get('coach_url')))
                print('{0:<3}OR\n'.format(''))
                print(' Search Appointment @: https://www.mhealthappointments.com/covidappt\n\n')
                print('--------------------------------------------------------------------: \n\n')


if len(sys.argv) == 2:
    city_state = sys.argv[1]
    re = VaxStatus(city_state=city_state)
else:
    print(
    """
    Usage:

    > python vax.py <City, StateCode>
    > python vax.py 'Tucson, AZ'

    Yay!

    Available @: Albertsons 0960 - 7300 N. Lacholla Blvd, Tucson, AZ, 85741

    Book @: https://kordinator.mhealthcoach.net/vcl/1600124140771

    OR

    Search Appointment @: https://www.mhealthappointments.com/covidappt

    --------------------------------------------------------------------

    """)

