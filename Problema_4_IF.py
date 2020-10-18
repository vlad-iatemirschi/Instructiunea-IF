a=int(input("dati varsta primei persoane"))
b=int(input("dati varsta persoanei doi"))
c=int(input("dati varsta persoanei trei"))
if a>18 and a<60:
    print(a)
if b>18 and b<60:
    print(b) 
if c>18 and c<60:
    print(c)
if a==b and b==c and a>18 and a<60:
    print(a,"",b,"",c)          
else:
    print("persoana nu au varsta necesara")          