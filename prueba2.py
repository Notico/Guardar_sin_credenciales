import requests
import json
import conf

def pedir_token(usuario, clave):
    url = "https://sandboxapicdc.cisco.com/api/aaaLogin.json"

    data = {
        "aaaUser" : {
            "attributes" : {
                "name" : usuario,
                "pwd" : clave
            }
        }
    }
    cabecera = {"content-type":"application/json" }
    requests.packages.urllib3.disable_warnings() #para borrar mensajes de warning
    respuesta=requests.post(url, data= json.dumps(data),headers= cabecera, verify= False)

    respuesta_json=respuesta.json()
    #print(respuesta.json())

    Token = respuesta_json["imdata"][0]["aaaLogin"]["attributes"]["token"]

    return Token
Token = pedir_token(conf.usuario, conf.clave)

#print("API-Token :" + Token)


url2 = "https://sandboxapicdc.cisco.com/api/changeSelfSshKey.json"

data2 = {
    "aaaChangeSshKey": {
        "attributes": {
            "userName": conf.usuario,
            "name": "A",
            "data": ""
        }
    }
}

header2 = {
        'content-type': "application/json",
}
API_Cookie = {
   "APIC-Cookie" : pedir_token(conf.usuario,conf.clave)
}
respuesta2 = requests.post(url2, data= json.dumps(data2), headers=header2, cookies=API_Cookie,verify=False)
print(respuesta2.json())
print(respuesta2)
