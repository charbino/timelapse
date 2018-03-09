# -*- coding:utf-8 -*-
# 
# Author : Marcelo
#
# Permet de prendre en photo les couchés et levé de soleil
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
	#Photo
	#camera = picamera.PiCamera()
	#camera.resolution = (1024, 768)
	timeBetweenPhoto  = 60			  # en seconde


	timelapse.initVariableGLobal();
	while True:
		i=0
		while timelapse.isTwilight():
			logging.debug('Je prend en photo')
			# camera.capture('photos/image{0:07d}.jpg'.format(i))
			# print('photos/image{0:07d}.jpg'.format(i))
			# i +=1
			time.sleep(timeBetweenPhoto)

