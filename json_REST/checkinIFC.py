import urllib2
import json
import os
from json import JSONEncoder
import base64

####################################################
# Check-in IFC:
# Check-in the IFC file to the defined Project. First, IFC file is encoded and a ProgressID is obtained
####################################################

def checkIn():

    request = "http://localhost:8082/json"
    with open('login.json', 'r') as login:
        token = json.loads(login.read())['response']['result']
    with open('allProjects.json', 'r') as projects:
        projectpoid = json.loads(projects.read())['response']['result'][0]['oid']

    with open('allDeserializers.json', 'r') as deserializer:
        deserializeroid = json.loads(deserializer.read())['response']['result'][0]['oid']

    comment = "Clinic 3D Model for Demonstration"
    file_name = "Clinic_Model"
    ifc_file = "../Clinic_Model.ifc"
    file_url = "/Users/InBookMode/Documents/PythonClient/Clinic_Model.ifc"

    file_size = os.path.getsize(file_url)
    with open(ifc_file) as ifc:
        encoded_ifc = base64.b64encode(ifc.read())


    req_checkinifc = JSONEncoder().encode({
  "token": "%s" % token,
  "request": {
    "interface": "ServiceInterface",
    "method": "checkin",
    "parameters": {
      "poid": "%s" % projectpoid,
      "comment": "%s" % comment,
      "deserializerOid": "%s" % deserializeroid,
      "fileSize": "%s" % file_size,
      "fileName": "%s" % file_name,
      "data": "%s" % encoded_ifc,
      "merge": "false",
      "sync": "false"
    }
  }
})
    req1 = urllib2.Request(request, req_checkinifc, {'Content-Type': 'application/json'})
    response_checkinIFC = json.load(urllib2.urlopen(req1))
    checkinIFC = open('checkinifc.json', 'w')
    json.dump(response_checkinIFC, checkinIFC, indent=5)
    checkinIFC.close()

####################################################
# Upload IFC:
# ProgressID is retrieved from the auto-generated JSON file and imported to upload IFC file
####################################################

    with open('checkinifc.json', 'r') as checkin:
        checkinifcfile = json.loads(checkin.read())['response']['result']

    req_processifc = JSONEncoder().encode({
  "token": "%s" % token,
  "request": {
    "interface": "Bimsie1NotificationRegistryInterface",
    "method": "getProgress",
    "parameters": {
      "topicId": "%s" %checkinifcfile
    }
  }
})
    req2 = urllib2.Request(request,req_processifc, {'Content-Type': 'application/json'})
    response_processIFC = json.load(urllib2.urlopen(req2))
    processIFC = open('processIFC.json', 'w')
    json.dump(response_processIFC, processIFC, indent=5)
    processIFC.close()

checkIn();