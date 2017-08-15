#Load necessary packages 

import requests
import json 

#List of API URL's for various API calls 

api_list = ['https://misslola.harvestapp.com/people.json', 'https://misslola.harvestapp.com/daily.json']

#For Loop looping each API URL 
#Loop then converts, prints, and saves each API call as a JSON file 

for api in api_list:
	json_data = requests.get(api, auth=('pschwarts@luc.edu', 'ps072017'))
	json_data.json()
	jf = json_data.json()
	print(json.dumps(jf,indent=4))
	pprint = (json.dumps(jf,indent=4))
	#with open('api', 'w') as f:
		#f.write(pprint)