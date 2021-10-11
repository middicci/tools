# NHTSA Recall history tool
Get last n years of recall history for make model year from nhtsa

# usage

```
> python recalls.py tesla 'model 3' 3

TESLA, MODEL 3, 2017 ::: No of Recalls : 0, No of Complaints : 0
TESLA, MODEL 3, 2018 ::: No of Recalls : 0, No of Complaints : 101
TESLA, MODEL 3, 2019 ::: No of Recalls : 1, No of Complaints : 34
```

# FAA Airport Status for Delays
Get Airport Traffic Delays information from FAA

# usage

```
> python faa.py JFK

John F Kennedy Intl, JFK, New York ::: Delays : False 
Status : No known delays for this airport
Weather : [{'Temp': ['Mostly Cloudy']}]
```

# CDC Flu Stats
Get CDC flu stats for last n years for a state in USA

# usage

```
> python flu.py <STATE> <LAST_N_YEARS> <CDC_SEVERITY_LEVEL>
> python flu.py CA 3 7

State : CA :: FLU Season: 2016-04-10 :: Week Number :: 15 :: CDC Severity level :: 7
State : CA :: FLU Season: 2017-03-19 :: Week Number :: 12 :: CDC Severity level :: 7
State : CA :: FLU Season: 2017-11-05 :: Week Number :: 45 :: CDC Severity level :: 7
State : CA :: FLU Season: 2019-04-14 :: Week Number :: 16 :: CDC Severity level :: 7
```

# Copyright.js

Adds current year to website footer and saves a release cycle.

# usage


```
<body onload="copyright('Company Inc.')">
	<span  class='copyright' ></span>
</body>
```

# Got Vax? COVID19 vaccine availability, Albertsons -> Safeway Pharmacies

```
Usage:

    > python vax.py <City, StateCode>
    > python vax.py 'Tucson, AZ'

    Yay!

    Available @: Albertsons 0960 - 7300 N. Lacholla Blvd, Tucson, AZ, 85741

    Book @: https://kordinator.mhealthcoach.net/vcl/1600124140771

    OR

    Search Appointment @: https://www.mhealthappointments.com/covidappt

    --------------------------------------------------------------------
 ```
