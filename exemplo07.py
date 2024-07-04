import os

os.system("cls")

print("Exibindo um Intervalo de Número")

# 1 Entrada
inicio = int(input("Digite o Inicio do Intervalo: "))
fim = int(input("Digite o Fim do Intervalo: "))

if inicio < fim:
  while inicio <= fim:
    print("Número: ", inicio)
    inicio = inicio + 1
  else:
     input("Pressione <ENTER> para emcerrar...")
else: 
  while fim <= inicio:
    print("Número: ", fim)
    fim = fim + 1

input("Presssione <ENTER> para encerrar..")