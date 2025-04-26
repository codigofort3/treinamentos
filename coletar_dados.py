# Coletar dados do usuário.

"""nome = input("Qual o seu nome ? :")
print(f"Olá {nome}, é um prazer te conhecer!")

idade = int(input("Qual a sua idade: "))
print(f"Ah que legal{nome} ,você é bastante novo!")

cidade = input("Em qual cidade você mora? :")
print(f"Ótimo, e em qual estado fica {cidade}? :")

estado = input("Qual o estado que você mora? :")
print(f'Tudo bem então {cidade} fica localizada no estado do {estado}')

cidade = input("E em qual cidade você mora? : ")
print(
    f"Certo, então você se chama {nome} e tem {idade} anos de idade e mora em {cidade} que fica no {estado}")"""

"""nome  = input("Qual o seu nome? : ")
idade = input("Qual a sua idade? : ")
print(f"Olá {nome}, você tem {idade} anos de idade.")
"""

# Transformando entrada em número
# Converter a entrada do usuário em um número inteiro com int()

"""numero = int(input("Digite um número: "))
print(f"O dobro de {numero} é {numero * 2}.")"""

# Coletando múltiplos dados
# Objetivo: Receber mais de uma informação e realizar cálculos.

"""nome  = input("Qual o seu nome? : ")
altura = float(input("Qual sua altura em metros? : "))
peso = float(input("Qual o seu peso em kg? : "))
imc = peso / (altura ** 2)
print(f"{nome}, o seu imc é {imc:.2f}.")"""

# Confirmando decisões com entrada
# Objetivo: Processar a resposta do usuário e reagir de acordo.

"""resposta = input("Você gosta de programar em python ? (sim/não):").lower()
if resposta == "sim":
    print("Que ótimo! Python é incrível.")

else:
    print("Ah, que pena . Espero que mude de idéia com o tempo.")"""

# Criando um pequeno questionário
# Objetivo: Praticar lógica condicional e incrementar variáveis.

"""print("Bem vindo ao quiz!")
pontos = 0

pergunta1 = input("Qual a capital do Brasil? : ").lower()
if pergunta1 == "brasilia":
    pontos += 1

pergunta2 = input("Quanto é 2 + 2? : ")
if pergunta2 == "4":
    pontos += 1

print(f"Você acertoui {pontos} perguta(s)")
"""

# Verificar se um número é positivo, negativo ou zero
"""numero = int(input("Digite um número : "))
if numero > 0:
    print("O número é positivo.")

elif numero < 0:
    print("O número é negativo.")

else:
    print("O número é zero.")"""

# Classificar a idade
# Crie um programa que classifica uma pessoa com base na idade que ela informar.

"""idade = int(input("Digite sua idade: "))
if idade < 12:
    print("Você é uma criança.")
elif 12 <= idade <= 17:
    print("Você é um adolescente.")
elif 18 <= idade <= 60:
    print("Você é um adulto")
else:
    print("Você é um idoso.")"""

# Calcular nota final
# Escreva um programa que aceita a nota de um aluno e informa se ele foi aprovado, ficou de recuperação ou foi reprovado.

"""nota = float(input("Digita a sua nota: "))
if nota >= 7.0:
    print("Parabéns vocÊ foi aprovado.")

elif 5.0 <= nota < 7.0:
    print("Você está de recuperação.")

else:
    print("Você está reprovado.")"""

# Calcular desconto em uma compra
# Implemente um programa que aplique descontos baseados no valor de uma compra.

"""valor_da_compra = float(input("Qual o valor da compra?: "))
if valor_da_compra > 1000:
    desconto = 0.15

elif 500 <= valor_da_compra <= 1000:
    desconto = 0.10

else:
    desconto = 0.5

valor_final = valor_da_compra - (valor_da_compra * desconto)
print(    f"Você recebeu um desconto  de {desconto * 100}%. Sua compra saiu por R${valor_final:.2f}.")"""

# Número par ou ímpar
# Escreva um programa que verifica se um número digitado pelo usuário é par ou ímpar.

"""numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print("O número é par. ")
else:
    print("O número é impar. ")
"""

# mprimir números de 1 a 10 usando um loop
# Objetivo: Pratique iterar sobre uma sequência de números usando range.

# for i in range(1, 100):
#    print(i)

# Soma dos números de 1 a N
# Objetivo: Usar um loop para somar números sequencialmente.

