import urllib2
import json
from json import JSONEncoder

####################################################
# Get all Deserializers:
# Creates a JSON object listing all the deserializers with a UID. UIDs are used later progresses
####################################################

def getAllDeserializers():

    request = "http://localhost:8082/json"
    with open('login.json', 'r') as f:
        token = json.load(f)['response']['result']

    req_all_deserializers = JSONEncoder().encode({
  "token":  "%s" % token,
  "request": {
    "interface": "PluginInterface",
    "method": "getAllDeserializers",
    "parameters": {
      "onlyEnabled": "false"
    }
  }
})
    req1 = urllib2.Request(request, req_all_deserializers, {'Content-Type': 'application/json'})
    response_Deserializers = json.load(urllib2.urlopen(req1))
    allDeserializers = open('allDeserializers.json', 'w')
    json.dump(response_Deserializers, allDeserializers, indent=5)
    allDeserializers.close()\

getAllDeserializers()
