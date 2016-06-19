import urllib2
import json
from json import JSONEncoder

####################################################
# Get all Projects:
# Creates a JSON object listing all the defined projects with a UID. UIDs are used later progresses
####################################################

def getAllProjects():

    request = "http://localhost:8082/json"
    with open('login.json', 'r') as f:
        token = json.load(f)['response']['result']

    req_all_projects = JSONEncoder().encode({
  "token": "%s" % token,
  "request": {
    "interface": "Bimsie1ServiceInterface",
    "method": "getAllProjects",
    "parameters": {
      "onlyTopLevel": "false",
      "onlyActive": "false"
    }
  }
})
    req1 = urllib2.Request(request, req_all_projects, {'Content-Type': 'application/json'})
    response_getAllProjects = json.load(urllib2.urlopen(req1))
    allProjects = open('allProjects.json', 'w')
    json.dump(response_getAllProjects, allProjects, indent=5)
    allProjects.close()

getAllProjects()