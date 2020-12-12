#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 16:38:04 2020

@author: y3
"""

#4 3

from screenshotAndKeypressTests import *
import time
import os

y = int(input("how many times to submit? "))
print("be in english")
time.sleep(5)


for _ in range(y):
    
    mouseClick(1,(695,473))
    
    time.sleep(0.3)
    mouseClick(1,(695,705))
    time.sleep(0.2)
    keypress(bytes("str כתבתי תוכנה שתלחץ שוב ושוב ושוב  ","utf-8"))
    
    time.sleep(0.3)
    mouseClick(1,(695,771))
    time.sleep(1)
    #again
    mouseClick(1,(745,440))
    time.sleep(1)
    

os.system('notify-send "done" "done"')