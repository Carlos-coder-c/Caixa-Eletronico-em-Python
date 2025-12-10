# Desafio do dia: Fazer um caixa eletronico, Sacar valores, calcular cedulas, Validar entradas e Mostrar saques anteriores...
TAXA = {
  "taxa-banco": 0.10
}

def sacar_valores(sacar_quantidade, taxa_banco):
  return sacar_quantidade * (1 - taxa_banco)

def calcular_cedulas(valor):
  notas = [200, 100, 50, 20, 10, 5, 2]
  resultado = {}
  
  for nota in notas:
    quantidade = valor // nota
    if quantidade > 0:
     resultado[nota] = quantidade
     valor %= nota
    
  return resultado

def validar_entradas():
  while True:
   valor = input('Digite o valor:')
   if valor.isdigit():
     return int(valor)
  
   print("Digite apenas numeros")
  
    
def ver_saques(lista):
  print('\nLista de saques: ')
  for indice, valor in enumerate(lista, start=1):
   print(f'{indice}. R$ {valor}')
   
   
saques = []
while True:
 print('----Seja bem vindo ao Caixa Eletronico XS----')
 print('1. Sacar Dinheiro')
 print('2. Calcular Cedulas')
 print('3. Ver Saques')

 escolha = int(input("Escolha uma Opção: "))
 if escolha == 1:
   valor = validar_entradas()
   recebido = sacar_valores(valor, TAXA['taxa-banco'])
   saques.append(recebido)
   print(f'Você sacou R${recebido}, diminuiu 10% por conta da taxa do banco👍 ')
  
 elif escolha == 2:
  valor = validar_entradas()
  cedulas = calcular_cedulas(valor)
  for nota, quantidade in cedulas.items():
   print(f'{quantidade} de {nota}')

 elif escolha == 3:
  ver_saques(saques)
  break
 
   
   
