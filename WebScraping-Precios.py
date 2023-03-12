import requests
from bs4 import BeautifulSoup

print("\n\nCreado por: RedLineFB\n")
print("\n\nBIENVENIDO A WebScraping-Precios\n")
sitio= input("Ingrese un sitio web: ") #URL para extraer los datos
respuesta= requests.get(sitio)#Enviar una solicitud al sitio
soup= BeautifulSoup(respuesta.content, 'html.parser')
list= soup.find_all("AGREGAR VARIABLE DE LA CLASE", class_="AGREGAR VARIABLE DE LA CLASE")

for f in list:
    enlaces_nombres= f.find("div", class_="AGREGAR VARIABLE DE LA CLASE").text
    enlaces_precios= f.find("span", class_="AGREGAR VARIABLE DE LA CLASE").text
    with open("precios.txt", 'a') as file:
        file.write(enlaces_nombres)
        print("\n")
        file.write(enlaces_precios)
        


