try:
    import requests
except ImportError:
    os.system('pip install requests')
    print('Installing requests...')
    print('Ejecuta de nuevo tu script...')
    exit()

try:
    import os
except ImportError:
    os.system('pip install os')
    print('Installing os...')
    print('Ejecuta de nuevo tu script...')
    exit()

try:
    import sys
except ImportError:
    os.system('pip install sys')
    print('Installing sys...')
    print('Ejecuta de nuevo tu script...')
    exit()

try:
    from bs4 import BeautifulSoup as bs
except ImportError:
    os.system('pip install BeautifulSoup')
    print('Installing BeautifulSoup...')
    print('Ejecuta de nuevo tu script...')
    exit()

try:
    import webbrowser
except ImportError:
    os.system('pip install webbrowser')
    print('Installing webbrowser...')
    print('Ejecuta de nuevo tu script...')
    exit()

""" Jordan Garcia Bernal
lo que realiza el script es buscar desde el numero de pagina que introdujo
el usuario como inicial hasta la que introdujo como final noticias
relacionadasa las siglas de la facultad que escogio el usuario y si es
que hay noticias que abrir se abre una pestaña en el buscador mostrando
la noticia o noticias encontradas, despues el script se finaliza."""

verificador = 1

print("Este script navega en las páginas de noticas de la UANL")
while verificador == 1:
    try:
        inicioRango = int(input("Pagina inicial para buscar: "))
        verificador = 0
    except ValueError:
        print("Error, introducir un numero")
verificador = 1
while verificador == 1:
    try:
        finRango = int(input("Pagina final para buscar: "))
        verificador = 0
    except ValueError:
        print("Error, introducir un numero")
dependencia = input("Ingrese las siglas de la Facultad a buscar: ")
if inicioRango > finRango:
    inicioRango, finRango = finRango, inicioRango
for i in range(inicioRango, finRango, 1):
    url = "https://www.uanl.mx/noticias/page/"+str(i)
    pagina = requests.get(url)
    if pagina.status_code != 200:
        raise TypeError("Pagina no encontrada")
    else:
        soup = bs(pagina.content, "html.parser")
        info = soup.select("h3 a")
        for etiqueta in info:
            url2 = etiqueta.get("href")
            pagina2 = requests.get(url2)
            if pagina2.status_code == 200:
                soup2 = bs(pagina2.content, "html.parser")
                parrafos = soup2.select("p")
                for elemento in parrafos:
                    if dependencia in elemento.getText():
                        print ("Abriendo", url2)
                        webbrowser.open(url2)
                        break
