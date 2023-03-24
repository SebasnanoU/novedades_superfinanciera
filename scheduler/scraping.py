import bs4
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from novedades.models import Novedades
from circulares.models import Circulares


def get_superfinanciera():
    with requests.Session() as session:
        web_superfinanciera = session.get("https://www.superfinanciera.gov.co/jsp")
    if web_superfinanciera.status_code == 200:
        return web_superfinanciera


def update_novedades(web_superfinanciera):
    print("Actualizando novedades...")
    print("Obteniendo datos de la web de la Superfinanciera...")
    print("Hora de ejecución:", datetime.now())
    data = []  # para almacenar los datos

    soup_superfinanciera = BeautifulSoup(web_superfinanciera.text, 'html.parser')
    novedades_superfinanciera = soup_superfinanciera.find_all('div', {'id': 'contenidoBloque232'})

    for novedades in novedades_superfinanciera:
        for novedad in novedades:
            if not isinstance(novedad, bs4.element.NavigableString):
                elements = novedad.find_all('a', {'class': 'link-new slider-tooltip'})
                for element in elements:
                    href = "https://www.superfinanciera.gov.co" + element['href']
                    title = element.select_one('.title h4').text
                    intro = element.select_one('.intro p').text.strip().replace('\n', '').replace('\r', '').replace('\t', '')

                    novedadg, created = Novedades.objects.get_or_create(link=href, titulo=title, intro=intro, date=datetime.now())

                    if created:
                        data.append(novedadg)

    print("Actualización de novedades completada.")
    return data


def update_circulares(web_superfinanciera):
    print("Actualizando circulares...")
    print("Obteniendo datos de la web de la Superfinanciera...")
    print("Hora de ejecución:", datetime.now())
    circulares_nuevas = []
    circulares_guardadas = Circulares.objects.all()

    soup_superfinanciera = BeautifulSoup(web_superfinanciera.text, 'html.parser')
    circulares_superfinanciera = soup_superfinanciera.find_all('div', {'id': 'contenidoBloque90820'})
    nuevas_agregadas = 0
    for circular in circulares_superfinanciera:
        elements = circular.find_all('div', {'class': 'col-10 title-circular'})
        for element in elements:
            texto_completo = element.text.strip()
            texto_extraido = texto_completo.split(". ", 2)[1].strip()
            a = element.find('a')
            href = a['href']
            link = "https://www.superfinanciera.gov.co" + str(href)
            titulo = a.text
            print(titulo)
            anexo = element.find('a', {'title': 'Anexo'})
            if anexo is not None:
                anexo = "https://www.superfinanciera.gov.co" + str(anexo['href'])
            circularg, created = Circulares.objects.get_or_create(link=link, titulo= titulo, intro=texto_extraido, anexo=anexo, fecha=datetime.now())
            if created:
                nuevas_agregadas += 1
                circulares_nuevas.append(circularg)
    if nuevas_agregadas > 0:
        print(f"Se han agregado {nuevas_agregadas} nuevas circulares.")
    else:
        print("No se han agregado circulares nuevas.")
    return circulares_nuevas
