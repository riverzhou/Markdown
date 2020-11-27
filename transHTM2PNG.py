#!/usr/bin/env python3

import os
import sys
from selenium import webdriver

def savePng(nameHtml, namePng):
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')
    option.add_argument('--disable-gpu')
    option.add_argument('--window-size=1024,768')
    option.add_argument('--force-device-scale-factor=2.0')
    option.add_argument('--hide-scrollbars')
    driver = webdriver.Chrome(options=option)
    driver.get('file://' + nameHtml)
    #print(driver.title)
    scroll_width = driver.execute_script('return document.body.parentNode.scrollWidth')
    scroll_height = driver.execute_script('return document.body.parentNode.scrollHeight')
    print(scroll_width, scroll_height)
    driver.set_window_size(scroll_width, scroll_height)
    driver.save_screenshot(namePng)
    driver.quit()

def printUsage(nameSelf):
    print('./{}  filename.html'.format(nameSelf))

def checkArgv(argv):
    if len(argv) != 2:
        printUsage(argv[0])
        return None, None
    filename = argv[1]
    if filename.endswith('.html') != True and filename.endswith('.htm') != True:
        printUsage(argv[0])
        return None, None
    path = os.getcwd() + '\\'
    nameHtml = path+filename
    namePng = nameHtml.rstrip('.html').rstrip('.htm') + '.png'
    if os.path.isfile(nameHtml) != True:
        print('{} not exist'.format(nameHtml))
        printUsage(argv[0])
        return None, None
    return nameHtml, namePng

def main(argv):
    nameHtml, namePng = checkArgv(argv)
    if nameHtml == None : return
    savePng(nameHtml, namePng)

if __name__ == '__main__':
    main(sys.argv)
    
