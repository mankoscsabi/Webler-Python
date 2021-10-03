a = float(input("Elso oldal hossza"))
b = float(input("masodik oldal hossza"))
c = float(input("Elso harmadik hossza"))

s = (a+b+c) / 2
terulet = (s*(s-a)*(s-b)*(s-c))** 0.5
print('A háromszög területe', terulet)
