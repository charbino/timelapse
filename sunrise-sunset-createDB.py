# -*- coding:utf-8 -*-
# 
# permet de créer la base de donnée et remplir les données via l'api
#
# https://api.sunrise-sunset.org/json?lat=45.668228&lng=6.366371&formatted=0
# API : https://sunrise-sunset.org/api
#
#-------------------------------------------------------------------------------
# Bibliothèques
#-------------------------------------------------------------------------------	

import sqlite3
from datetime import timedelta, date, datetime, timedelta
import requests
import json


#-------------------------------------------------------------------------------


# Create database and table
conn = sqlite3.connect('sunset-sunrise.db')
c = conn.cursor()
c.execute('''CREATE TABLE sunsetSunrise (date text, sunrise text, sunset text, solar_noon text, civil_twilight_begin text, civil_twilight_end text)''')
conn.commit()

#coordonnée
latitudeAlbertville = 45.668228
longitudeAlbertville = 6.366371
formatted = 0

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2019, 1, 1)
end_date = date(2019, 12, 31)
for singledate in daterange(start_date, end_date):
	print date.strftime(singledate,"%Y-%m-%d")
	dateApi = date.strftime(singledate,"%Y-%m-%d")
	url = 'https://api.sunrise-sunset.org/json?lat={}&lng={}&formatted={}&date={}'.format(latitudeAlbertville,longitudeAlbertville,formatted,dateApi)
	responseJson = requests.post(url).json()
	dateNow = datetime.now()

	if(responseJson['status']=='OK'):
		sunriseText = responseJson['results']['sunrise']
		sunsetText = responseJson['results']['sunset']
		solarNoonText = responseJson['results']['solar_noon']
		civilTwilightBeginText = responseJson['results']['civil_twilight_begin']
		civilTwilightEndText = responseJson['results']['civil_twilight_end']

		arguments = (dateApi, sunriseText, sunsetText, solarNoonText, civilTwilightBeginText,civilTwilightEndText)
		c.execute("INSERT INTO sunsetSunrise VALUES (?,?,?,?,?,?)",arguments)
		conn.commit()
conn.close()
