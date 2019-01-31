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
import os
#-------------------------------------------------------------------------------

if __name__ == '__main__':

	#logging
	logging.basicConfig(filename='log/champignon.log',level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

	#Photo
	camera = picamera.PiCamera()
	camera.resolution = (1024, 768)
	timeBetweenPhoto  = 5			  # en seconde


	timelapse.initVariableGLobal();
	while True:
		while timelapse.isSun():
			#logging.debug('Je prend en photo')

			dateNowGlobal = datetime.now();
			dateOfDay = date.strftime(dateNowGlobal,"%Y-%m-%d")
			dateNowGlobalFromatted  = date.strftime(dateNowGlobal,"%Y-%m-%dT%H:%M:%S")

			path = 'photos/champignon/{}'.format(dateOfDay)
			if(not os.path.exists(path)):
				os.makedirs(path)

			camera.capture('{}/image{}.jpg'.format(path,dateNowGlobalFromatted))
			logging.debug('{}/image{}.jpg'.format(path,dateNowGlobalFromatted))

			time.sleep(timeBetweenPhoto)

