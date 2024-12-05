import csv
from pylab import figure,show,plot, xlabel, ylabel, title
table=[]
table2016 = []
table2021 = []
table2023 = []
table_metad = []

# lecture des csv 
with open('donnees_2008.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=',')
    for row in reader:
        table.append(row)

with open('donnees_2016.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=',')
    for row in reader:
        table2016.append(row)

with open('donnees_2021.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=';')
    for row in reader:
        table2021.append(row)

with open('metadonnees_communes.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=';')
    for row in reader:
        table_metad.append(row)

with open('donnees_2023.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=';')
    for row in reader:
        table2023.append(row)

# variables 
popul = []
code = 0
annees = [2008,2016,2021,2023]

choix = input("Voulez-vous la population par département ou par ville ? \n Choisissez 'département' ou 'ville' : ")




if choix == "ville":
    entree = input("Entrez une ville : ")

    for i in range(len(table)):
        if entree == table[i][6]:
            popul.append(int(table[i][9]))

    for j in range(len(table2016)):
        if entree == table2016[j][6]:
            popul.append(int(table2016[j][9]))

    for k in range(len(table_metad)):
        if entree == table_metad[k][3]:
            code = table_metad[k][2]

    for l in range(len(table2021)):
        if code == table2021[l][2]:
            popul.append(int(table2021[l][5]))

    for m in range(len(table2023)):
        if entree == table2023[m][7]:
            popul.append(int(table2023[m][10]))

    print(popul)


    figure()
    title(f"Recensement {entree} de 2008 à 2023")
    xlabel('Années')
    ylabel('Population')
    plot(annees,popul)
    show()





"""elif choix == "département":
    departement = int("Entrez un n° de département : ")
    popul_dep = 0

    for i in range(len(table)):
        if departement == table[i][2]:
            popul_dep += int(table[i][9])
    popul.append(popul_dep)
    print(popul_dep)


    for j in range(len(table2016)):
        if departement == table2016[j][2]:
            popul_dep += int(table2016[j][9])
    popul.append(popul_dep)
    print(popul_dep)


    for l in range(len(table2021)):
        if departement == table2021[l][2]:
            popul_dep += int(table2021[l][5])
    popul.append(popul_dep)
    print(popul_dep)


    for m in range(len(table2023)):
        if departement == table2023[m][2]:
            popul_dep += int(table2023[m][10])
            print(popul_dep)

    popul.append(popul_dep)

    figure()
    title(f"Recensement du département n°{departement} de 2008 à 2023")
    xlabel('Années')
    ylabel('Population')
    plot(annees,popul)
    show()"""
            






# TP1-Recensement-NIBERT-SIBER_Jauris_TRANQUILLE_Romainv2
