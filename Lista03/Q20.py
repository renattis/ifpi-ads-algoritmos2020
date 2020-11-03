n = int(input('Digite o valor de N: '))

constante = 1
contador = 2

cima = 1
baixo = 1

for numero in range(contador, n - 1):
#calculo 1
   calc_cima = (contador * cima) - (baixo * cima)
   calc_baixo = contador * constante

#variáveis de controle
   cima = calc_cima
   baixo = calc_baixo

   contador += 1

#calculo 2
   calc_cima = (contador * cima) + (baixo * cima)
   calc_baixo = contador * baixo

#variáveis de controle
   cima = calc_cima
   baixo = calc_baixo

#calculo final
cima_final = (n * cima) - (baixo * constante)
baixo_final = n * baixo

#resultado
final = (cima_final / 2) / (baixo_final / 2)
print(f'Resultado: {final}')
