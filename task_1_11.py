#BMI = Körpergewicht (in kg) / (Körpergröße (in m))²

weight = int(input("Wie Schwer bist du in Kg? "))
height = float(input("Wie gross bist du in Meter? "))

bmi = weight / (height**2)

print(f"Du hast einen BMI von {round(bmi, 2)}")