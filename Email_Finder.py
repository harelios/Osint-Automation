from bs4 import BeautifulSoup as soup
import requests
import re
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def email_finder(url):
    #webdriver
    options = Options()
    options.add_argument("--headless") #mode headless (to not display the navigators each time we run the program
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--windows-size=19201080")

    service = Service(r"C:/Users/Proprietaire/chromedriver-win64/chromedriver-win64/chromedriver.exe") #Path to the webdriver
    driver = webdriver.Chrome(service=service, options=options) #Webdriver

    Domain = input("Enter a domain's name to scan (exemple : example.com) : \n")
    url = f"https://www.{Domain}"
    email_list = []
    regex = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}"   
    response = requests.get(url)
    invalide_type = [".png",".jpg",".gif",".webp",".svg"]
    
    #   We start to see if the page is written in html    
    if response.status_code == 200:
        print(f"HTTP request to the website {url} successful ")
        html_text = soup(response.content,"html.parser").get_text()
        print(driver.page_source)
        email = re.findall(regex,html_text)
        #emails = set(emails) #to prevent the same emails twice
        email_list.extend(email)
    #if the list doesn't return anything (list empty), we try to see if the page is write in javascript
    if not email_list:
            try: 
                driver.get(url)
                sleep(5)
                javascript_text = driver.page_source
                email = re.findall(regex, javascript_text)
                email_list.extend(email)
            except Exception as e:
                    print(f"Aucun site {e} trouver")    
                    driver.quit()
                    return f"Aucun site {e} trouver"
                

    filtered_email = []
    for i in email_list:
        is_valid = True
        for element in invalide_type:
            if i.lower().endswith(element):
                is_valid = False
                break
            if is_valid == True:
                filtered_email.append(i)
    
    driver.quit()    
    return f"Email(s) found : {filtered_email}"
    


