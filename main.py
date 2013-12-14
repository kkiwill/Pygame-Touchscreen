#!/usr/bin/python
# -*- coding: utf8 -*-
# Kiwil 13/12/13
# http://kiwilgk.blogspot.fr/

import pygame, sys, os, time, urllib, lib, glob, re, datetime, RPi.GPIO as GPIO
from pygame.locals import *
from lib import *
from subprocess import call

lib.touchscreen()
pygame.init()

def screenMain():
  # set up the window
  screen=lib.setupwindow()

  # Fill background
  background = pygame.Surface(screen.get_size())
  background = background.convert()
  background.fill(WHITE)

  bx2 = pygame.draw.rect(background,  YELLOW, (0, 80, 320, 80))
  bxin2= pygame.draw.rect(background, WHITE, (5,85,310,70))
  bx3 = pygame.draw.rect(background, RED, (0, 0, 320, 80))
  bxin3 = pygame.draw.rect(background, WHITE, (5, 5, 310, 70))
  bx4 = pygame.draw.rect(background, BLUE, (0, 160, 320, 80))
  bxin4 = pygame.draw.rect(background, WHITE, (5, 165, 310, 70))

  # Display some text
  font = pygame.font.Font(None, 36)
  txt = font.render("Systeme", 2, (BLACK))
  txt1 = font.render("GPIO", 2, (BLACK))
  txt2 = font.render("Camera",2, (BLACK))

  #text = pygame.transform.rotate(text,270)
  txtpos = txt.get_rect(center=(160,40))
  txtpos2= txt1.get_rect(center=(160,120))
  txtpos3= txt2.get_rect(center=(160,200))
  
  background.blit(txt, txtpos)
  background.blit(txt1, txtpos2)
  background.blit(txt2, txtpos3)
  screen.blit(background, (0, 0))
  pygame.display.flip()

  running = True

  # run the game loop
  while running:
      for event in pygame.event.get():
          if event.type == QUIT:
              pygame.quit()
              sys.exit()
              running = False
          elif event.type == pygame.MOUSEBUTTONDOWN:
              if bxin2.collidepoint(pygame.mouse.get_pos()):
                 screenGPIO()
              if bxin3.collidepoint(pygame.mouse.get_pos()):
                 screenSYS()
              if bxin4.collidepoint(pygame.mouse.get_pos()):
                 screenCamera()
      pygame.display.update()

def screenGPIO():
  # set up the window
  screen=lib.setupwindow()

  # Fill background
  background = pygame.Surface(screen.get_size())
  background = background.convert()
  background.fill(WHITE)

  # Set up forms
  box1 = pygame.draw.rect(background, YELLOW,(0, 0, 80, 80))
  box2 = pygame.draw.rect(background, BLACK,(80, 0, 80, 80))
  box3 = pygame.draw.rect(background,  BLUE, (160, 0, 80, 80))
  box4 = pygame.draw.rect(background, GREEN, (240, 0, 80, 80))
  box5 = pygame.draw.rect(background, MAGENTA,(0, 80, 80, 80))
#  box6 = pygame.draw.rect(background, RED,(80, 80, 80, 80))
#  box7 = pygame.draw.rect(background,  CYAN, (160, 80, 80, 80))
#  box8 = pygame.draw.rect(background, BLACK, (240, 80, 80, 80))

#  box9 = pygame.draw.rect(background, GREEN,(80, 160, 80, 80))
#  box10 = pygame.draw.rect(background,  BLUE, (160, 160, 80, 80))
#  box11 = pygame.draw.rect(background, CYAN, (240, 160, 80, 80))

  cir  = pygame.draw.circle(background, BLACK, (22, 219), 20)

  # Display some text
  font = pygame.font.Font(None, 20)
  GPIO24 = font.render("GPIO 24", 1, (BLACK))
  GPIO23 = font.render("GPIO 23", 1, (RED))
  GPIO22 = font.render("GPIO 22",1, (YELLOW))
  GPIO21 = font.render("GPIO 21",1, (BLACK))
  GPIO4 = font.render("GPIO 4",1, (BLACK))
