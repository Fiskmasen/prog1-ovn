import math#import math behövs för att kunna skriva in och använda vissa matematiska tecken/uttryck, som till exempel pi

r = input ("Mata in radien: ")#input är det man vill att programet ska skriva ut för att be användaren skriva in något
r = float(r)#float är i stort sätt tal/siffror med decimaler, och i det här fallet så använder vi float för att omvandla r (alltså radien) från en string till en float. Om man inte gör det och lämnar "r" som en string, så kommer inte programmet att fungera
V = 4*math.pi*r**3/3#Detta är ena formeln given från boken
print(V)#print behövs för att skriva ut programmet till terminalen

A = 4*math.pi*r**2#Detta är andra formeln given från boken
print(A)