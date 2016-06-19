import urllib2
import json
from json import JSONEncoder

####################################################
# Get BIMserver info:
# Creates a JSON object listing information about the BIMserver and configurations
####################################################

def getServerInfo():

    request = "http://localhost:8082/json"
    with open('login.json', 'r') as f:
        token = json.load(f)['response']['result']

    req_server_info = JSONEncoder().encode({
  "token": "%s" % token,
  "request": {
    "interface": "AdminInterface",
    "method": "getBimServerInfo",
    "parameters": {
    }
  }
})
    req1 = urllib2.Request(request, req_server_info, {'Content-Type': 'application/json'})
    response_serverInfo = json.load(urllib2.urlopen(req1))
    serverInfo = open('bimServerInfo.json', 'w')
    json.dump(response_serverInfo, serverInfo, indent=5)
    serverInfo.close()\

getServerInfo()