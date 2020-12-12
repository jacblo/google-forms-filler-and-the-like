#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 15:39:03 2020

@author: y4
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import json
import os
from fileImporter import *

if input('load or create? (l/c)').lower() == 'c':
    url = input('url: ')
    ff = webdriver.Chrome()
    ff.get(url)
    time.sleep(0.05)
    data = [url]
    while True:
        inp = input('what to do? (b - button or link, t - insert text, w - wait)').lower()
        if inp == 'b':
            path = input('xpath: ')
            try:
                ff.find_element_by_xpath(path).click()
            except:
                print('invalid')
            else:
                if input('add?y/n ') == 'y':
                    data.append(["b",path])
        elif inp == 't':
            path = input('xpath: ')
            toAdd = input('what to write: ')
            try:
                ff.find_element_by_xpath(path).send_keys(toAdd)
            except:
                print('invalid')
            else:
                if input('add?y/n ') == 'y':
                    data.append(["t",path,toAdd])
        elif inp == 'w':
            if input('seconds or untill element?(s/e)').lower() == "s":
                while True:
                    dat = input("how many seconds to wait?(decimal works) ")
                    try:
                        float(dat)
                    except:
                        print("not number")
                    else:
                        dat = float(dat)
                        break
            else:
                dat = input("xpath: ")
            if input('add?(y/n) ').lower() == 'y':
                data.append(["w",dat])
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
    ff.close()

else:
    while True:
        file = fillInput("location: ") + input('name: ')+'.json'
        if os.path.isfile(file):
            break
        else:
            print('not a file, try again\n--------------------------\n')
    with open(file,mode='r') as f:
        data = json.load(f)
    
    while True:
        try:
            times = int(input("how many times to run? "))
        except:
            print("not a number try again")
        else:
            break
    
    url = data[0]
    data = data[1:]
    ff = webdriver.Chrome()
    ff.get(url)
    time.sleep(0.1)
    for count in range(times):
        print('submitted: ',count)
        for x in data:
            if x[0] == 'b':
                try:
                    ff.find_element_by_xpath(x[1]).click()
                except:
                    print('invalid path "'+x[1]+'"')
            elif x[0] == 't':
                try:
                    ff.find_element_by_xpath(x[1]).send_keys(x[2])
                except:
                    print('invalid path "'+x[1]+'"')
            elif x[0] == 'w':
                if type(x[1]) == float:
                    time.sleep(x[1])
                else:
                    unt = x[1]
                    element = WebDriverWait(ff, 10).until(lambda x: x.find_element_by_xpath(unt))
    print('done')
    os.system('notify-send "done" "done"')
    ff.close()