n = int(input('Digite o valor de N: '))
contador = 2
constante = 1

cima = 1
baixo = 1
cima_impar = 3

for numero in range(contador, n + 1):
   # operacao 1
   calc_cima = (baixo * cima_impar) + (contador * cima)
   calc_baixo = contador * baixo

   contador += 1
   cima_impar += 2

   cima = calc_cima
   baixo = calc_baixo
# operacao 2
divisao_cima = cima / 2
divisao_baixo = baixo / 2

# Resultado
final = (divisao_cima / 2) / (divisao_baixo / 2)
print(f'Resultado: {final}')
