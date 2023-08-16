#4- Um dado é lançado 50 vezes, e o valor correspondente é armazenado em um vetor. 
# Faça um programa que simule o lançamento do dado e determine o percentual 
# de ocorrências de face 6 do dado dentre esses 50 lançamentos.

vetor=[]
lancamento = 10
for a in range(lancamento):
    jogada= int(input(f'{a+1}° jogada: '))
    vetor.append(jogada)
print(vetor)
contador= 0
for h in vetor:
    if h == 6:
        contador+=1
media= (contador/lancamento)*100
print(f'A porcentagem é {media:.0f}%')
