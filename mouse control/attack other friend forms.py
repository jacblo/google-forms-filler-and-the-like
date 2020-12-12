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

x = input("what to write: ") + " "
y = int(input("how many times to submit? "))
print("be in english")
time.sleep(5)


for _ in range(y):
    
    #email
    mouseClick(1,(686,684))
    keypress(bytes("str "+x+" ","utf-8"))

    
    #name
    mouseClick(1,(686,830))
    keypress(bytes("str "+x+" ","utf-8"))
    
    #scroll
    for __ in range(15):
        mouseClick(5,(781,989))
        time.sleep(0.02)
    time.sleep(0.1)
    
    mouseClick(1,(686,660))
    
    mouseClick(1,(686,813))
    keypress(bytes("str "+x+" ","utf-8"))
    
    #submit
    mouseClick(1,(690,880))
    time.sleep(1)
    
    #again
    mouseClick(1,(428,50))
    keypress(bytes("str https://www.google.com/url?q=https://docs.google.com/forms/d/e/1FAIpQLScuo2w8Q15rOKBoiM4aGdXbmGrfIGhsi6q3fy_SIqzjCWYIQQ/viewform?usp%3Dsf_link&sa=D&source=hangouts&ust=1606207854010000&usg=AFQjCNH3-Plnn6LH8D_TE8bO1arsCeMm3w ","utf-8"))
    keypress(b'key Return ')
    time.sleep(2)
    
    
os.system('notify-send "done" "done"')