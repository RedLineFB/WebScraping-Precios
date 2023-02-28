import requests
from bs4 import BeautifulSoup

print("\n\nCreado por: RedLineFB\n")
print("\n\nBIENVENIDO A WebScraping-Precios\n")
sitio= input("Ingrese un sitio web: ") #URL para extraer los datos
respuesta= requests.get(sitio)#Enviar una solicitud al sitio
soup= BeautifulSoup(respuesta.content, 'html.parser')
list= soup.find_all("div", class_="product text-left")

for f in list:
    enlaces_nombres= f.find("div", class_="product--data--info").text
    enlaces_precios= f.find("span", class_="woocommerce-Price-currencySymbol").text
    with open("precios.txt", 'a') as file:
        file.write(enlaces_nombres)
        print("\n")
        file.write(enlaces_precios)
        


