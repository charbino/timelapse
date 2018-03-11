# -*- coding:utf-8 -*-
# Author : Marcelo
# Permet de prendre en photo du lever du soleil au couché
#
#
#-------------------------------------------------------------------------------
# Bibliothèques
#-------------------------------------------------------------------------------
import time                             #bibliothèque time
import picamera
import logging
import timelapse
from datetime import datetime, timedelta, date
import os
#-------------------------------------------------------------------------------

if __name__ == '__main__':

	#logging
	logging.basicConfig(filename='log/weather.log',level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

	#Photo
	camera = picamera.PiCamera()
	camera.resolution = (1024, 768)
	timeBetweenPhoto  = 60			  # en seconde
	withTwilight = True


	timelapse.initVariableGLobal();
	while True:
		while timelapse.isSun(withTwilight):
			#logging.debug('Je prend en photo')

			dateNowGlobal = datetime.now();
			dateOfDay = date.strftime(dateNowGlobal,"%Y-%m-%d")
			dateNowGlobalFromatted  = date.strftime(dateNowGlobal,"%Y-%m-%dT%H:%M:%S")

			path = 'photos/weather/{}'.format(dateOfDay)
			if(not os.path.exists(path)):
				os.makedirs(path)

			camera.capture('{}/image{}.jpg'.format(path,dateNowGlobalFromatted))
			logging.debug('{}/image{}.jpg'.format(path,dateNowGlobalFromatted))

			time.sleep(timeBetweenPhoto)

