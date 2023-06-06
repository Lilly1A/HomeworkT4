"""
Citiţi de la tastatură un număr întreg.
Dacă numărul este negativ, afişaţi mesajul `"That number is less than 0!"`.
Dacă este pozitiv, afişaţi `"That number is greater than 0!"`.
Dacă nu este nici negativ nici pozitiv afişaţi mesajul `"You picked 0!"`.
"""
n=int(input("Introdu un numar intreg "))
if n < 0:
    print("That number is less than 0!")
else:
    if n > 0:
        print("That number is greater than 0!")
    else:
        print("You picked 0!")

