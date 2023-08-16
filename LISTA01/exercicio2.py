#Faça um programa que preencha por leitura um vetor de 10 posiçoes,
#e conta quantos valores diferentes existem no vetor
vetor = []
for a in range(10):
    cleiton=int(input(f'Digite o {a + 1} numero: '))
    vetor.append(cleiton)
print(vetor)
listavazia = []
for i in vetor:
    if i not in listavazia:
        listavazia.append(i)
print(f'Números distintos:{listavazia}')
print(f'Quantidade de num diferentes:{len(listavazia)}')
