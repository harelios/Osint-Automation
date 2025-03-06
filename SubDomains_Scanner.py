import requests
import datetime 
import time



def Subdomains_Scanner(SubDomains=None,Words_Length=None):
    if not SubDomains:
        SubDomains = input("Entrer un nom de domaine : \n")
    
    if not Words_Length: 
        Words_Length = int(input("Entrer la plage de mots que vous souhaitez tester (max 114441) : \n"))
    with open(f"SubDomains_{SubDomains}_find.txt","w") as output_file:
        with open("Subdomains_wordlist.txt","r") as file:
            lignes = file.readlines()[:Words_Length]
            date = datetime.datetime.now()
            output_file.write(date.strftime("%d-%m-%Y %H:%M:%S") + "\n")
            for line in lignes:
                    test_SousDomaines = line.strip() +"."+ SubDomains
                    url = f"https://{test_SousDomaines}"
                    try:
                        reponse = requests.get(url, timeout=5)
                        time.sleep(2)
                    except requests.exceptions.ConnectionError: 
                        url = f"http://{test_SousDomaines}" #Si https ne fonctionne pas, essayer http
                        try:
                            reponse = requests.get(url, timeout=5)
                            time.sleep(2)
                        except requests.exceptions.ConnectionError:
                            continue
                        except requests.exceptions.Timeout:
                            result = f"Timeout pour le sous domaine {test_SousDomaines}"
                            yield result
                            continue
                    except requests.Timeout:    
                        result =  f"Timeout pour le sous domaine {test_SousDomaines}"
                        yield result
                    if reponse.status_code == 200:
                        result = f"Sous Domaine trouvé : {test_SousDomaines}"
                        yield result
                        output_file.write(f"Sous domaine trouve ! : {test_SousDomaines}\n")
                    elif reponse.status_code in [301,302]:
                        result =  f"Sous Domaine {test_SousDomaines} existant mais redirigé autre part, code {reponse}"
                        yield result
                        output_file.write(f"Sous domaine {test_SousDomaines} existant mais redirige autre part, code {reponse} \n")
                    elif reponse.status_code in [403,401]:
                        result =  f"Sous domaine {test_SousDomaines} existant mais accès interdit, code {reponse}"
                        yield result
                        output_file.write(f"Sous domaine {test_SousDomaines} existant mais acces interdit, code {reponse} \n")
                    elif reponse.status_code == 404:
                        continue
                    else:
                        result =  f"Reponse inatendu pour le sous domaine {test_SousDomaines}, code {reponse}"
                        yield result
                        output_file.write(f"Reponse inatendu pour le sous domaine {test_SousDomaines}, code {reponse} \n")
            result =  "Scan terminé ! \n"            
            yield result
            output_file.write("Scan termine !\n")
            
            
if __name__ == "__main__":
    Subdomains_Scanner()