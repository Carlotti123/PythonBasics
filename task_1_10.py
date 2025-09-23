distance= int(input("Wie viele Kilometer willst du zurücklegen? "))
speed = int(input("Wie schnell willst du fahren? "))
gasconsume =int(input("Wie viel Benzin verbraucht dein Auto pro 100 Kilometer? "))

time = distance / speed
gas= distance * (gasconsume / 100)

print(f"Du wirst {gas}L Benzin verbrauchen")
print(f"Du wirst {time} Stunden für diese Strecke brauchen")