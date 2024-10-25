import math

a = float(input("Entrez la valeur de a: "))
b = float(input("Entrez la valeur de b: "))
c = float(input("Entrez la valeur de c: "))

if a == 0:
    print("Ce n'est pas une équation quadratique.")
else:
    discriminant = b**2 - 4 * a * c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f"Les solutions sont x1 = {root1} et x2 = {root2}")
    elif discriminant == 0:
        root = -b / (2 * a)
        print(f"La solution est x = {root}")
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        print(f"Les solutions sont x1 = {real_part} + {imaginary_part}i et x2 = {real_part} - {imaginary_part}i")
