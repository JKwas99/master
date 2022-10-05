name = []

for i in range(0,10):
    x = input("Podaj liczbę "+str(i+1)+"/10: ")
    name.append(int(x))

print("Użytkownik podał następujące liczby - "+str(name))

name_length = len(name)
max = name[0]
min = name[0]

for i in range(0,name_length-1):
    if(max<name[i]):
        max = name[i]

for i in range(0,name_length-1):
    if(min>name[i]):
        min = name[i]

print("Największa podana liczba przez użytkownika to - "+str(max))

print("Najmniejsza podana liczba przez użytkownika to - "+str(min))