"""n = int(input("Digite um número: "))
soma = 0
for i in range(1, n + 1):
    soma += i
    print("A soma dos números de 1 a {n} é {soma}.")"""

# Imprimir os elementos de uma lista
# Objetivo: Iterar sobre os elementos de uma lista e trabalhar com estruturas iteráveis.

"""frutas = ["maçã", "banana", "laranja", "uva"]
for fruta in frutas:
    print(fruta)
"""

# Verificar números pares em um intervalo
# Objetivo: Combinar o uso de loops e condicionais.

"""inicio = int(input("Digite o inicio do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

for numero in range(inicio, fim + 1):
    if numero % 2 == 0:
        print(f"{numero} é par. ")
"""

# Loop while para adivinhar um número
# Objetivo: Praticar o loop while para criar um jogo interativo.

"""numero_secreto = 55
tentativa = -1

print("Adivinhe o número secreto! (entre 1 e 100) ")

while tentativa != numero_secreto:
    tentativa = int(input("Digite sua tentativa: "))
    if tentativa < numero_secreto:
        print("Muito baixo.")

    elif tentativa > numero_secreto:
        print("Muito alto. ")

print("Parabéns ,você acertou. ")
"""

"""while True:
    mensagem = input("Digite algo (ou 'sair' para encerrar): ")
    if mensagem.lower() == "sair":
        print("Encerrando o bot. Até mais!")
        break
    else:
        print(f"Bot: Você disse '{mensagem}'!")
"""
"""
def calculadora():
    print("Bem-vindo à Calculadora Simples!")
    print("Selecione a operação desejada:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    
    while True:
        opcao = input("Escolha uma opção (1/2/3/4) ou 'sair' para encerrar: ")
        
        if opcao.lower() == 'sair':
            print("Encerrando a calculadora. Até mais!")
            break

        if opcao in ('1', '2', '3', '4'):
            try:
                numero1 = float(input("Digite o primeiro número: "))
                numero2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Por favor, insira números válidos!")
                continue

            if opcao == '1':
                print(f"O resultado é: {numero1 + numero2}")
            elif opcao == '2':
                print(f"O resultado é: {numero1 - numero2}")
            elif opcao == '3':
                print(f"O resultado é: {numero1 * numero2}")
            elif opcao == '4':
                if numero2 != 0:
                    print(f"O resultado é: {numero1 / numero2}")
                else:
                    print("Erro: Divisão por zero não é permitida.")
        else:
            print("Opção inválida. Tente novamente.")
        
        print()

# Chamando a função
calculadora()"""

"""#Usando biblioteca TKinter
import tkinter as tk
from tkinter import messagebox

def calcular():
    operacao = operacao_var.get()
    try:
        numero1 = float(entry_numero1.get())
        numero2 = float(entry_numero2.get())
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos!")
        return

    if operacao == "Adição":
        resultado = numero1 + numero2
    elif operacao == "Subtração":
        resultado = numero1 - numero2
    elif operacao == "Multiplicação":
        resultado = numero1 * numero2
    elif operacao == "Divisão":
        if numero2 != 0:
            resultado = numero1 / numero2
        else:
            messagebox.showerror("Erro", "Divisão por zero não é permitida.")
            return
    else:
        messagebox.showerror("Erro", "Selecione uma operação válida.")
        return

    label_resultado.config(text=f"Resultado: {resultado}")

# Criação da janela principal
janela = tk.Tk()
janela.title("Calculadora Simples")

# Entrada do primeiro número
tk.Label(janela, text="Primeiro número:").pack()
entry_numero1 = tk.Entry(janela)
entry_numero1.pack()

# Entrada do segundo número
tk.Label(janela, text="Segundo número:").pack()
entry_numero2 = tk.Entry(janela)
entry_numero2.pack()

# Seleção da operação
tk.Label(janela, text="Selecione a operação:").pack()
operacao_var = tk.StringVar()
tk.OptionMenu(janela, operacao_var, "Adição", "Subtração", "Multiplicação", "Divisão").pack()

# Botão para calcular
tk.Button(janela, text="Calcular", command=calcular).pack()

# Exibição do resultado
label_resultado = tk.Label(janela, text="Resultado: ")
label_resultado.pack()

# Executar o loop principal da interface gráfica
janela.mainloop()
"""

