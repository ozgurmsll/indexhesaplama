name = input('adınız:')
kg = float(input('kilonuz:'))
hg = float(input('boyunuz:'))
index= (kg) / (hg ** 2)
zayif= (index >= 0 )and (index <=18.4)
normal= (index >=18.4)and (index <= 25)
dana=(index >=25)and (index <=29)



print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen zayıf  : {zayif}' )
print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen normal  : {normal}' )
print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen dana  : {dana}' )

