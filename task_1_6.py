mony=20
price=3.2

amount=(mony//price)
rest=(mony%price)

print(f"Mit {mony}CHF kann man {int(amount)} Stück Schokoriegel kaufen und hat {round(rest, 2)}CHF übrig")