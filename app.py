# se importa las librerias a usar en el proyecto

import requests 
import configparser

# habilita las capacidades de servidor.
# es la libreria encargada de gestionar la renderizacion 
# de las vistas

from  flask import Flask, render_template, request

# el objeto principal de la aplicacion se llama app

app = Flask(__name__)

#  Inciamos con la logica de la aplicacion.

# se gestiona la ruta inicial de la aplicacion


# Ruta Principal
@app.route ('/')
# aqui va el nombre de la funcion o metodo que gestiona la ruta
def weather_dashboard():
    return render_template ('home.html')


# Ruta que pinta los resultados    
@app.route ('/results', methods=['POST'])
def render_resultados 
    
    # para poder mostrar los resultados, antes debo saber cual es la ciudad
    # que digito en el formulario

    cityname= request.form['cityname']

    # es pasarle el valor de la ciudad que el usuario digito al api
    # pero antes de consumir el api 
   
    # esta variable esta almacenando el valor del api key
    # que se encuentra en el archivo config.ini 
    api =  get_api_key(); 

    # vamos a conectarnos al api y consumirlo

    data = get_weather_results(cityname, api)

#se toma lña temperatura del json
    temp = "{0:.2f}".format (data['main']['temp'])

    #se toma la temperatura termica

    feels_like = "{0:.2f}".format(data['main']['feels_like'])

    #La condicion de temperatura

    weather = data ["wather"][0]['main']

    location = data ['name']

return render_template ('results.html', location=location, temp=temp, feels_like= feels_like, weather=weather)


# aqui se consumio el servicio web 

def  get_weather_results (cityname, api_key)

    url =  "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(cityname,api_key)
 
    r = request.get(url)
    return r.json
 
 








def get_api_key():
    # esta funcion obtiene el valor del api key que 
    # se va a utilizar para consumir el servicio web

    # se lee el archivo que guarda la api key del servicio web
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config ['openweathermap'] ['api']