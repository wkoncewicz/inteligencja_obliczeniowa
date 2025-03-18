import pandas as pd
import numpy as np

df = pd.read_csv("iris_with_errors.csv")

kolumny1 = df.values[:,0]
kolumny2 = df.values[:,1]
kolumny3 = df.values[:,2]
kolumny4 = df.values[:,3]
kolumny5 = df.values[:,4]
counter = 0

def checkIfEmpty(column):
    global counter
    for i in range (len(column) - 1):
        if column[i] == '-' or pd.isna(column[i]):
            counter=counter+1
            column[i] = '0'
    return column


kolumny1 = checkIfEmpty(kolumny1)
kolumny2 = checkIfEmpty(kolumny2)
kolumny3 = checkIfEmpty(kolumny3)
kolumny4 = checkIfEmpty(kolumny4)
kolumny5 = checkIfEmpty(kolumny5)
print(kolumny1)
print(df)
print("Empty cells:", counter)

def replaceWrongCells(column):
    column = np.array(column, dtype=float)
    mean_value = np.mean(column)
    print(mean_value)

    for i in range(len(column) - 1):
        if column[i] <= 0 or column[i] >= 15:
            column[i] = mean_value
    return column

kolumny1 = replaceWrongCells(kolumny1)
kolumny2 = replaceWrongCells(kolumny2)
kolumny3 = replaceWrongCells(kolumny3)
kolumny4 = replaceWrongCells(kolumny4)
print(kolumny2)

def correctName(name):
    setosa_count = 0
    virginica_count = 0
    versicolor_count = 0
    for i in range (len(name) - 1):
        if i <= (len('Setosa') - 1) and name[i] == 'Setosa'[i]:
            setosa_count += 1
        if i <= (len('Virginica') - 1) and name[i] == 'Virginica'[i]:
            virginica_count += 1
        if i <= (len('Versicolor') - 1) and name[i] == 'Versicolor'[i]:
            versicolor_count += 1

    print(setosa_count, virginica_count, versicolor_count)
    setosa_count = setosa_count/len('Setosa')
    virginica_count = virginica_count/len('Virginica')
    versicolor_count = versicolor_count/len('Versicolor')

    if setosa_count > virginica_count and setosa_count > versicolor_count:
        return "Setosa"
    elif setosa_count < virginica_count and virginica_count > versicolor_count:
        return "Virginica"
    elif versicolor_count > virginica_count and setosa_count < versicolor_count:
        return "Versicolor"
    else:
        print(setosa_count, virginica_count, versicolor_count)
        return 'NA' 

def replaceWrongNames(column):
    for i in range(len(column) - 1):
        if column[i] != 'Setosa' and column[i] != 'Virginica' and column[i] != 'Versicolor':
            column[i] = correctName(column[i])
    return column

print(kolumny5)
kolumny5 = replaceWrongNames(kolumny5)
print(kolumny5)

