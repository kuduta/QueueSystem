#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 18:35:06 2019

@author: nexpose
"""




import pygame
import time
import sys



def playsound(num):
    pygame.init()
    #pygame.mixer.music.load("sounds/"+ str(num)+".mp3")
    pygame.mixer.music.load("sound/"+ str(num)+".wav")
    pygame.mixer.music.play()
    time.sleep(1.1)
    

#playsound(8)
    
input = '765645'


#seconds = int(input('How many seconds to wait ? '))


#for i in range(seconds):
    #print (str(seconds  - i )+ ' seconds remain' )
#    print (str(i+1 )+ ' seconds remain' )
#    time.sleep(1)
print ('Argument List:', str(sys.argv[1]))

input=str(sys.argv[1])
#x = list(input)
x = list(input)
f = 'invit'
a = 'atport1'
e = 'end'
playsound(f)
time.sleep(0.3)


for i in x:
    playsound(i)
    
playsound(a)
playsound(3)
playsound(e)


    
    