from tkinter import Tk
import random

def copx(text):
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(text)
    r.update()
    r.destroy()
def nbr(text):
    res = ''
    for i in range(len(text)):
        res = res + text[len(text)-i-1]
    return res
def xfnd(fnd, text, x=''):
    res = []
    if not x == '':
        ndl = x.find(fnd); bl = x[0:ndl]
        ndr = ndl + len(fnd); br = x[ndr:len(x)]
        for i in range(len(text) - (len(fnd) - 1)):
            proof = text[i:i+len(fnd)]
            pfl = text[i-len(bl):i]
            pfr = text[i+len(fnd):i+len(fnd)+len(br)]
            if proof == fnd:
                if not (pfl == bl and pfr == br):
                    res.append(i)
    else:
        for i in range(len(text) - (len(fnd) - 1)):
            proof = text[i:i+len(fnd)]
            if proof == fnd:
                res.append(i)
    return(res)
def rep(text, cnd=2):
    text = str(text)
    res = ''
    for i in range(cnd):
        res = res + text
    if cnd == 0:
        res = None
    return res
def qlna(text):
    res = text.replace('\n', '')
    return res
def lethel(text):
    text = str(text).lower()
    alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+|-=\/"№;:?,.~`<>[]' + chr(0x007b) + chr(0x007d) + chr(39)
    res = ''
    for i in text:
        f = open('lethelalph.hxf', 'r', -1, 'utf-8')
        sel = (f.readlines()[alph.find(i)]).replace('\n', '')
        sym = sel[random.randint(0, len(sel)-1)]
        f.close()
        res = res + sym
    return res
