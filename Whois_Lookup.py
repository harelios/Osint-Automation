import whois
import datetime
import json

domaine = input("Enter a domain name for the whois lookup (example.com) : \n")


def format_date(date_value):
    """Convertit une date en chaîne de caractères ou la laisse vide si None"""
    if isinstance(date_value, list):  # Certains WHOIS retournent une liste de dates
        return [d.strftime("%Y-%m-%d %H:%M:%S") if isinstance(d, datetime.datetime) else str(d) for d in date_value]
    return date_value.strftime("%Y-%m-%d %H:%M:%S") if isinstance(date_value, datetime.datetime) else str(date_value)


def get_whois_info(domaine):
    whois_request = whois.whois(domaine)
    date = datetime.datetime.now()
    with open(f"Whois_{domaine}.txt", "w" ) as file:
        try:
            print("----------Whois information----------")
            print(f"Domaine name : {whois_request.domain_name} \n")
            print(f"Registrar : {whois_request.registrar} \n")
            print(f"creation date : {whois_request.creation_date} \n")
            print(f"Expiration date : {whois_request.expiration_date} \n")
            print(f"Last updated date : {whois_request.updated_date} \n ")
            print(f"DNS servers : {whois_request.name_servers} \n")
            print(f"Status : {whois_request.status} \n")
            print(f"Emails : {whois_request.emails} \n")
            file.write(date.strftime("%d-%m-%Y %H-%M-%S") + "\n")
            whois_request = str(whois_request)
            file.write(whois_request)
        except Exception as e: 
            print(f"Erreur lors de la récupération des informations WHOIS : {e}")


def save_as_json(domaine):
    whois_request = whois.whois(domaine)
    data = {"Domaine Name" : whois_request.domain_name, "Registrar" : whois_request.registrar, "Creation Date" : format_date(whois_request.creation_data), "Expiration Date" : format_date(whois_request.expiration_date), 
            "Last Updated Date" :format_date(whois_request.update_date),"DNS Servers" : whois_request.name_servers, "Status" : whois_request.status, "Emails" : whois_request.emails}
    with open(f"Whois_{domaine}.json", "w") as file:
        json.dump(data,file, indent=5)
    print(f"Données bien écrites dans Whois_{domaine}.json")

get_whois_info(domaine)
save_as_json(domaine)