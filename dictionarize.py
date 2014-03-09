#!/usr/bin/env python
#-*- coding:utf-8 -*-

import commands
import os

fout = open("before1","w")
string1 = commands.getoutput("find ../src -type f -print | xargs grep 'label='")
fout.write(string1)
string2 = commands.getoutput("find ../src -type f -print | xargs grep 'SetLabel'")
fout.write(string2)
string3 = commands.getoutput("find ../src -type f -print | xargs grep 'SetLabel'")
fout.write(string3)

fout.close()

fin = open("before1").readlines()
fout = open("before2","w")

def split(part,string):
    if string == "label=":
        return part.split(string)[1].strip().split(')')[0].strip() 
    elif string == "SetLabel":
        return part.split('SetLabel')[1].strip().split('(')[1].split(')')[0].strip()

def insert(part):
    squote = False
    dquote = False 
    extracted = part 
    if extracted == "' ' ":
        return 
    if extracted == "''":
        return
    if extracted == '" "':
        return 
    if extracted == '""':
        return
    if "'" in part:
        squote = True
    elif '"' in part:
        dquote = True
    else:
        return 
    #if not squote and dquote:
    #    fout.write("'")
    fout.write(extracted)
    if squote and extracted[-1] != "'":
        fout.write("'")
    elif dquote and extracted[-1] != '"':
        fout.write('"')
    #else:
    #    fout.write("'")
    fout.write("\t")
    if squote:
        fout.write("''")
    elif dquote:
        fout.write('""')
    else:
        fout.write("''")
    fout.write("\n")

for line in fin:
    before = line.split('\t')[0].strip()
    if 'label=' in before:
        before = split(before,"label=")
        insert(before)
    elif 'SetLabel' in before:
        before = split(before,"SetLabel")
        insert(before)
fout.close()

array = []
fin = open("before2").readlines()
for line in fin:
    array.append(line.strip())
array = sorted(list(set(array)))

fout = open("dictionary_temp.txt","w")
for a in array:
    fout.write(a)
    fout.write("\n")

fout.close()


os.system("rm before1")
os.system("rm before2")