#  GPIO21 = font.render("GPIO 21",1,(YELLOW))
#  GPIO10 = font.render("GPIO 10",1,(BLACK))
#  GPIO9 = font.render("GPIO 9 ",1,(BLACK))
#  GPIO11  = font.render("GPIO 11",1,(BLACK))
#  GPIO0  = font.render("GPIO 0",1,(BLACK))
#  GPIO1  = font.render("GPIO 1",1,(BLACK))
  text3 = font.render("<<",1, (YELLOW))

  #text = pygame.transform.rotate(text,270)
  textpos = GPIO24.get_rect(center=(40,40))
  textpos2= GPIO23.get_rect(center=(120,40))
  textpos5= GPIO22.get_rect(center=(200,40))
  textpos6= GPIO21.get_rect(center=(280,40))
  
  textpos3= GPIO4.get_rect(center=(40,120))
 #textpos7= GPIO21.get_rect(center=(120,120))
  #textpos8= GPIO10.get_rect(center=(200,120))
  #textpos9= GPIO9.get_rect(center=(280,120))
  
 # textpos10= GPIO11.get_rect(center=(40,200))
 # textpos11= GPIO0.get_rect(center=(120,200))
 # textpos12= GPIO1.get_rect(center=(200,200))
  
  textpos4= text3.get_rect(center=(21,215))

  background.blit(GPIO24, textpos)
  background.blit(GPIO23, textpos2)
  background.blit(GPIO22, textpos5)
  background.blit(GPIO21, textpos6)
  background.blit(GPIO4, textpos3)
 # background.blit(GPIO21,textpos7)
 # background.blit(GPIO10,textpos8)
 # background.blit(GPIO9,textpos9)
 # background.blit(GPIO11,textpos10)
 # background.blit(GPIO0,textpos11)
 # background.blit(GPIO1,textpos12)
  
  background.blit(text3, textpos4)
  screen.blit(background, (0, 0))
  pygame.display.flip()

  running = True

  #State of GPIO
  state18=0
  state16=0
  state15=0
  state13=0
  
  state7=0
  state13=0
  state19=0
  state21=0
  
  state23=0
  state3=0
  state5=0
  
  # run the game loop
  while running:
      for event in pygame.event.get():
          if event.type == QUIT:
              pygame.quit()
              sys.exit()
              running = False
              
          elif event.type == pygame.MOUSEBUTTONDOWN:
              
              # 4 top buttons
              if box1.collidepoint(pygame.mouse.get_pos()):
                 state18=lib.SRGPIO(state18,18)
              if box2.collidepoint(pygame.mouse.get_pos()):
                 state16=lib.SRGPIO(state16,16)
              if box3.collidepoint(pygame.mouse.get_pos()):
                 state15=lib.SRGPIO(state15,15)
              if box4.collidepoint(pygame.mouse.get_pos()):
                 state13=lib.SRGPIO(state13,13)
                 
#               # 4 middle buttons
              if box5.collidepoint(pygame.mouse.get_pos()):
                 state7=lib.SRGPIO(state7,7)
#              if box21.collidepoint(pygame.mouse.get_pos()):
#                 state13=lib.SRGPIO(state13,13)
#              if box2.collidepoint(pygame.mouse.get_pos()):
#                 state21=lib.SRGPIO(state21,21)
#              if box5.collidepoint(pygame.mouse.get_pos()):
#                 state19=lib.SRGPIO(state19,19)
#              
#              # 4 bottom button
#              if box4.collidepoint(pygame.mouse.get_pos()):
#                 state23=lib.SRGPIO(state23,23)
#              if box6.collidepoint(pygame.mouse.get_pos()):
#                 state3=lib.SRGPIO(state3,3)
#              if box9.collidepoint(pygame.mouse.get_pos()):
#                 state5=lib.SRGPIO(state5,5)
              
              # back to screenMain
              if cir.collidepoint(pygame.mouse.get_pos()):
                 lib.reset(18,16)
                 screenMain()
                 
          elif event.type == KEYDOWN and event.key == K_ESCAPE:
               running = False
      pygame.display.update()

def screenSYS():
  # set up the window
  screen=lib.setupwindow()

  #Variable Sys
  date= time.strftime("%d %b %Y")
  t = os.popen("/opt/vc/bin/vcgencmd measure_temp")
  temp= t.read()
  
  page = urllib.urlopen("http://www.monip.org/").read()
  ip = page.split("IP : ")[1].split("<br>")[0]
  
  # set up background
  background = pygame.Surface(screen.get_size())
  background = background.convert()
  background.fill(WHITE)

  # Set up forms
  bx3 = pygame.draw.rect(background, BLUE, (100, 0, 120, 30))
  cir = pygame.draw.circle(background, BLACK, (21, 219), 20)

  # Display some text
  font36 = pygame.font.Font(None, 36)
  font25 = pygame.font.Font(None, 25)
  txt = font36.render("Systeme", 12, (BLACK))
  txt1 = font36.render("<<", 1, (YELLOW))
  txtdate = font25.render(date,1, (BLACK))
  txttemp = font25.render(temp,1, (BLACK))
  txtIP = font25.render(ip,1, (BLACK))

  #text = pygame.transform.rotate(text,270)
  txtpos = txt.get_rect(center=(160,12))
  txtpos2= txt1.get_rect(center=(20,215))
  datepos= txtdate.get_rect(center=(270,230))
  temppos= txttemp.get_rect(center=(276,200))
  ippos = txtIP.get_rect(center=(160,120))

  background.blit(txttemp, temppos)
  background.blit(txtdate, datepos)
  background.blit(txtIP, ippos)
  background.blit(txt, txtpos)
  background.blit(txt1, txtpos2)
  screen.blit(background, (0, 0))
  pygame.display.flip()

  running = True

  # run the game loop
  while running:
      for event in pygame.event.get():          
          if event.type == QUIT:
              pygame.quit()
              sys.exit()
              running = False
          elif event.type == pygame.MOUSEBUTTONDOWN:
               if cir.collidepoint(pygame.mouse.get_pos()):
                  screenMain()
      pygame.display.update()
      
