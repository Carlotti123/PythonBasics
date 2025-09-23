pswd = input("Gib ein Passwort ein:")

if len(pswd) < 8:
    print("Dein Passwort ist zu kurz, verwende mindestens 8 Zeichen")
else:
    print("Dein Passwort ist mindestens 8 Zeichen lang. Super!")