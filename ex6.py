"""
Scrieţi un program care citeşte de la tastatură numele unei persoane.
Dacă numele nu începe cu literă mare, atunci programul transformă valoarea citită în numele persoanei scris cu literă mare.
După aceasta, afişează la ecran `"Salut, <numele citit de la tastatura care începe cu litera mare>!"`.
"""
nume=input('Introduceti nemele ')
nume1=nume.capitalize()
if nume[0]==nume1[0]:
    print(f"Salut,{nume1}")
else:
    print(nume1)
