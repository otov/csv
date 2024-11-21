import csv

with open ("degvv2024ml.csv",encoding="utf-8" )as file:
    csv1= csv.reader(file)
    saraksts=list(csv1)
    print("Izdruka ir: ",saraksts,"\n")

print(file.name)

garums=len(saraksts)
print(garums)

pirmais=saraksts[2]
print(pirmais)

pirmie = saraksts[2:7]
print(pirmie)


def ievade():
    file = open ("degvv2024ml.csv",encoding="utf-8" )
    csv1= csv.reader(file)
    masivs=list(csv1)
    num=input("Ievadiet kārtas nr.: ")
    nummurs=int(num)
    elements=masivs[nummurs+1]
    print(elements)

ievade()


