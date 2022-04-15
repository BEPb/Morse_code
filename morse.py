"""
Python 3.9 программа перевода с английского в код Морзе
Название файла morse.py

Version: 0.1
Author: Andrej Marinchenko
Date: 2022-04-15
"""

def morse(kata):
        morseAlphabet ={
                "A" : ".-",             "B" : "-...",
                "C" : "-.-.",           "D" : "-..",            "E" : ".",
                "F" : "..-.",           "G" : "--.",            "H" : "....",
                "I" : "..",             "J" : ".---",           "K" : "-.-",
                "L" : ".-..",           "M" : "--",             "N" : "-.",
                "O" : "---",            "P" : ".--.",           "Q" : "--.-",
                "R" : ".-.",            "S" : "...",            "T" : "-",
                "U" : "..-",            "V" : "...-",           "W" : ".--",
                "X" : "-..-",           "Y" : "-.--",           "Z" : "--..",
                " " : "/"
        }
        key=[]
        kat = kata.upper()
        for k in kat:
                key.insert(len(key), k)
        for a in key:
                i = key.index(a)
                key[i] = morseAlphabet[a]


        return " ".join(key)

def reverse(m):
        alphabet ={
                ".-":  "A",             "-...": "B",
                "-.-.":"C",             "-..":  "D",           ".":    "E",
                "..-.":"F",             "--.":  "G",           "....": "H",
                "..":  "I",             ".---": "J",           "-.-":  "K",
                ".-..":"L",             "--":   "M",           "-.":   "N",
                "---": "O",             ".--.": "P",           "--.-": "Q",
                ".-.": "R",             "...":  "S",           "-":    "T",
                "..-": "U",             "...-": "V",           ".--":  "W",
                "-..-":"X",             "-.--": "Y",           "--..": "Z",
                "/"   :" "
       }
        kta = m.split(" ")
        for a in kta:
                i = kta.index(a)
                kta[i] = alphabet[a]
        return "".join(kta).title()


while True:
        a = input("Enter text or cipher for reverse Morse code translation: ")
        if a[0] =="." or a[0] == "-":
                print(reverse(a))
        else:
                print(morse(a))











                

