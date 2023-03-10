import bs4
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from novedades.models import Novedades
from circulares.models import Circulares

def update_novedades():
    with requests.Session() as session:
        web_superfinanciera = session.get("https://www.superfinanciera.gov.co/jsp")

    if web_superfinanciera.status_code == 200:
        soup_superfinanciera = BeautifulSoup(web_superfinanciera.text, 'html.parser')
        novedades_superfinanciera = soup_superfinanciera.find_all('div', {'id': 'contenidoBloque232'})
        data = []  # para almacenar los datos

        for novedades in novedades_superfinanciera:
            for novedad in novedades:
                if not isinstance(novedad, bs4.element.NavigableString):
                    elements = novedad.find_all('a', {'class': 'link-new slider-tooltip'})
                    for element in elements:
                        href = "https://www.superfinanciera.gov.co" + element['href']
                        title = element.select_one('.title h4').text
                        intro = element.select_one('.intro p').text.strip().replace('\n', '').replace('\r', '').replace('\t', '')

                        novedadg = Novedades(link=href, titulo=title, intro=intro)

                        # Comprobamos si la novedad ya existe en la base de datos
                        if not Novedades.objects.filter(link=href).exists():
                            # Si no existe, la agregamos
                            novedadg.save()
                            data.append(novedadg)  # agregamos el objeto a la lista

        print("Actualización de novedades completada.")
        return data  # devolvemos la lista completa de objetos actualizados o nuevos en la base de datos





def update_circulares():
    circulares_nuevas = []
    circulares_guardadas = Circulares.objects.all()

    with requests.Session() as session:
        web_superfinanciera = session.get("https://www.superfinanciera.gov.co/jsp")

    if web_superfinanciera.status_code == 200:
        soup_superfinanciera = BeautifulSoup(web_superfinanciera.text, 'html.parser')
        circulares_superfinanciera = soup_superfinanciera.find_all('div', {'id': 'contenidoBloque90820'})

        for circular in circulares_superfinanciera:
            elements = circular.find_all('div', {'class': 'col-10 title-circular'})
            for element in elements:
                a = element.find('a')
                href = a['href']
                link = "https://www.superfinanciera.gov.co" + str(href)

                titulo = a.text

                anexo = element.find('a', {'title': 'Anexo'})
                if anexo is not None:
                    anexo = "https://www.superfinanciera.gov.co" + str(anexo['href'])

                circularg = Circulares(link=link, titulo=titulo, anexo=anexo, fecha=datetime.now())

                # Verificar si la circular ya está guardada
                if circulares_guardadas.filter(link=link).exists():
                    continue
                else:
                    circulares_nuevas.append(circularg)
                    circularg.save()

    return circulares_nuevas