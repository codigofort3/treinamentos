soma = 0
while True:
    numero = int(input("Digite um número. (Negativo para sair): "))
    if numero < 0 :
        break
    soma += numero
print(f" A soma dos número é : {soma}")
