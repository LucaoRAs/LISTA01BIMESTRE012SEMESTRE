#dExercício 01 - 10/08/2023
#Dada a lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52] faça um programa que:
#a) imprima o maior elemento
#b) imprima o menor elemento
#c) imprima os números pares
#d) imprima o número de ocorrências do primeiro elemento da lista
#e) imprima a média dos elementos
#f) imprima a soma dos elementos de valor negativo

lista= [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]
#a) imprima o maior elemento
print('Maior valor')
print(max(lista))
print('-------------')
#b) imprima o menor elemento
print('Menor valor:')
print(min(lista))
print('-------------')
#c) imprima os números pares
for i in lista:
    if i%2==0:
        print(i)
print('-------------')
#d) imprima o número de ocorrências do primeiro elemento da lista
contador=0
for u in lista:
    if u == lista[0]:
        contador+=1
print(f'Numero de ocorrencias é: {contador}')
print('-------------')
#e) imprima a média dos elementos
soma = sum(lista)
media = soma/len(lista)
print(f'a média é: {media:.2f}')
print('-------------')
#f) imprima a soma dos elementos de valor negativo
soma2= 0
for h in lista:
    if h < 0:
        soma2= soma2+h
print(f'A soma dos num negativos é: {soma2}') 
