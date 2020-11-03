n = int(input('Digite o valor de N: '))

contador1 = 1
contador2 = 2

cima = 1
baixo = 0

for numero in range(contador2, n + 1):
   calc_cima = (contador2 * cima) + (contador1 * 1)
   calc_baixo = contador2 * contador1

   cima = calc_cima
   baixo = baixo + calc_baixo

   contador1 = calc_baixo
   contador2 += 1

final = (calc_cima / 2) / (calc_baixo / 2)
print(f'Resultado: {final}')
