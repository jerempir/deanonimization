# -*- coding: cp1251 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re
key = []
alpha = 'abcdefghijklmnopqrstuvwxyz'
rualpha = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
i = 0
f = open("dehash.txt","r")
lines = f.readlines()
def sezarru(x,n):
    itog = ''
    for c in x:
        if c in rualpha:
            itog += rualpha[(rualpha.index(c) - n) % len(rualpha)]
        else:
            itog += c
    return itog
def sezareng(x):
    itog = ''
    global i
    n = key[i]
    i+=1
    for c in x:
        if c in alpha:
            itog += alpha[(alpha.index(c) - n) % len(alpha)]
        else:
            itog += c
    return itog
def adr(x):
    x = x.lower()
    n = len(x)
    k = 0
    for i in range(n,0,-1):
        if x[i-1] == ".":
            word = x[i-3]+x[i-2]
            break
    while sezarru(word,k) != "кв":
        k+=1
    key.append(k)
    return sezarru(x,k)
def hash(x,lines):
    for i in lines:
        some_val = str(i).split(":")
        if x == some_val[0]:
            return some_val[1]

df = pd.read_excel('database.xlsx',engine='openpyxl')
df['Адрес'] = df["Адрес"].apply(lambda x: adr(x))
df['key'] = key
df['email'] = df["email"].apply(lambda x:sezareng(x))
df['Телефон'] = df["Телефон"].apply(lambda x:hash(x,lines))
df.to_csv('filename.csv',index=False)