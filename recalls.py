import urllib3
import datetime
import sys
import json
http = urllib3.PoolManager()

class Recall:
    def __init__(self, make, model, last_n_years):
        self.API_URL = "https://api.nhtsa.gov/vehicles/byYmmt?make={}&model={}&modelYear={}&productDetail=all"
        self.details = []
        self.recall_history(make.upper(), model.upper(), last_n_years)
        self._display()

    def _get_nhtsa_data(self, make, model, year):
        r = http.request('GET', self.API_URL.format(make, model, year))
        data = {}
        if r.status == 200:
            data = r.data
        return data

    def recall_history(self, make, model, last_n_years):
        now = datetime.datetime.now()
        current_year = now.year
        for year in range(current_year - last_n_years, current_year):
            self.details.append(self._get_nhtsa_data(make, model, year))

    def _display(self):
        for product in self.details:
            resp = json.loads((product.decode('utf-8')))
            if resp.get('results'):
	            print ("{}, {}, {} ::: No of Recalls : {}, No of Complaints : {}".format(resp.get('results')[0].get('make'),
	            	resp.get('results')[0].get('vehicleModel'),
	            	resp.get('results')[0].get('modelYear'),
	            	resp.get('results')[0].get('recallsCount'),
	            	resp.get('results')[0].get('complaintsCount')))


if len(sys.argv) > 3:
    make, model, last_n_years = sys.argv[1].upper(), sys.argv[2].upper(), int(sys.argv[3])
    re = Recall(make, model, last_n_years)
else:
    print(
    """
    Usage:
    > python recalls.py tesla 'model 3' 3

    TESLA, MODEL 3, 2017 ::: No of Recalls : 0, No of Complaints : 0
    TESLA, MODEL 3, 2018 ::: No of Recalls : 0, No of Complaints : 101
    TESLA, MODEL 3, 2019 ::: No of Recalls : 1, No of Complaints : 34

    """)


