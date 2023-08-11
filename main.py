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

#print("*********************************************************************************************************************")
print("API-Token :" + Token)
#print("*********************************************************************************************************************")

#pedir TopSystem

url1 = "https://sandboxapicdc.cisco.com/api/class/topSystem.json"
header = {
        'content-type': "application/json",
}
API_Cookie = {
    "APIC-Cookie" : pedir_token(conf.usuario,conf.clave)
}

respuesta1 = requests.get(url1, headers=header, cookies=API_Cookie,verify=False)
print(respuesta1.json())


#for i in range (0,4): # cuando es un numero fijo
#     IP_LOCAL = respuesta1.json()["imdata"][i]["topSystem"]["attributes"]["address"]
#     MAC_LOCAL = respuesta1.json()["imdata"][i]["topSystem"]["attributes"]["fabricMAC"]
#     Estado_nodo = respuesta1.json()["imdata"][i]["topSystem"]["attributes"]["state"]
#     print("IP : "+IP_LOCAL+ " / "+ " MAC : "+ MAC_LOCAL+ " / "+ "Estado : " +Estado_nodo )

for i in range (0,int(respuesta1.json()["totalCount"])): # cuando es un numero variable
    IP_LOCAL = respuesta1.json()["imdata"][i]["topSystem"]["attributes"]["address"]
    MAC_LOCAL = respuesta1.json()["imdata"][i]["topSystem"]["attributes"]["fabricMAC"]
    Estado_nodo = respuesta1.json()["imdata"][i]["topSystem"]["attributes"]["state"]
    print("IP : "+IP_LOCAL+ " / "+ " MAC : "+ MAC_LOCAL+ " / "+ "Estado : " +Estado_nodo )