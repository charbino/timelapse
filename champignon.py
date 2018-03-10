# -*- coding:utf-8 -*-
# Author : Marcelo
# Permet de prendre en photo quand il fait jour 
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
#-------------------------------------------------------------------------------

if __name__ == '__main__':

	#logging
	logging.basicConfig(filename='log/champignon.log',level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

	#Photo
	camera = picamera.PiCamera()
	camera.resolution = (1024, 768)
	timeBetweenPhoto  = 60			  # en seconde


	timelapse.initVariableGLobal();
	while True:
		while timelapse.isSun():
			#logging.debug('Je prend en photo')

			dateNowGlobal = datetime.now();
			dateNowGlobalFromatted  = date.strftime(dateNowGlobal,"%Y-%m-%dT%H:%M:%S")

			camera.capture('photos/champignon/image{}.jpg'.format(dateNowGlobalFromatted))
			logging.debug('photos/champignon/image{}.jpg'.format(dateNowGlobalFromatted))

			time.sleep(timeBetweenPhoto)

