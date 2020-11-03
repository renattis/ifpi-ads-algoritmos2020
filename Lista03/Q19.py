n = int(input('Digite o valor de N: '))
constante = 1
contador = 2
novo_contador = 1


cima = 1
baixo = 4


# Esse -1 é para descontar já que o contador começa com 2 e assim poder chegar até a operação final
for numero in range(contador, n - 1):

   # Operação 1
   calc_cima = (n * (n - novo_contador)) - (contador * constante)
   calc_baixo = n * contador

   cima = calc_cima
   baixo = calc_baixo

   contador += 1
   novo_contador += 1

# Operação 2
   calc_cima = ((n - novo_contador)*cima) + (baixo * contador)
   calc_baixo = ((n - novo_contador)*baixo)

   cima = calc_cima
   baixo = calc_baixo

# Operação final
cima_final = (baixo * n) - (constante * cima)
baixo_final = baixo * constante

# Mostrar resultado final na tela
final = (cima_final / 2) / (baixo_final / 2)
print(f'Resultado: {final}')