def screenCamera():
# From akeric.com: http://www.akeric.com/blog/?p=632
  def saveImage():
      """
      Save the current image to the working directory of the program.
      """
      currentImages = glob.glob("/home/pi/cam-interface/pics/*.jpg")
      numList = [0]
      for img in currentImages:
          i = os.path.splitext(img)[0]
          try:
              num = re.findall('[0-9]+$', i)[0]
              numList.append(int(num))
          except IndexError:
              pass
      numList = sorted(numList)
      newNum = numList[-1]+1
      saveName = 'Pi-Cam-%05d.jpg' % newNum
      return saveName
# End from akeric.com

  def main():
      pygame.init()
      screen = pygame.display.set_mode((320, 240))
      clock = pygame.time.Clock()

## Button example code additions
      pygame.mouse.set_visible(1)
      background = pygame.Surface(screen.get_size())
      background = background.convert()
      background.fill((250,250,250))
      screen.blit(background, (0,0))
      pygame.display.flip()

      button_quit = pygame.image.load('/home/pi/cam-interface/Pi-Quit1.png').convert_alpha()
      button_pic = pygame.image.load('/home/pi/cam-interface/Pi-camera1.png').convert_alpha()
      button_clear = pygame.image.load('/home/pi/cam-interface/Pi-Clear1.png').convert_alpha()
      button_off = pygame.image.load('/home/pi/cam-interface/Pi-Off1.png').convert_alpha()
      b_quit = screen.blit(button_quit,(270,190))
      b_cam = screen.blit(button_pic,(1,1))
      b_clear = screen.blit(button_clear,(220,190))
      b_off = screen.blit(button_off,(1,190))
      pygame.display.flip()

## end button additional code    
      radius = 3
      x = 0
      y = 0
      mode = 'blue'
      points = []

### I need to remove some of this code to stop it still producing the mouse trails, but removing the forced update at the end it no longer draws them on screen.
      while True:
        
          pressed = pygame.key.get_pressed()
        
          alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
          ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
          for event in pygame.event.get():
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used 
              if event.type == pygame.QUIT:
                  return
              if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_w and ctrl_held:
                      return
                  if event.key == pygame.K_F4 and alt_held:
                      return
                  if event.key == pygame.K_ESCAPE:
                      return
            
                # determine if a letter key was pressed 
                  if event.key == pygame.K_r:
                      mode = 'red'
                  elif event.key == pygame.K_g:
                      mode = 'green'
                  elif event.key == pygame.K_b:
                      mode = 'blue'
            
              if event.type == pygame.MOUSEBUTTONDOWN:
                  if event.button == 1: # left click grows radius 
                     # radius = min(200, radius + 1)
                      pos = pygame.mouse.get_pos()
                      if b_cam.collidepoint(pos):
                          background.fill((250,250,250))
                          screen.blit(background, (0,0))
                          button_takingpic = pygame.image.load('/home/pi/cam-interface/Pi-aperature1.png').convert_alpha()
                          b_takingpic = screen.blit(button_takingpic,(120,100))
                          pygame.display.flip()
                          time.sleep(0.1)
                        
                          background.fill((250,250,250))
                          screen.blit(background, (0,0))
                          button_takingpic = pygame.image.load('/home/pi/cam-interface/Pi-aperature2.png').convert_alpha()
                          b_takingpic = screen.blit(button_takingpic,(120,100))
                          pygame.display.flip()
                          time.sleep(0.1)               


                          background.fill((250,250,250))
                          screen.blit(background, (0,0))                        
                          button_takingpic = pygame.image.load('/home/pi/cam-interface/Pi-aperature3.png').convert_alpha()
                          b_takingpic = screen.blit(button_takingpic,(120,100))                      
                          pygame.display.flip()
                          time.sleep(0.1)                        
                        
                        
                          background.fill((250,250,250))
                          screen.blit(background, (0,0))
                          button_takingpic = pygame.image.load('/home/pi/cam-interface/Pi-aperature4.png').convert_alpha()
                          b_takingpic = screen.blit(button_takingpic,(120,100))                   
                          pygame.display.flip()
                          time.sleep(0.1)               
                        

                          background.fill((250,250,250))
                          screen.blit(background, (0,0))
                          button_takingpic = pygame.image.load('/home/pi/cam-interface/Pi-aperature5.png').convert_alpha()
                          b_takingpic = screen.blit(button_takingpic,(120,100))
                          pygame.display.flip()
                          time.sleep(0.1)
                        
                        
                          background.fill((250,250,250))
                          screen.blit(background, (0,0))
                          button_takingpic = pygame.image.load('/home/pi/cam-interface/Pi-aperature6.png').convert_alpha()
                          b_takingpic = screen.blit(button_takingpic,(120,100))
                          pygame.display.flip()
                          time.sleep(0.1)
                        
                        
                          background.fill((250,250,250))
                          screen.blit(background, (0,0))
                          button_takingpic = pygame.image.load('/home/pi/cam-interface/Pi-aperature7.png').convert_alpha()
                          b_takingpic = screen.blit(button_takingpic,(120,100))
                          pygame.display.flip()

                          start_time = time.time()

                          filename = "/home/pi/cam-interface/pics/" + saveImage()
                          argument="raspistill -t 200 -n -o " + filename
                          call ([argument], shell=True)
                          time.sleep(0.1)
                          if (filename[-3:] == "JPG") or (filename[-3:] == "jpg") :
                              surf = pygame.image.load(filename)
                              next_time = time.time()
                              picture = pygame.transform.scale(surf, (320, 240))
                              screen.blit(picture,(0,0))
