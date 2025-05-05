import urllib.request, json
import sys

print("Elige uno de estos 3 Lugares: ")
print("1. Barcelona")
print("2. Madrid")
print("3. Palencia")
respuesta = int(input("Tu respuesta es: "))

if (respuesta == 1):
	url_tiempo = "https://api.open-meteo.com/v1/forecast?latitude=41.38879&longitude=2.15899&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
	ciudad = "Barcelona"
elif (respuesta == 2):
	url_tiempo = "https://api.open-meteo.com/v1/forecast?latitude=40.4165&longitude=-3.70256&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
	ciudad = "Madrid"
elif (respuesta == 3):
	url_tiempo = "https://api.open-meteo.com/v1/forecast?latitude=42.00955&longitude=-4.52406&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
	ciudad = "Palencia"
else:
	print("Respuesta invalida")
	sys.exit()

with urllib.request.urlopen(url_tiempo) as datos:
	parseado = json.load(datos)

	print("Temperatura en " + ciudad + ": ", parseado["current"]["temperature_2m"])
	print("Velocidad del viento en " + ciudad + ": ", parseado["current"]["wind_speed_10m"])
	print("Humedad relativa en " + ciudad + ": ", parseado["hourly"]["relative_humidity_2m"][0])
