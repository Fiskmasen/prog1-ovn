svar = input("Antal sekunder: ")
sek = int(svar)
print("Inmatningen: ", sek)
tim = sek // 3600
sek = sek % 3600
print("Rest från timmar: ", sek)
min = sek // 60
sek = sek % 60
print("Rest från minuter: ", sek)
print("Timmar: ", tim)
print("Minuter: ", min)
print("Sekunder: ", sek)