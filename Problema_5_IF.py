ac=int(input("dati anul curenta"))
lc=int(input("dati luna curenta"))
zc=int(input("dati ziua curenta"))
an=int(input("dati anul nasterii"))
ln=int(input("dati luna nasterii"))
zn=int(input("dati ziua nasterii"))
if lc>ln or ( ln==lc and zc>zn):
    print((ac-an),"ani")
if lc<ln or (ln==lc and zc<zn):
    print((ac-an)-1)   