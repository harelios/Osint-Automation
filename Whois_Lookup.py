import whois
import datetime
import json



def format_date(date_value):
    """Convertit une date en chaîne de caractères ou la laisse vide si None"""
    if isinstance(date_value, list):  # Certains WHOIS retournent une liste de dates
        return [d.strftime("%Y-%m-%d %H:%M:%S") if isinstance(d, datetime.datetime) else str(d) for d in date_value]
    return date_value.strftime("%Y-%m-%d %H:%M:%S") if isinstance(date_value, datetime.datetime) else str(date_value)


def get_whois_info(domain=None):
    if not domain:
        domain = input("Enter a domain name for the whois lookup (example.com) : \n")

    whois_request = whois.whois(domain)
    date = datetime.datetime.now()
    with open(f"Whois_{domain}.txt", "w" ) as file:
        try:
            print("----------Whois information----------")
            Domain_name = f"{whois_request.domain_name} \n"
            Registrar = f"{whois_request.registrar} \n"
            Creation_Date = f"{format_date(whois_request.creation_date)} \n"
            Expiration_Date = f"{format_date(whois_request.expiration_date)} \n"
            Last_Updated_Date = f"{format_date(whois_request.updated_date)} \n"
            Dns_Server = f"{whois_request.name_servers} \n"
            Status = f"{whois_request.status} \n"
            Emails = f"{whois_request.emails} \n"
            file.write(date.strftime("%d-%m-%Y %H-%M-%S") + "\n")
            whois_request = str(whois_request)
            file.write(whois_request)
        except Exception as e: 
            return f"Error retrieving Whois information : {e} \n"
        if Domain_name and Registrar and Creation_Date and Expiration_Date and Last_Updated_Date and Dns_Server and Status and Emails == None:
            return f"Error in trying to get the informations about {domain}, maybe the name entered is wrong, verify and try again \n"
    return f"Domain_name : {Domain_name}\n Registrar : {Registrar} \n Creation_Date : {Creation_Date} \n Expiration_Date : {Expiration_Date} \n Last_Updated_Date : {Last_Updated_Date} \n  Dns_Server : {Dns_Server} \n Status : {Status} \n Emails : {Emails} \n"
    
def save_as_json(domaine):
    whois_request = whois.whois(domaine)
    data = {"Domaine Name" : whois_request.domain_name, "Registrar" : whois_request.registrar, "Creation Date" : format_date(whois_request.creation_data), "Expiration Date" : format_date(whois_request.expiration_date), 
            "Last Updated Date" :format_date(whois_request.update_date),"DNS Servers" : whois_request.name_servers, "Status" : whois_request.status, "Emails" : whois_request.emails}
    with open(f"Whois_{domaine}.json", "w") as file:
        json.dump(data,file, indent=5)
    return f"Données bien écrites dans Whois_{domaine}.json"

if __name__ =="__main__":
    get_whois_info()

