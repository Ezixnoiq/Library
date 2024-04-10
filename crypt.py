def txnum(text, rov):
    res = ''
    for i in text:
        sym = str(bin(ord(i)))
        sym = sym[2:len(sym)]
        if rov == True:
            while len(sym) < 16:
                sym = '0' + sym
        res = res + sym
    return res
def txord(text):
    k = 0
    res = ''
    for i in range(int(len(text) / 16)):
        sym = ''
        for j in range(16):
            sym = sym + text[k]
            k += 1
        res = res + chr(int(sym, 2))
    return res
def hash(text, force=8):
    dgr = 2 ** force
    bls = int(dgr / 8)
    sgmts = []
    nmn = txnum(text, False)
    i = 0
    while not len(nmn) % (dgr) == 0:
        nmn = nmn + nmn[i]
        i += 1
    k = 0
    for i in range(int(len(nmn) / bls)):
        word = ''
        for j in range(int(len(nmn) / 8)):
            word = word + nmn[k]
            k += 1
        sgmts.append(word)
    pre = ''
    for i in range(bls):
        sym = 0
        for j in range(8):
            sym = sym ^ int(sgmts[j][i])
        pre = pre + str(sym)
    res = ''
    k = 0
    for i in range(int(len(pre) / 4)):
        sym = ''
        for j in range(4):
            sym = sym + pre[k]
            k += 1
        sym = str(hex(int(sym, 2)))
        sym = sym[2:len(sym)]
        res = res + sym
    return res
def encrypt(text, key):
    hsh = hash(key, force=9)
    bh = ''
    for i in hsh:
        sym = str(bin(int(i, 16)))
        sym = sym[2:len(sym)]
        while len(sym) < 4:
            sym = '0' + sym
        bh = bh + (sym)
    nmn = txnum(text, True)
    pre = ''
    for i in range(len(nmn)):
        pre = pre + str(int(nmn[i]) ^ int(bh[i % len(bh)]))
    res = ''
    k = 0
    for i in range(int(len(pre) / 4)):
        sym = ''
        for j in range(4):
            sym = sym + pre[k]
            k += 1
        sym = str(hex(int(sym, 2)))
        sym = (sym[2:len(sym)]).upper()
        res = res + sym
    return res
def decrypt(text, key):
    hsh = hash(key, force=9)
    bh = ''
    for i in hsh:
        sym = str(bin(int(i, 16)))
        sym = sym[2:len(sym)]
        while len(sym) < 4:
            sym = '0' + sym
        bh = bh + (sym)
    x = ''
    for i in text:
        sym = str(bin(int((i).lower(), 16)))
        sym = sym[2:len(sym)]
        while len(sym) < 4:
            sym = '0' + sym
        x = x + (sym)
    nmn = ''
    for i in range(len(x)):
        nmn = nmn + str(int(x[i]) ^ int(bh[i % len(bh)]))
    res = txord(nmn)
    return res