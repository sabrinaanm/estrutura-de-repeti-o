import os

os.system("cls")

print("Exemplo de While com texto")

resposta = input("Deseja calcular a soma de dois números/ (sim) ou (nao):").lower()

while resposta != "sim":
 print("==================================")
 print("Calculando a SOMA dos dois números")
 print("===================================") 

 # 1 Entrada
 v1 = int(input("Digite um número: "))
 v2 = int(input("Digite outro múmero: "))

 # 2 Processamento
 resultado = v1 + v2

 # 3 Saida
 print("O resultado é: ", resultado)

 resposta = input("Digite (sim) para reiniciar, e (nao) para encerrar!").lower()
else:
 input("Pressione <ENTER> para encerrar o programa....")