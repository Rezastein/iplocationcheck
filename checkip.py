import socket
import requests
import pprint
import json


apiKey = "914a488ac9e9ba"
while True:
    menu_ = input("\nMenu :\n  1.Website\n  2.Ip address Only\n  e.exit\n\n==> ")
    if menu_ == "1":
        hostname = input("Enter a Domain name: ")
        ip_address = socket.gethostbyname(hostname)

        request_url = "https://ipinfo.io/{}?token={}".format(str(ip_address), str(apiKey))
        reponse = requests.get(request_url)
        geolocation = reponse.content.decode()
        geolocation = json.loads(geolocation)

        for k,v in geolocation.items():
            pprint.pprint(str(k) + ' : ' + str(v))
    elif menu_ == "2":
        ip_address2 = input("Ip Address : ")

        request_url2 = "https://ipinfo.io/{}?token={}".format(str(ip_address2), str(apiKey))
        reponse2 = requests.get(request_url2)
        geolocation2 = reponse2.content.decode()
        geolocation2 = json.loads(geolocation2)

        for i,j in geolocation2.items():
            pprint.pprint(str(i) + ' : ' + str(j))
    else:
        exit()