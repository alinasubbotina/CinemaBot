import requests
import json
res = requests.get("https://api-gate2.movieglu.com/cinemaLiveSearch/?query=odeon+cinemas",
                   headers = {
                   "api-version" : "v200", 
                   "Authorization" : "Basic VEVMRTpFQ1RZOTExc1BFWUo=", 
                   "x-api-key" : "vwcrurVcnk8xm71uDtPhv9vfcuHsg4Jw2sKzSs3w",
                   "client" : "TELE",
                   "territory" : "UK",
                   "device-datetime" : "2019-06-02T19:30:50.360Z"
                   })
data = json.loads(res.text)
print(data['cinemas'][0]['city'])
