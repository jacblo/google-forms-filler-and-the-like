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
    
    
    #change language
    keypress(keymap("Alt_L+Shift_L"))
    
    #name
    mouseClick(1,(729,518))
    keypress(bytes("str "+x,"utf-8"))
    
    #last name
    mouseClick(1,(729,675))
    keypress(bytes("str "+x,"utf-8"))
    
    #username
    mouseClick(1,(729,813))
    keypress(bytes("str "+x,"utf-8"))
    
    #next
    mouseClick(1,(683,891))
    time.sleep(3)
    
    
    #do you sell armour?
    mouseClick(1,(693,497))
    
    #what enchants
    mouseClick(1,(798,683))
    keypress(bytes("str "+x,"utf-8"))
    
    #next
    mouseClick(1,(798,763))
    time.sleep(3)
    
    
    #sell elytra
    mouseClick(1,(693,419))
    
    #enchnts
    mouseClick(1,(732,626))
    keypress(bytes("str "+x,"utf-8"))
    
    #next
    mouseClick(1,(795,707))
    time.sleep(3)
    
    #sword and pickaxe
    mouseClick(1,(692,358))
    
    #with enchants?
    mouseClick(1,(693,535))
    
    #what enchants?
    mouseClick(1,(693,722))
    keypress(bytes("str "+x,"utf-8"))
    
    #money
    mouseClick(1,(693,868))
    keypress(bytes("str "+x,"utf-8"))
    
    #next
    mouseClick(1,(781,955))
    time.sleep(3)
    
    #scroll
    for __ in range(15):
        mouseClick(5,(781,989))
    for __ in range(3):
        mouseClick(4,(781,989))
        time.sleep(0.2)
    time.sleep(1)
    
    #sell enchants?
    mouseClick(1,(690,117))
    #
    #which out of 14
    
    for w in range(299,820,36):
        mouseClick(1,(781,w))
        time.sleep(0.2)
    mouseClick(1,(845,802))
    keypress(bytes("str "+x,"utf-8"))
    
    #money
    mouseClick(1,(736,968))
    keypress(bytes("str "+x,"utf-8"))
    
    #next
    mouseClick(1,(792,1040))
    time.sleep(3)
    
    #comment
    mouseClick(1,(709,355))
    keypress(bytes("str "+x,"utf-8"))
    
    #submit
    mouseClick(1,(830,423))
    time.sleep(3)
    
    #again
    mouseClick(1,(745,264))
    time.sleep(3)
    
    #change language
    keypress(keymap("Alt_L+Shift_L"))
    
os.system('notify-send "done" "done"')