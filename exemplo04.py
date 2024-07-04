import os

os.system("cls")

print("Exemplo de While utilizando continue")

i = 0

while i < 6:
    i = i + 1

    if i == 3: 
        continue
    
    print(i)