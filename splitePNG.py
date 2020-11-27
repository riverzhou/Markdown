#!/usr/bin/env python3

import os
import sys
from math import ceil
from PIL import Image

Image.MAX_IMAGE_PIXELS = None

def splitePNG(namePng, maxFile=9):
    baseName = namePng.rstrip('.png')
    im = Image.open(namePng)
    w,h  = im.size
    number = min(maxFile, ceil(h/(2*w)))
    size = int(h/number)
    left = 0
    right = w
    top = 0
    botton = size
    for i in range(number):
        region = im.crop((left, top, right, botton))
        region.save("{}_{}.png".format(baseName, i))
        top = botton
        botton += size
        if botton > h:
            botton = h

def printUsage(nameSelf):
    print('./{}  filename.png'.format(nameSelf))

def checkArgv(argv):
    if len(argv) != 2:
        printUsage(argv[0])
        return None
    filename = argv[1]
    if filename.endswith('.png') != True :
        printUsage(argv[0])
        return None
    path = os.getcwd() + '\\'
    namePng = path+filename
    if os.path.isfile(namePng) != True:
        print('{} not exist'.format(namePng))
        printUsage(argv[0])
        return None
    return namePng

def main(argv):
    namePng = checkArgv(argv)
    if namePng == None : return
    #print('{}'.format(namePng))
    splitePNG(namePng)

if __name__ == '__main__':
    main(sys.argv)
    
