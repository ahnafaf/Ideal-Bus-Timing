# -*- coding: utf-8 -*-
"""
XxCodingProjectxX

"""

import requests
import json
import pprint

busStop1 = requests.get("https://api.winnipegtransit.com/v3/stops/62024/schedule.json?api-key=hUWGdgaAfmWi4K9aAwJW&end=23:59:00").json()
busStop2 = requests.get("https://api.winnipegtransit.com/v3/stops/61213/schedule.json?api-key=hUWGdgaAfmWi4K9aAwJW&key=BLUE-0-U").json()

# print(json.dumps(busStop2["stop-schedule"]["route-schedules"], indent=1, sort_keys=True))

dictStop2 = busStop2["stop-schedule"]["route-schedules"][0]['scheduled-stops']

# A dictionary which stores the buses that go to UManitoba from Stop 2
bus_timings = {}

for i in range(len(dictStop2)): ## To iterate through the values within the filtered dictionary
    if (dictStop2[i]['variant']['name'] == 'BLUE to University of Manitoba'): ## Checks if the name is UManitoba or not
        bus_timings[f"Bus_{i}"] = dictStop2[i]['times']
    else:
        print("Else")
