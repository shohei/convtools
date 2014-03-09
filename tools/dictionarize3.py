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

def get_word(part,string):
    if string == "label=":
        extracted1 = part.split(string)[1]
        if "'" in extracted1:
            extracted2 = extracted1.split("'")[1]#.strip() 
            extracted2 = "'"+extracted2+"'"
        elif '"' in extracted1:
            extracted2 = extracted1.split('"')[1]#.strip() 
            extracted2 = '"'+extracted2+'"'
        return extracted2 
        
    elif string == "SetLabel":
        extracted1 = part.split('SetLabel')[1]
        if "'" in extracted1:
            extracted2 = extracted1.split("'")[1]
            if not extracted2[-1] == "'":
                extracted2 = "'" + extracted2 + "'"
        elif '"' in extracted1:
            extracted2 = extracted1.split('"')[1]
            if not extracted2[-1] == '"':
                extracted2 = '"' + extracted2 + '"'
        else:
            extracted2 = extracted1.split('(')[1].split(')')[0]
        print extracted2
        return extracted2 

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
    before = line#.split(':')[1].strip()
    #before = line
    if 'label=' in before:
        before = get_word(before,"label=")
        insert(before)
    elif 'SetLabel' in before:
        before = get_word(before,"SetLabel")
        insert(before)
fout.close()

array = []
fin = open("before2").readlines()
for line in fin:
    array.append(line.strip())
array = sorted(list(set(array)))

fout = open("dictionary_temp3.txt","w")
for a in array:
    fout.write(a)
    fout.write("\n")

fout.close()


os.system("rm before1")
os.system("rm before2")


