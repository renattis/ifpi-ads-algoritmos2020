n = int(input('Digite um número inteiro de 1 a 7:  '))


#Fichas com os dados finais
mais_gordo = 0
nome_m_gordo = ''
id_m_gordo = 0

mais_magro = 800
nome_m_magro = ''
id_m_magro = 0

for numero in range(1, n + 1):


   #Gera os dados das fichas
   random_id = random.randint(10000, 100000)
   random_peso = random.randint(350, 700)

   random_nome = random.randint(1, n)
   lista_nomes = ['celsinho', 'valente', 'galopante', 'um chifre',
                  'baguela', 'matador', 'gordinho', 'Rei do pasto']
   selecionar_nome = lista_nomes[numero-1]

   #Compara e coloca os dados gerados nas fichas finais
   if random_peso > mais_gordo:
      mais_gordo = random_peso
      nome_m_gordo = selecionar_nome
      id_m_gordo = random_id

   if random_peso < mais_magro:
      mais_magro = random_peso
      nome_m_magro = selecionar_nome
      id_m_magro = random_id

#mostra as fichas finais
print('\n')

print('MAIS MAGRO:')
print(f'Número de identificação: {id_m_magro}/{mais_magro}')
print(f'Peso: {mais_magro} kg')
print(f'Nome do boi: {nome_m_magro}')

print('\n')

print('MAIS GORDO')
print(f'Número de identificação: {id_m_gordo}/{mais_gordo}')
print(f'Peso: {mais_gordo} kg')
print(f'Nome do boi: {nome_m_gordo}')
