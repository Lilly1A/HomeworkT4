"""
Scrieți un program care cere utilizatorului să introducă o propoziție.
Dacă propoziția se încheie cu un semn de întrebare ("?"),
afișați mesajul „Aceasta este o întrebare”.
În caz contrar, afișați mesajul „Aceasta nu este o întrebare”
"""
str=input('Introduceti o propozitie ')
if str[-1] == '?':            # sau if str[-1] in '?'
    print('Aceasta este o întrebare')
else:
    print('Aceasta nu este o întrebare')