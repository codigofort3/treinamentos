#contando de 1 a 10

"""contador  = 1 # Define a variável 'contador' com o valor inicial 1

while contador <= 50: # Enquanto 'contador' for menor ou igual a 10, o loop continua
    print(f"Número: {contador}")# Imprime o valor atual de 'contador' na tela
    contador += 1# Incrementa 'contador' em 1 a cada repetição"""


#Somando números até que o usuário digite 0:


"""
soma = 0  # Inicializa a variável 'soma' com 0 para armazenar a soma dos números digitados

while True: # Inicia um loop infinito (ele só para quando encontrar um 'break')
    numero = int(input("Digite um número (0 para sair):"))# Pede um número ao usuário e converte para inteiro

    if numero == 0:  # Verifica se o número digitado é 0
        break # Se for 0, interrompe o loop
    soma += numero  # Se não for 0, adiciona o número digitado à variável 'soma'

print(f"A soma dos números é : {soma}")    # Exibe a soma total dos números digitados"""



"""# Cálculo de Fatorial

#O programa pede ao usuário que digite um número O valor digitalizado é convertido para inteiro usando int().
numero = int(input("Digite um número para calcular o fatorial: ")) 

#fatorialcomeça em 1 (pois a multiplicação deve começar com 1).
#contadortambém começa em 1 (para começar a multiplicação do fatorial corretamente).
fatorial = 1
contador = 1

#Enquanto contadorfor menor ou igual ao numero:
#Multiplicar fatorialpelo contador( fatorial *= contador).
#Aumenta o contadorem 1 ( contador += 1).
#Isso faz com que fatorialacumule o produto de todos os números de 1até numero.
while contador <= numero:
    fatorial *= contador
    contador += 1

    print(f"O fatorial de {numero} é {fatorial}")


numero = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1
contador = 1

while contador <= numero:
    fatorial *= contador
    contador += 1

print(f"O fatorial de {numero} é {fatorial}")"""

#TABUADA COM WHILE

numero = int(input("Digite um número para ver a tabuada: "))

contador = 1

while contador <= 10:
    print(f"{numero} x {contador}  = {numero * contador}")
    contador += 1
