# -*- coding: utf-8 -*-
"""
XxCodingProjectxX

(dictStop2[i]['times']['arrival']['scheduled'])

# print(json.dumps(busStop2["stop-schedule"]["route-schedules"], indent=1, sort_keys=True))
"""

import requests
import json
import pprint
from datetime import datetime

busStop1 = requests.get("https://api.winnipegtransit.com/v3/stops/62024/schedule.json?api-key=hUWGdgaAfmWi4K9aAwJW&end=23:59:00").json()
busStop2 = requests.get("https://api.winnipegtransit.com/v3/stops/61213/schedule.json?api-key=hUWGdgaAfmWi4K9aAwJW&key=BLUE-0-U").json()

## Slicing the original dictionary to filter out what we want
dictStop2 = busStop2["stop-schedule"]["route-schedules"][0]['scheduled-stops']
dictStop1 = busStop1["stop-schedule"]["route-schedules"][0]['scheduled-stops'] 

# Dictonaries which stores the buses that go to UManitoba from Stop 2 and 1
bus_timings2 = {} 
bus_timings1 = {}

# Function that goes into dictionary maker to return datetime object into the bus_timings dictionary
def timeTransform(dateString):
    return datetime.strptime(dateString, '%Y-%m-%dT%H:%M:%S')


def dictMaker(busDict1, busDict2):  
    for i in range(len(busDict1)): ## To iterate through the values within the filtered dictionary
        if (busDict1[i]['variant']['name'] == 'River Road to St. Vital Centre via River Road'): ## Checks if the name is UManitoba or not
            bus_timings1[f"Bus_{i}"] = timeTransform(busDict1[i]['times']['arrival']['scheduled'])
        else:
            print("Else")
            
    for i in range(len(busDict2)): ## To iterate through the values within the filtered dictionary
        if (busDict2[i]['variant']['name'] == 'BLUE to University of Manitoba'): ## Checks if the name is UManitoba or not
            bus_timings2[f"Bus_{i}"] = timeTransform(busDict2[i]['times']['arrival']['scheduled'])
        else:
            print("Else")

dictMaker(dictStop1,dictStop2)
                
    
        
