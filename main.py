import requests
import json
import conf

print(conf.clave)
print(conf.usuario)
url = "https://sandboxapicdc.cisco.com/api/aaaLogin.json"

data = {
    "aaaUser" : {
        "attributes" : {
            "name" : "admin",
            "pwd" : "!v3G@!4@Y"
        }
    }
}
cabecera = {"content-type":"application/json" }
requests.packages.urllib3.disable_warnings() #para borrar mensajes de warning
respuesta=requests.post(url, data= json.dumps(data),headers= cabecera, verify= False)

respuesta_json=respuesta.json()
print(respuesta.json())

API_Token = respuesta_json["imdata"][0]["aaaLogin"]["attributes"]["token"]

print("***************************************")
print("API-Token :"+API_Token)
print("***************************************")




# pedir TopSystem

#url1 = "https://sandboxapicdc.cisco.com/api/class/topSystem.json"
#header = {
#        'content-type': "application/json",
#}
#API_Cookie = {
#    "APIC-Cookie" : pedir_token()
#}

#respuesta1 = requests.get(url1, headers=header, cookies=API_Cookie,verify=False)
#print(respuesta1.json())
