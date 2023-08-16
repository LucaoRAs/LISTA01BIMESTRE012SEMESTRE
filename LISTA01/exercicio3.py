#3- Faça um programa que preencha por leitura um vetor de 5 posições, 
# e informe a posição em que um valor x (lido do teclado) 
# aparece pela primeira vez no vetor. 
# Caso o valor x não seja encontrado, o programa deve imprimir o valor -1

vetor= []
e = 5
for a in range(e):
    melao= int(input(f'Digite o {a+1}° numero: '))
    vetor.append(melao)
print(vetor)
x = int(input('Qual o valor solicitado? '))
for i, h in enumerate(vetor):
    if x == h:
        print(f'esse numero esta na posicao: {i}')
if x not in vetor:
        print(-1)
    