### Poor, this really needs to be moved to proper OOP, just didn't have the time, easier to just copy and paste :-( JPOD.
                              button_quit = pygame.image.load('/home/pi/cam-interface/Pi-Quit1.png').convert_alpha()
                              button_pic = pygame.image.load('/home/pi/cam-interface/Pi-camera1.png').convert_alpha()
                              button_clear = pygame.image.load('/home/pi/cam-interface/Pi-Clear1.png').convert_alpha()
                              button_off = pygame.image.load('/home/pi/cam-interface/Pi-Off1.png').convert_alpha()
                              b_quit = screen.blit(button_quit,(270,190))
                              b_cam = screen.blit(button_pic,(1,1))
                              b_clear = screen.blit(button_clear,(220,190))
                              b_off = screen.blit(button_off,(1,190))
                              pygame.display.flip()			   	
                      elif b_quit.collidepoint(pos):
                              screenMain()
                      elif b_clear.collidepoint(pos):
                              background.fill((250,250,250))
                              screen.blit(background, (0,0))
                              pygame.display.flip()
### Poor, this really needs to be moved to proper OOP, just didn't have the time, easier to just copy and paste :-( JPOD.
                              button_quit = pygame.image.load('/home/pi/cam-interface/Pi-Quit1.png').convert_alpha()
                              button_pic = pygame.image.load('/home/pi/cam-interface/Pi-camera1.png').convert_alpha()
                              button_clear = pygame.image.load('/home/pi/cam-interface/Pi-Clear1.png').convert_alpha()
                              button_off = pygame.image.load('/home/pi/cam-interface/Pi-Off1.png').convert_alpha()
                              b_quit = screen.blit(button_quit,(270,190))
                              b_cam = screen.blit(button_pic,(1,1))
                              b_clear = screen.blit(button_clear,(220,190))
                              b_off = screen.blit(button_off,(1,190))
                              pygame.display.flip()
                      elif b_off.collidepoint(pos):
                              screenMain()
### Old code that I should find time to remove and check it doesn't break anything.
                      elif event.button == 3: # right click shrinks radius
                              radius = max(1, radius - 1)
            
              if event.type == pygame.MOUSEMOTION:
                # if mouse moved, add point to list 
                  position = event.pos
                  points = points + [position]
		# this next line use the last x values (work this out - JPOD)
                  points = points[-100:]
                
          screen.fill((0, 0, 0))
        
        # draw all points 
          i = 0
          while i < len(points) - 1:
              drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
              i += 1
        
##        pygame.display.flip()
## Removed these to stop the mouse trails update.        
##        clock.tick(60)

  def drawLineBetween(screen, index, start, end, width, color_mode):
      c1 = max(0, min(255, 2 * index - 256))
      c2 = max(0, min(255, 2 * index))
    
      if color_mode == 'blue':
          color = (c1, c1, c2)
      elif color_mode == 'red':
          color = (c2, c1, c1)
      elif color_mode == 'green':
          color = (c1, c2, c1)
    
      dx = start[0] - end[0]
      dy = start[1] - end[1]
      iterations = max(abs(dx), abs(dy))
    
      for i in xrange(iterations):
          progress = 1.0 * i / iterations
          aprogress = 1 - progress
          x = aprogress * start[0] + progress * end[0]
          y = aprogress * start[1] + progress * end[1]
          pygame.draw.circle(screen, color, (int(x), int(y)), width)

  main()


screenMain()
