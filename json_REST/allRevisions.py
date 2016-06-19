import urllib2
import json
from json import JSONEncoder

####################################################
# Get all Revisions:
# Creates a JSON object listing all the revisions of the project with a OID. OIDs are used later progresses
####################################################

def getAllRevisions():

    request = "http://localhost:8082/json"
    with open('login.json', 'r') as f:
        token = json.load(f)['response']['result']
    with open('allProjects.json', 'r') as project:
        poid = json.load(project)['response']['result'][0]['oid']

    req_all_revisions = JSONEncoder().encode({
  "token": "%s" % token,
  "request": {
    "interface": "Bimsie1ServiceInterface",
    "method": "getAllRevisionsOfProject",
    "parameters": {
      "poid": "%s" % poid
    }
  }
})
    req1 = urllib2.Request(request, req_all_revisions, {'Content-Type': 'application/json'})
    response_Revisions = json.load(urllib2.urlopen(req1))
    allRevisions = open('allRevisions.json', 'w')
    json.dump(response_Revisions, allRevisions, indent=5)
    allRevisions.close()

getAllRevisions()
