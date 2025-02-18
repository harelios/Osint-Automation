import requests
import datetime 
import time

Sous_Domaine = input("Entrer un nom de domaine : \n")
longueur_mots = int(input("Entrer la plage de mots que vous souhaitez tester (max 114441) : \n"))
with open(f"SubDomains_{Sous_Domaine}_find.txt","w") as output_file:
    with open("Subdomains_wordlist.txt","r") as file:
        lignes = file.readlines()[:longueur_mots]
        date = datetime.datetime.now()
        output_file.write(date.strftime("%d-%m-%Y %H:%M:%S") + "\n")
        for line in lignes:
                test_SousDomaines = line.strip() +"."+ Sous_Domaine
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
                        print(f"Timeout pour le sous domaine {test_SousDomaines}")
                        continue
                except requests.Timeout:    
                    print(f"Timeout pour le sous domaine {test_SousDomaines}")
                if reponse.status_code == 200:
                    print(f"Sous Domaine trouvé : {test_SousDomaines}")
                    output_file.write(f"Sous domaine trouve ! : {test_SousDomaines}\n")
                elif reponse.status_code in [301,302]:
                    print(f"Sous Domaine {test_SousDomaines} existant mais redirigé autre part, code {reponse}")
                    output_file.write(f"Sous domaine {test_SousDomaines} existant mais redirige autre part, code {reponse} \n")
                elif reponse.status_code in [403,401]:
                    print(f"Sous domaine {test_SousDomaines} existant mais accès interdit, code {reponse}")
                    output_file.write(f"Sous domaine {test_SousDomaines} existant mais acces interdit, code {reponse} \n")
                elif reponse.status_code == 404:
                    continue
                else:
                    print(f"Reponse inatendu pour le sous domaine {test_SousDomaines}, code {reponse}")
                    output_file.write(f"Reponse inatendu pour le sous domaine {test_SousDomaines}, code {reponse} \n")
        print("Scan terminé ! \n")
        output_file.write("Scan termine !\n")