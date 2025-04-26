soma = 0
quantidade = 0

while True:
    nota = float(input("Digite uma nota (-1 para encerrar):"))
    if nota == -1:
        break
    soma += nota
    quantidade += 1 
    
if quantidade > 0:
    media = soma / quantidade
    print(f"A média das notas é :{media:.2f}")

else:
    print("Nenhuma nota foi inserida.")