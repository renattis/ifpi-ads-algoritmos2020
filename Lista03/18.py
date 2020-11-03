n = int(input('Digite: '))

contador1 = 1
contador2 = 2
novo_contador = 1

cima = 1
baixo = 4

for numero in range(contador2, n + 1):
   calc_cima = ((n - novo_contador)*cima) + (baixo * contador2)
   calc_baixo = (n - novo_contador) * baixo

   cima = calc_cima
   baixo = calc_baixo

   contador2 += 1
   novo_contador += 1

final = (calc_cima / 2) / (calc_baixo / 2)
print(f'Resultado: {final}')
