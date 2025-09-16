zahl=float(input("Gibt eine Zahl ein "))


if(zahl>10 and zahl<20):
    print(f"Die Zahl {round(zahl, 0)} liegt zwischen 10 und 20")
    
if(zahl>100 or zahl<0):
    print(f"Die Zahl {round(zahl, 0)} ist grösser als 100 oder kleiner als 0")
    
print("and verlangt das beide Bedingungen zutreffen. Bei or wiederrum muss nur eine der beiden oder beide Bedingung erfüllt sein")