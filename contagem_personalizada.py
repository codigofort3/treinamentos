inicio = int(input("Digite um número inicial: "))
fim = int(input("Digite um número final: "))

if fim > inicio:
    while inicio <= fim:
        print(inicio)
        inicio += 1
    
else:
    print("O número final deve ser maior que o número inicial.")
