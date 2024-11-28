import csv

with open ("csddreg.csv",encoding="utf-8" )as file:
    csv1= csv.reader(file)
    saraksts=list(csv1)
    print("Faila nosaukums: ",file.name,"\n")
    print("Izdruka ir: ",saraksts,"\n")

print("Kopējais ierakstu skaits: ",len(saraksts))
print("-------------------------------------------------------------------------------------------------------------------")
pirmais=saraksts[1]
print("Pirmā rinda: ",pirmais)
print("-------------------------------------------------------------------------------------------------------------------")
pedejais=saraksts[-1]
print("Pēdējā rinda: ",pedejais)
print("-------------------------------------------------------------------------------------------------------------------")
trnobeig=saraksts[-3]
print("Trešais no beigām: ",trnobeig)
print("-------------------------------------------------------------------------------------------------------------------")
pirmpieci=saraksts[1:5]
print("Pirmie pieci: ",pirmpieci)
print("-------------------------------------------------------------------------------------------------------------------")