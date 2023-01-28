# -*- coding: utf-8 -*-
"""
XxCodingProjectxX

(dictStop2[i]['times']['arrival']['scheduled'])

# print(json.dumps(busStop2["stop-schedule"]["route-schedules"], indent=1, sort_keys=True))


date difference

then use datediff.minutes

print(json.dumps(busStop1["stop-schedule"]["route-schedules"][0], indent=1, sort_keys=True))

https://api.winnipegtransit.com/v3/stops/61213/schedule.json?api-key=hUWGdgaAfmWi4K9aAwJW&key=BLUE-0-U

    for p in itertools.product(bus_timings1.values(), bus_timings2.values()):
        print(p)
"""

import requests
import json
import pprint
from datetime import datetime
from datetime import timedelta
import itertools


busStop1 = requests.get("https://api.winnipegtransit.com/v3/stops/60185/schedule.json?api-key=hUWGdgaAfmWi4K9aAwJW&start=06:00:00&end=23:59:00").json()
busStop2 = requests.get("https://api.winnipegtransit.com/v3/stops/61213/schedule.json?api-key=hUWGdgaAfmWi4K9aAwJW&key=BLUE-0-U&start=06:00:00&end=23:59:00").json()

## Slicing the original dictionary to filter out what we want, which is the steps processed, otherwise it is a dictionary and values of time cannot be accessed.
dictStop2 = busStop2["stop-schedule"]["route-schedules"][0]['scheduled-stops']
dictStop1 = busStop1["stop-schedule"]["route-schedules"][0]['scheduled-stops'] 

# empty list of difference of times
timeDiff = []



def timeTransform(dateString):
    """Parses the time string to object"""
    return datetime.strptime(dateString, '%Y-%m-%dT%H:%M:%S')

def dictMaker(busDict1, busDict2):  
    """Dictonaries which stores the buses that go to UManitoba from Stop 2 and 1"""
    bus_timings2 = [] 
    bus_timings1 = []
    for i in range(len(busDict1)): ## To iterate through the values within the filtered dictionary for bus1
        if (busDict1[i]['variant']['name'] == 'River Road to St. Vital Centre via River Road'): ## Checks if the name is UManitoba or not
            bus_timings1.append(timeTransform(busDict1[i]['times']['arrival']['scheduled'])) #s ets the dictionary of timings for bus1
    for i in range(len(busDict2)): ## To iterate through the values within the filtered dictionary for bus2
        if (busDict2[i]['variant']['name'] == 'BLUE to University of Manitoba'): ## Checks if the name is UManitoba or not
            bus_timings2.append(timeTransform(busDict2[i]['times']['arrival']['scheduled']))
    return bus_timings1, bus_timings2


bus_timings1, bus_timings2 = dictMaker(dictStop1,dictStop2) # b_t1 holds all the bus timings going to the UofM bus


## Function that goes into dictionary maker to return datetime object into the bus_timings dictionary
##First get each dates from the dictionaries
for p, v in itertools.product(bus_timings1, bus_timings2):
    if (v > p and (v - p < timedelta(seconds=600))):
        timeDiff.append(str(v-p))