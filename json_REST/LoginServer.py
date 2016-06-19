import urllib2
import json
from json import JSONEncoder
import pickle

####################################################
# Login Server:
# Logs-in the user to the BIMserver. Function asks username and password variables
####################################################

def login_BIMserver(username, password):

    request = "http://localhost:8082/json"
    req_login = JSONEncoder().encode({
      "request": {
        "interface": "Bimsie1AuthInterface",
        "method": "login",
        "parameters": {
          "username": "%s" % username,
          "password": "%s" % password
        }
      }
    })
    req1 = urllib2.Request(request, req_login, {'Content-Type': 'application/json'})
    response_login = json.load(urllib2.urlopen(req1))
    login_json = open('login.json', 'w')
    json.dump(response_login, login_json, indent=5)
    login_json.close()

login_BIMserver("admin@bimserver.org", "admin")
