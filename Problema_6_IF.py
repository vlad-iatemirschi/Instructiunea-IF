a=int(input("dati prima nota"))
b=int(input("dati a doua nota"))
c=int(input("dati a treia nota"))
if c and b and a <=10 and c and b and a >=0:
    if c>=8:
        print(a,b,c)
    if c<8:
        if a>b and a>c:
            print(a)
        if b>a and b>c:
            print(b)
        if c>a and c>b:
            print(c)
        if a==b==c:
            print("nu am primit note" )
else:
    print("eroare")                            