zahl1=float(input("Gib eine Zahl ein "))
zahl2=float(input("Gib eine zweite Zahl ein "))

if(zahl1>zahl2):
    print(f"{zahl1} ist grösser als {zahl2}")
elif(zahl1<zahl2):
    print(f"{zahl2} ist grösser als {zahl1}")
else:
    print("Die beiden eingegebenen Zahlen sind gleich gross")


print("Ein vergleich wie 5<10 gibt einen boolean wert aus. Dieser kann entweder True oder False sein")