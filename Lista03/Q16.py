n = int(input('Digite o valor de N: '))
qtd_atual = 2
anterior = 0
atl = 1
print(anterior, atl)

for numero in range(1, n - 1):
   novo_atual = anterior + atl
   anterior = atl
   atl = novo_atual

   print(f'{atl} \n')
   qtd_atual += 1
