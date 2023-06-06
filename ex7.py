"""
Scrieți un program pentru a citi temperatura de la utilizator și pentru a afișa un mesaj adecvat în funcție de starea temperaturii de mai jos.
Temp -40-(-10) atunci 'Vremea extrem de rece'
Temp -10-0 atunci 'Vremea foarte rece'
Temp 0-10 atunci 'Vreme rece'
Temp 10-20 atunci 'Vreme normala'
Temp 20-30 atunci 'Vreme calda'
Temp 30-40 atunci 'Este foarte cald'
Temp >=40 atunci 'Este extrem de cald'
"""
temp=int(input('Introduceti temperatura '))
if (temp > -40) and (temp < -10):
   print('Vreme extrem de rece')
else:
   if temp >= -10 and temp < 0:
        print('Vremea foarte rece')
   else:
        if (temp >= 0) and (temp< 10):
             print('Vreme rece')
        else:
             if (temp >= 10) and temp< 20:
                  print('Vreme normala')
             else:
                  if temp >= 20 and temp< 30:
                       print ('Vreme calda')
                  else:
                       if temp >= 30 and temp< 40:
                            print ('Este foarte cald')
                       else:
                            if temp>=40:
                                 print('Este extrem de cald')


