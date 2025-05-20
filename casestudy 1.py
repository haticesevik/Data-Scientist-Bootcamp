#case1

x = 8
y = 3.2
z = 8j
a = "Hello World"
b = True
c = 23 < 22
l = [1, 2, 3]
d = {"Name": "Jake", "Age": 27, "Adress": "Downtown"}
t = ("Machine Learning", "Data Science")
s = {"Python", "Machine Learning", "Data Science"}

print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(type(b))
print(type(c))
print(type(l))
print(type(d))
print(type(t))
print(type(d))
print(type(s))

#case2

text = "The goal is to turn data into information, and information into insight."

print(text.upper())
print(text.replace(","," "))
print(text.replace("."," "))
print(text.upper().replace(",", " ").replace(".", " ").split())

#case3
lst = ["D", "a", "t", "a", " ", "S", "c", "i", "e", "n", "c", "e"]

print(len(lst))
print(lst[0])
print(lst[10])

new_list = [lst[0].upper(), lst[1].upper(), lst[2].upper(), lst[3].upper()]
print(new_list)

lst.pop(8)
print(lst)

print(lst.append(12))
print(lst)

lst.insert(8,"N")
print(lst)

#case4

dictionary = {"Daisy": 12, "Charlie": 7, "Teddy": 4, "Antonio": 9}
print(dictionary.keys())

print(dictionary.values())

dictionary["Daisy"] = 13
print(dictionary)

dictionary["Ahmet"] = ["Turkey", 24]
print(dictionary)

dictionary.pop("Antonio")
print(dictionary)

#case5

liste = [2,13,18,93,22]

def function (liste):
    even = []
    odd = []

    for i in liste:
        if i % 2 == 0 :
            even.append(i)
        else:
            odd.append(i)
    return even, odd

evenlist, oddlist = function(liste)

print("Tek sayılar:", oddlist)
print("Çift sayılar:", evenlist)



#case6
A = []
B = []

ogrenciler = ["Ali", "Veli", "Ayşe", "Burak", "Can", "Cem"]

for index, students in enumerate (ogrenciler):
    if index <= 2 :
        print("Mühendislik fakültesi öğrencileri"  + str(index) + "Öğrenci adı:" + students)
    else:
        print("Tıp Fakültesi Öğrencileri"  + str(index) + "." + "Öğrenci adı:" + students)

print(index, students)

#case7
ders_kodlari = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi = [3, 4, 2, 4]
kontenjan = [30, 75, 150, 25]

print(list(zip(ders_kodlari, kredi, kontenjan)))

for derskodu, kredi, kontenjan in zip(ders_kodlari, kredi, kontenjan):
    print(f"Kredisi {kredi} olan {derskodu} dersin kontenjanı {kontenjan} kişidir.")



#case8
set1 = {"data", "python", "machine", "learning"}
set2 = {"data", "machine"}

def küme(set1, set2):
    if set1.issuperset(set2):
        print(set1.intersection(set2))
    else:
        print(set2.difference(set1))
küme(set1, set2)


