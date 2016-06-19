import urllib2
import json
from json import JSONEncoder

####################################################
# Get data based on GUID:
# Returns the data pf the defined GUID of the queried element
####################################################

def getDataByGUID():
    request = "http://localhost:8082/json"
    with open('login.json', 'r') as f:
        token = json.load(f)['response']['result']
    with open('allRevisions.json', 'r') as revisions:
        projectroid = json.loads(revisions.read())['response']['result'][0]['oid']
    guid = "2g$QZpOGbBUxSNx_ZgxGCP"

    req_guid_object = JSONEncoder().encode({
  "token": "%s" % token,
  "request": {
    "interface": "Bimsie1LowLevelInterface",
    "method": "getDataObjectByGuid",
    "parameters": {
      "roid": "%s" %projectroid,
      "guid": "%s" %guid
    }
  }
})
    req1 = urllib2.Request(request, req_guid_object, {'Content-Type': 'application/json'})
    response_getByGUID = json.load(urllib2.urlopen(req1))
    addProject = open('getByGUID.json', 'w')
    json.dump(response_getByGUID, addProject, indent=5)
    addProject.close()\

getDataByGUID()