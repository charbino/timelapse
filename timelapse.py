# -*- coding:utf-8 -*-
# 
# Author : Marcelo
#
# librairie de timelapse
#
#
#-------------------------------------------------------------------------------
# Bibliothèques
#-------------------------------------------------------------------------------
import time                             #bibliothèque time
import requests
import json
import sqlite3
from datetime import datetime, timedelta, date
import logging
#-------------------------------------------------------------------------------

#database
conn = sqlite3.connect('sunset-sunrise.db')
c = conn.cursor()


#variable global 
dateNowGlobal = datetime.now()
sunriseGlobal =""
sunsetGlobal =""
solarNoonGlobal =""
civilTwilightBeginGlobal = ""
civilTwilightEndGlobal = ""


#Actualise les données avec les données du jour en base de données
def initVariableGLobal():
	logging.debug('Mise à jour des données')
	global dateNowGlobal
	global sunriseGlobal
	global sunsetGlobal
	global solarNoonGlobal
	global civilTwilightBeginGlobal
	global civilTwilightEndGlobal

	#get all data for this day in database
	dateNowGlobal = datetime.now();
	dateNowGlobalFromatted  = date.strftime(dateNowGlobal,"%Y-%m-%d")
	t = (dateNowGlobalFromatted,)
	c.execute('SELECT * FROM sunsetSunrise WHERE date=?', t)
	result = c.fetchone()

	sunriseGlobal = result[1]
	sunsetGlobal = result[2]
	solarNoonGlobal = result[3]
	civilTwilightBeginGlobal = result[4]
	civilTwilightEndGlobal = result[5]

def isWinterHour():
# TODO faire cette function
	return True

def isSun():
	result = False
	global dateNowGlobal
	global sunriseGlobal
	global sunsetGlobal
	global solarNoonGlobal
	global civilTwilightBeginGlobal
	global civilTwilightEndGlobal

	dateNow = datetime.now()

	# si pas la date du jour on actualise les données du jours
	if(date.strftime(dateNow, '%Y-%m-%d') != date.strftime(dateNowGlobal, '%Y-%m-%d')):
		initVariableGLobal();

	sunriseText = sunriseGlobal
	sunsetText = sunsetGlobal

	# print sunriseGlobal
	sunrise = datetime.strptime(sunriseText, '%Y-%m-%dT%H:%M:%S+00:00')
	sunset  = datetime.strptime(sunsetText,'%Y-%m-%dT%H:%M:%S+00:00')
	civilTwilightBegin = dateNow.strptime(civilTwilightBeginGlobal,'%Y-%m-%dT%H:%M:%S+00:00')
	civilTwilightEnd   = dateNow.strptime(civilTwilightEndGlobal,'%Y-%m-%dT%H:%M:%S+00:00')

	#mise a l'heure en fonction heure hiver/été
	if(isWinterHour()):
		addHourUtc = 1
	else:
		addHourUtc = 2

	sunrise = sunrise + timedelta(hours=addHourUtc)
	sunset  = sunset + timedelta(hours=addHourUtc)
	civilTwilightBegin = civilTwilightBegin + timedelta(hours=addHourUtc)
	civilTwilightEnd   = civilTwilightEnd + timedelta(hours=addHourUtc)

	if(dateNow > sunrise and dateNow < sunset):
		result = True
		
	return result

def isTwilight():
	result = False
	global dateNowGlobal
	global sunriseGlobal
	global sunsetGlobal
	global solarNoonGlobal
	global civilTwilightBeginGlobal
	global civilTwilightEndGlobal

	dateNow = datetime.now()

	# si pas la date du jour on actualise les données du jours
	if(date.strftime(dateNow, '%Y-%m-%d') != date.strftime(dateNowGlobal, '%Y-%m-%d')):
		initVariableGLobal();

	sunriseText = sunriseGlobal
	sunsetText = sunsetGlobal

	# print sunriseGlobal
	sunrise = datetime.strptime(sunriseText, '%Y-%m-%dT%H:%M:%S+00:00')
	sunset  = datetime.strptime(sunsetText,'%Y-%m-%dT%H:%M:%S+00:00')
	civilTwilightBegin = dateNow.strptime(civilTwilightBeginGlobal,'%Y-%m-%dT%H:%M:%S+00:00')
	civilTwilightEnd   = dateNow.strptime(civilTwilightEndGlobal,'%Y-%m-%dT%H:%M:%S+00:00')

	#mise a l'heure en fonction heure hiver/été
	if(isWinterHour()):
		addHourUtc = 1
	else:
		addHourUtc = 2

	sunrise = sunrise + timedelta(hours=addHourUtc)
	sunset  = sunset + timedelta(hours=addHourUtc)
	civilTwilightBegin = civilTwilightBegin + timedelta(hours=addHourUtc)
	civilTwilightEnd   = civilTwilightEnd + timedelta(hours=addHourUtc)

	if((dateNow > civilTwilightBegin and dateNow < sunrise) or (dateNow < civilTwilightEnd and dateNow > sunset)):
		result = True
		
	return result
