#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 11:16:14 2020

@author: y4
"""

from screenshotAndKeypressTests import *
import time
import os
import pyautogui
from fileImporter import *
import json
from tkinter import *
import sys
#pyautogui.mouseinfo.position()

def quitProgram(event=None):
    print("quit")
    os.system('notify-send "quit" "quit"')
    sys.exit()

master = Tk()
master.bind('f6f', quitProgram)

if input("load or create?(l/c) ").lower() == 'l':
    while True:
        file = fillInput("location: ") + input('name: ')+'.json'
        if os.path.isfile(file):
            break
        else:
            print('not a file, try again\n--------------------------\n')
    with open(file,mode='r') as f:
        commands = json.load(f)
    
    while True:
        try:
            times = int(input("how many times to run? "))
        except:
            print("not a number try again")
        else:
            break
    print("starting in 5 seconds")
    time.sleep(5)
    for x in range(times):
        for x in commands:
            time.sleep(0.01)
            if x[0] == 'click':
                mouseClick(x[2],x[1])
            elif x[0] == 'str':
                keypress(bytes("str "+x[1]+" ","utf-8"))
            elif x[0] == 'custom':
                keypress(bytes(x+" ",'utf-8'))
            elif x[0] == 'scroll':
                if int(x[1]) > 0:
                    button = 4
                else:
                    button = 5
                for _ in range(abs(int(x[1]))):
                    mouseClick(button)
            elif x[0] == 'wait':
                time.sleep(float(x[1]))


else:
    data = []
    while True:
        typeChoice = input('what type to add?(sc-scroll,cu-custom,s-string,c-click,w-wait seconds)')
        if typeChoice.lower() == 'cu':
            data.append(["custome",input('custom xte input: ')])
        elif typeChoice.lower() == 'c':
            button = input('what button?(no responce will be 1) ')
            if button == "":
                button = 1
            else:
                button=int(button)
            print('in 3 seconds will record mouse pos')
            time.sleep(5)
            
            dat = ['click',list(pyautogui.mouseinfo.position()),button]
            print("position: ",tuple(dat[1]))
            if input('add?(y/n) ').lower() == 'y':
                data.append(dat)
        elif typeChoice.lower() == "s":
            string = input('what to write? ')
            if input('add?(y/n) ').lower() == 'y':
                data.append(["str",string])
        elif typeChoice.lower() == 'sc':
            while True:
                dat = input("how much to scroll?(positive up negative down) ")
                try:
                    int(dat)
                except:
                    print("not number")
                else:
                    break
            if input('add?(y/n) ').lower() == 'y':
                data.append(["scroll",dat])
        elif typeChoice.lower() == 'w':
            while True:
                dat = input("how many seconds to wait?(decimal works) ")
                try:
                    float(dat)
                except:
                    print("not number")
                else:
                    break
            if input('add?(y/n) ').lower() == 'y':
                data.append(["wait",dat])
        if input("more?(no responce will continue and n will finish) ").lower() == 'n':
            break
    
    print("save\n--------------")
    while True:
        location = fillInput("location: ")
        if os.path.isdir(location):
            break
        else:
            print('not a folder, try again\n--------------------------\n')
    name = input('name: ')+'.json'
    with open(location+name,mode='w')as f:
        f.write(json.dumps(data))


print("done")
os.system('notify-send "done" "done"')