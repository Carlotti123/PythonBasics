hours= int(input("Gib Stunden an: "))
min= int(input("Gib Minuten an: "))
sec= int(input("Gib Sekunden an:"))

hoursinsec = hours * 60 * 60
mininsec = min * 60

finaltime = sec + mininsec + hoursinsec

print(f"Deine Zeit ist {round(finaltime / 60 / 60, 2)}")