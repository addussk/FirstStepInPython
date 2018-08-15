produkty=["mleko","ser","chleb"]

x=2
y=1

print(type(produkty))
print(produkty[0:x])

produkty.append("bulka")

x = produkty.count("bulka")

print(produkty,x)

cena = [10,15,12,15]

produkty.extend(cena)

print(produkty)

produkty=("mleko","ser","chleb")
print(type(produkty))


## slowniki

person = {"wiek":20 , "imie":"Ania" , "nazwisko":"kowalska"    }
print(person["wiek"])
print(person)
print(type(person))

i = 0

while i < 10:
    i += 1
    print(i)

suma =0
while 0:
    x=input("wprowadz liczbe iteracji:")
    suma +=int(x)
    print(suma)


lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

i=0

while i<10:
    print(lista[i])
    i += 1

print("petla for")

for litera in lista :
    if litera=="e":
        print(litera)

print("f.range")

for   i in range(50,100,5):
    print(i)

print("lekcja9")

fruits=['apple','orange','pear', 'banana', 'apple']

print("Sprawdzam {} {}".format("siema", "asdasd"))
i=0
for i, fruit in enumerate(fruits):
    if i==4:
        break
    print(fruit)
    print(i)

print(type(fruit))

print("lekcja10")

