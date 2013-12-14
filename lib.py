#!/usr/bin/python
# -*- coding: utf8 -*-
# Kiwil 10/12/13
# http://kiwilgk.blogspot.fr/

import pygame,sys,os,RPi.GPIO as GPIO

# color :
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
CYAN  = (  0, 255, 255)
MAGENTA=(255,   0, 255)
YELLOW =(255, 255,   0)

#Function
def  touchscreen():
	from evdev import InputDevice, list_devices
	devices = map(InputDevice, list_devices())
	eventX=""
	for dev in devices:
		if dev.name == "ADS7846 Touchscreen":
			eventX = dev.fn
			os.environ["SDL_FBDEV"] = "/dev/fb1"
			os.environ["SDL_MOUSEDRV"] = "TSLIB"
			os.environ["SDL_MOUSEDEV"] = eventX

#Set/Reset GPIO
def SRGPIO(state,GP):
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(GP, GPIO.OUT)

	if (state==0):
		GPIO.output(GP,GPIO.HIGH)
		return 1
	else:
		GPIO.output(GP,GPIO.LOW)
		return 0

#Reset GPIO
def reset(gp1,gp2):
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(gp1, GPIO.OUT)
	GPIO.setup(gp2, GPIO.OUT)
	GPIO.output(gp1, GPIO.LOW)
	GPIO.output(gp2, GPIO.LOW)

#Setup a windows for touchscreen
def setupwindow():
	screen = pygame.display.set_mode((320, 240), 0, 32)
	pygame.display.set_caption('Drawing')
	return screen
  

