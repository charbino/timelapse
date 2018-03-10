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
		i=0
		while timelapse.isSun():
			logging.debug('Je prend en photo')
			# camera.capture('photos/image{0:07d}.jpg'.format(i))
			# print('photos/image{0:07d}.jpg'.format(i))
			# i +=1
			time.sleep(timeBetweenPhoto)

