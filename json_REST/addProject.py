import urllib2
import json
from json import JSONEncoder

####################################################
# Define Project:
# Add a new project to BIMServer. IFC file will be uploaded from different script
####################################################

def addProject():

    request = "http://localhost:8082/json"
    with open('login.json', 'r') as f:
        token = json.load(f)['response']['result']

    ## Define a project name and choose the IFC schema ##
    project_name = "ClassDemo_Project"
    schema1 = "ifc2x3tc1"
    schema2 = "ifc4"

    req_addProject = JSONEncoder().encode({
  "token": "%s" % token,
  "request": {
    "interface": "Bimsie1ServiceInterface",
    "method": "addProject",
    "parameters": {
      "projectName": "%s" % project_name,
      "schema": "%s" % schema1
    }
  }
})
    req1 = urllib2.Request(request, req_addProject, {'Content-Type': 'application/json'})
    response_addProject = json.load(urllib2.urlopen(req1))
    addProject = open('addProject.json', 'w')
    json.dump(response_addProject, addProject, indent=5)
    addProject.close()\

addProject()