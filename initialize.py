#!/usr/bin/env python
#-*-coding:utf-8-*-

import glob
import os

def change_quote(path):
    command = """ find """ +path+ """ -type f -print | xargs gsed -i "s/\\"/\\'/g" """ 
    os.system(command)

for file in glob.glob('../src/guis/*'):
    try:
        file.split('/')[-1].split('.')[1]
    except:
        #change_quote(file)
        fin = open(file,"r").readlines()
        fout = open(file,"w")
        i = 0
        for line in fin:
            fout.write(line)
            if i==0:
                fout.write("#-*- coding:utf-8 -*-")
                fout.write("\n")
            i += 1

for file in glob.glob('../src/py/*.py'):
    #change_quote(file)
    fin = open(file,"r").readlines()
    fout = open(file,"w")
    i = 0
    for line in fin:
        fout.write(line)
        if i==0:
            fout.write("#-*- coding:utf-8 -*-")
            fout.write("\n")
        i += 1

for file in glob.glob('../src/scripts/*'):
    try:
        file.split('/')[-1].split('.')[1]
    except:
        #change_quote(file)
        fin = open(file,"r").readlines()
        fout = open(file,"w")
        i = 0
        for line in fin:
            fout.write(line)
            if i==0:
                fout.write("#-*- coding:utf-8 -*-")
                fout.write("\n")
            i += 1
    

