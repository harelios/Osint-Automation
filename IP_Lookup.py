import requests
import json

ip = input("Enter an ip adress for the IP Lookup : \n")
def ip_lookup(ip):
    Api_Keys = "847ca7c5b64d1154d51c0db17ddcf2a5"
    url = f"http://api.ipstack.com/{ip}?access_key={Api_Keys}"
    response = requests.get(url)
    data = response.json()
    if "error" in data:
        print(f"Erreur : {data["error"]["info"]}")
        return 
    
    result = {"IP" : data.get("ip", "N/A"), "Continent" : data.get("continent_name", "N/A"),"Country" : data.get("country_name", "N/A"),
              "Region" :data.get("region_name","N/A"), "City" : data.get("city", "N/A"), "Zip Code": data.get("zip", "N/A"),
              "Latitude": data.get("latitude", "N/A"), "Longitude" : data.get("longitude", "N/A"),
              "Connexion's Type" : data.get("type", "N/A")}
    print("Resultat IP Lookup : \n")
    for key,value in result.items():
        print(f"{key} : {value}")
    
    with open(f"IP_Lookup_{ip}.json", "w") as file:
        json.dump(result,file,indent=5)

ip_lookup(ip)
