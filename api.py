
import requests
import json
from datetime import date

x = input("Enter the place ")
parameters = {
    "q":x,
    "key":"aad0de9f9034493591f07d83c0806ef6"
}

response = requests.get("https://api.opencagedata.com/geocode/v1/json",params=parameters)

print(response.status_code)
val = response.json()



if(response.status_code == 200):
        print(json.dumps(val['results'][0]['bounds']['southwest'],sort_keys=True, indent=4))

        lat = val['results'][0]['bounds']['southwest']['lat']
        lon = val['results'][0]['bounds']['southwest']['lng']

        locationParam= {
            "lat":lat,
            "lon":lon
        }

        response2 = requests.get("http://api.open-notify.org/iss-pass.json",params=locationParam)
        if(response2.status_code ==200):

            timeval = response2.json()
            timestamp = date.fromtimestamp(timeval['request']['datetime'])
            print("The ISS will be visible over",x, " at ",timestamp," for ",timeval['request']['passes'],"passes at an altitude of ",timeval['request']['altitude'])
        #print(response2.status_code)

        #print(json.dumps(response2.json(),sort_keys=True,indent=4))
        else:
            print("Couldn't fetch data")


else:
    print("COuldn't retrieve data")



