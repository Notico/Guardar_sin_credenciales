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

print("API-Token :" + Token)


url2 = "https://sandboxapicdc.cisco.com/api/changeSelfPassword.json"
user = input("nombre de usuario : ")
clave_antigua= input("ingrese su clave antigua : ")
clave_nueva= input("ingrese su clave nueva : ")

data2 = {
    "aaaUser" : {
        "attributes" : {
            "userName" : user,
            "oldPassword" : clave_antigua,
            "newPassword": clave_nueva
        }
    }
}
cabecera2 = {"content-type":"application/json" }
requests.packages.urllib3.disable_warnings() #para borrar mensajes de warning

API_Cookie = {
   "APIC-Cookie" : pedir_token(conf.usuario,conf.clave)
}

res=requests.post(url2, data= json.dumps(data2),headers= cabecera2, cookies=API_Cookie,verify= False)

res_json=res.json()
print(res.json())

#Token = res_json["imdata"][0]["aaaLogin"]["attributes"]["token"]


