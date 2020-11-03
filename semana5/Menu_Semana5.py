def opcoes_menu(lista,menu):

   def inserir_valores(lista):
      lista.clear()
      qtd = int(input('Quantos valores desejar inserir?'))

      for i in range(qtd):
         valor = int(input('Valor: '))
         lista.append(valor)

      print('Valores inseridos com sucesso!')
      input('<enter> to continue...')


   def mostra_valor(lista):
      posicao = int(input('Qual posição? '))
      print('Valor buscado:')
      print(lista[posicao])

      input('<enter> to continue...')

   #3
   def remover_final(lista):
      lista.pop()
      print(f' Resultado: {lista}')

   #4
   def remover_inicio(lista):
      del lista[0]
      print(f' Resultado: {lista}')

   #5
   def remover_posicao(lista):
      posicao = int(input(f'A lista vai até {len(lista)}. Quer remover o item de qual posição? '))
      
      if posicao > len(lista):
         print(f'Erro digite um valor dentro dos disponíveis')
      else:
         del lista[posicao]
         print(f' Resultado: {lista}')

   #6
   def mostrar_todos_valores(lista):
      for numero in lista:
         print(f'Os valores da lista são: {numero}')
   #7
   def add_valor_posicao(lista):
      valor = int(input(f'Qual o valor quer adcionar?'))
      posicao = int(input(f'Em qual posição?'))
      lista.inset(posicao,valor)
      print(f' Resultado: {lista}')

   #8
   def contagem(lista):
      par = 0
      impar = 0
      for numero in lista:
         if (numero%2) == 0:
            par += 1
         else:
            impar += 1
      print(f'Números pares:{par} Números ímpares:{impar} ')

      positivo = 0
      negativo = 0
      for numero in lista:
         if numero >= 0:
            positivo += 1
         elif numero < 0:
            negativo += 1
      print(f'Números positivos: {positivo} Números negativos: {negativo}')

      primo = 0
      for numero in lista:
         if numero % 2 == 1:
            primo += 1
         else:
            pass
      print(f'Números primos: {primo}')

   #9
   def media_valores(lista):
      soma = 0
      tamanho = len(lista)

      for numero in lista:
         soma += numero
      media = soma / tamanho

      print(f'A média de valores é: {media}')

   #10

   def ocorrencias(lista):
      valor = int(input('Qual valor quer procurar as ocorrências: '))
      ocorrencias = lista.count(valor)
      print(f'As ocorrências são: {ocorrencias}')

   #11
   def dobrar(lista):
      lista_dobrados = []

      for numero in lista:
         dobrar = numero * 2
         lista_dobrados.append(dobrar)
      print(f'Números dobrados: {lista_dobrados}')


   #12
   def apagar(lista):
      lista.clear()
      print('A lista foi apagada')

   #13
   def inverter(lista):
      inverter = lista.reverse()
      print(f'A lista invertida é: {inverter}')

   #14
   def ordem_crescente(lista):
      ordenar = sorted(lista)
      print(f'A lista em ordem é: {ordenar}')

   while True:  # Condição sempre verdadeira, só irá para em caso de break ou error
      opcao = int(input(menu))

      # Verificar operacao a fazer de acordo com a opcao
      if opcao == 1:
         # Listas quando passadas como argumentos e modificadas por
         # funções não é necessário retorná-las
         # Se modificar a lista dentro de um função, as variáveis que já
         # apontavam para ela, terão acesso a lista moficiada normalmente
         # Por isso nao está ```lista = inserir_valores(lista)````
         inserir_valores(lista)
      elif opcao == 2:
         mostra_valor(lista)
      elif opcao == 3:
         remover_final(lista)
      elif opcao == 4:
         remover_inicio(lista)
      elif opcao == 5:
         remover_posicao(lista)
      elif opcao == 6:
         mostrar_todos_valores(lista)
      elif opcao == 7:
         add_valor_posicao(lista)
      elif opcao == 8:
         contagem(lista)
      elif opcao == 9:
         media_valores(lista)
      elif opcao == 10:
         ocorrencias(lista)
      elif opcao == 11:
         dobrar(lista)
      elif opcao == 12:
         apagar(lista)
      elif opcao == 13:
         inverter(lista)
      elif opcao == 14:
         ordem_crescente(lista)
      elif opcao == 0:  # sair do while
         break
      else:
         print('Opção Inválida')
