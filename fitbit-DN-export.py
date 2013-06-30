import fitbit
import json
import os

DNconsumer_key = os.getenv('DNconsumer_key')
DNconsumer_secret = os.getenv('DNconsumer_secret')
DNuser_key = os.getenv('DNuser_key')
DNuser_secret = os.getenv('DNuser_secret')

fb = fitbit.Fitbit(DNconsumer_key, DNconsumer_secret, 
	user_key=DNuser_key, user_secret=DNuser_secret)

datpath = 'DNfitbit/'
trackr = '30d'

steps = fb.time_series('activities/steps', base_date='today',period=trackr)['activities-steps']
distance = fb.time_series('activities/distance', base_date='today',period=trackr)['activities-distance']
sleeps = fb.time_series('sleep/minutesAsleep', base_date='today',period=trackr)['sleep-minutesAsleep']

# Export STEPS
with open(datpath + 'steps.json', 'w') as file:
    for st in steps:
    	file.write(json.dumps(st) + '\n')
    print 'cat ' + datpath + 'steps.json'

# Export DISTANCE
with open(datpath + 'distance.json', 'w') as file:
	for dist in distance:
		file.write(json.dumps(dist) + '\n')
	print 'cat ' + datpath + 'distance.json'

# Export NAPS
with open(datpath + 'naps.json', 'w') as file:
	for naps in sleeps:
		file.write(json.dumps(naps) + '\n')
	print 'cat ' + datpath + 'naps.json'