#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

fin = open("dictionary.txt").readlines()
fout = open("escaped","w")

for line in fin:
    line = line.replace(" ","\s")
    #line = line.replace("(","\(")
    line = line.replace("%","\%")
    line = line.replace(".","\.")
    line = line.replace(":","\:")
    line = line.replace("/","\/")
    fout.write(line)

fout.close()

fin = open("escaped").readlines()
for line in fin:
    split = line.split("\t")
    before = split[0].strip()
    after = split[1].strip()
    command = 'find ../src -type f -print | xargs gsed -i "s/'+before+'/'+after+'/g"'
    print command
    os.system(command)


os.system("rm escaped")

