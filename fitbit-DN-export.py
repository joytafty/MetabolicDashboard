import fitbit
import json

DNconsumer_key = 'e83cb29ae0f0439e8aeb2704b5e9eaa4'
DNconsumer_secret = '77fdd761c63247868627cc4ed2114306'
DNuser_key = 'e543804b25d1aba781d1d8472eb899bd'
DNuser_secret = '4d8da8bf4adc2df317d32ed86c8bc1c1'

fb = fitbit.Fitbit(DNconsumer_key, DNconsumer_secret, 
	user_key=DNuser_key, user_secret=DNuser_secret)

datpath = 'DNfitbit/'
trackr = '30d'

# Export STEPS
with open(datpath + 'steps.json', 'w') as file:
    for steps in fb.time_series('activities/steps', 
    	base_date='today', period=trackr)['activities-steps']:
    	file.write(json.dumps(steps) + '\n')
    print 'cat ' + datpath + 'steps.json'

# Export SLEEP
with open(datpath + 'distance.json', 'w') as file:
	for distance in fb.time_series('activities/distance', 
		base_date='today', period=trackr)['activities-distance']:
		file.write(json.dumps(distance) + '\n')
	print 'cat ' + datpath + 'distance.json'

# Export NAPS
with open(datpath + 'naps.json', 'w') as file:
	for naps in fb.time_series('sleep/minutesAsleep', 
		base_date='today', period=trackr)['sleep-minutesAsleep']:
		file.write(json.dumps(naps) + '\n')
	print 'cat ' + datpath + 'naps.json'