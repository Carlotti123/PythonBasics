zahl1=float(input("Gib eine Zahl ein: "))
zahl2=float(input("Gib eine zweite Zahl ein: "))

summe=zahl1+zahl2
produkt=zahl1*zahl2
differenz=zahl1-zahl2
quotient=zahl1/zahl2


print(f"{zahl1} plus {zahl2} ist gleich {round(summe, 2)}")
print(f"{zahl1} mal {zahl2} ist gleich {round(produkt, 2)}")
print(f"{zahl1} minus {zahl2} ist gleich {round(differenz, 2)}")
print(f"{zahl1} geteilt durch {zahl2} ist gleich {round(quotient, 2)}")

print(" / dividiert")
print("// dividiert und rundet das ergebnis auf eine Ganzzahl AB")