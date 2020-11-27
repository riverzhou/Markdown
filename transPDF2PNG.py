#!/usr/bin/env python3

import os
import sys
import fitz

def pdf2png(namePdf,namePng,zoom_x=4,zoom_y=4,rotation_angle=0):
    pdf = fitz.open(namePdf)
    for pg in range(pdf.pageCount):
        page = pdf[pg]
        trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotation_angle)
        #pm = page.getPixmap(matrix=trans, alpha=False)
        pm = page.getPixmap(matrix=trans)
        pm.writePNG('{}_{}.png'.format(namePng.rstrip('.pdf'),pg))
    pdf.close()

def printUsage(nameSelf):
    print('./{}  filename.pdf'.format(nameSelf))

def checkArgv(argv):
    if len(argv) != 2:
        printUsage(argv[0])
        return None, None
    filename = argv[1]
    if filename.endswith('.pdf') != True:
        printUsage(argv[0])
        return None, None
    path = os.getcwd() + '\\'
    namePdf = path+filename
    namePng = namePdf.rstrip('.pdf') + '.png'
    if os.path.isfile(namePdf) != True:
        print('{} not exist'.format(namePdf))
        printUsage(argv[0])
        return None, None
    return namePdf, namePng

def main(argv):
    namePdf, namePng = checkArgv(argv)
    if namePdf == None : return
    pdf2png(namePdf,namePng)

if __name__ == '__main__':
    main(sys.argv)
    
