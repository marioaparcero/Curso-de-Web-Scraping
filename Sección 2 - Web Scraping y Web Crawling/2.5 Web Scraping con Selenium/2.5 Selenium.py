# Instalación de la librería selenium
import sys
!{sys.executable} -m pip install -U selenium

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Scrapper de las estaciones de la red SIAR

print('Iniciando Scraper')
import zipfile
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chromeOptions = webdriver.ChromeOptions()
# Cambiamos la carpeta en la que se descargará el fichero
prefs = {"download.default_directory" : os.getcwd()+"/Resultados Selenium"} 
chromeOptions.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome("chromedriver.exe",options=chromeOptions)
# Web de la que queremos extraer datos
driver.get('http://eportal.mapama.gob.es/websiar/SeleccionParametrosMap.aspx?dst=1')

# Comunidad autonoma
value_ccaa=8
value_ccaa_string = str(value_ccaa)
string_ccaa = 'select[name="ctl00$ContentPlaceHolder1$DropDownListCCAA"] option[value="'+value_ccaa_string+'"]'
desplegable_ccaa = driver.find_element_by_css_selector(string_ccaa)
click_desplegable_ccaa = desplegable_ccaa.click()

time.sleep(2)

# Provincia
value_prov=50
value_prov_string = str(value_prov)
string_prov = 'select[name="ctl00$ContentPlaceHolder1$DropDownListProvincia"] option[value="'+value_prov_string+'"]'
desplegable_prov = driver.find_element_by_css_selector(string_prov)
click_desplegable_prov = desplegable_prov.click()

time.sleep(2)

# Estacion
value_est=2
value_est_string = str(value_est)
string_est = 'select[name="ctl00$ContentPlaceHolder1$DropDownListEstacion"] option[value="'+value_est_string+'"]'
desplegable_est = driver.find_element_by_css_selector(string_est)
click_desplegable_est = desplegable_est.click()

time.sleep(2)

agregar_estacion = driver.find_element_by_css_selector('input[name="ctl00$ContentPlaceHolder1$ButtonAgregar"]')
# Botón para agregar estación climática
click_agregar_estacion=agregar_estacion.click()

time.sleep(0.5)

# Borra la fecha de inicio por defecto
driver.find_element_by_id('txtFechaIni').clear()

time.sleep(0.5)

# Borra la fecha fin por defecto
driver.find_element_by_id('txtFechaFin').clear()

time.sleep(2)

inputElement = driver.find_element_by_id("txtFechaIni")
# Fecha de Inicio
inputElement.send_keys('10/11/2018')

time.sleep(2)

inputElement = driver.find_element_by_id("txtFechaFin")
# Fecha de fin
inputElement.send_keys('15/11/2018')

time.sleep(2)

consultar_datos_button = driver.find_element_by_css_selector('input[name="ctl00$ContentPlaceHolder1$btnConsultar"]')
# Botón de consultar datos
consultar_datos = consultar_datos_button.click()

time.sleep(2)

driver.switch_to.window(driver.window_handles[1])
exportar_csv_link = driver.find_element_by_css_selector('a[id="ContentPlaceHolder1_ExportarCSV"]')
# Botón de exportar csv
descargar_csv = exportar_csv_link.click()

time.sleep(2)

# Cierra el navegador
driver.quit()

# Carga el zip de salida guardado en "Resultados Selenium"
zip_ref = zipfile.ZipFile('Resultados Selenium/InformeDatos.zip', 'r')
# Extrae el fichero csv del zip 
zip_ref.extractall("Resultados Selenium/")
zip_ref.close()
# Borra el archivo 'ImportarDatos.zip'
os.remove('Resultados Selenium/InformeDatos.zip')