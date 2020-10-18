a=int(input("dati nr primului elev"))
b=int(input("dati n ral doilea elev"))
c=int(input("dati nr al treilea elev"))
a1=int(input("dati punctajul primului elev"))
b1=int(input("dati punctajul al doilea elev"))
c1=int(input("dati punctajul al treilea elev"))
if a1>b1 and a1>c1:
     print(a)
if b1>a1 and b1>c1:
    print(b)
if c1>a1 and c1>b1:
    print(c)
if a1==b1 and a1>c1:
    print(a,"",b) 
if a1==c1 and a1>b1:
    print(a,"",c) 
if b1==c1 and b1>a1:
    print(b,"",c) 
if a1==b1==c1:
    print("toti au acelasi numar de puncte")            