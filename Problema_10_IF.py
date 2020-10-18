a=int(input("Numarul de gaini: ")) 
b=int(input("Numarul de boabe: ")) 
ag=b//a
bc=b-(a*ag) 
if ag>bc: 
    print("Gaina primeste cu ",ag-bc," boabe mai mult") 
if bc>ag: 
    print("Curcanul primeste cu ",bc-ag," boabe mai mult") 
if bc==ag: 
    print("Primesc acelasi numar de boabe",b//a)
                   