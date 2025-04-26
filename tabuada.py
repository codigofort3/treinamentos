numero = int(input("DFigite um Número para ver a tabuada: "))
contador = 1

while contador <=11:
    print(f"{numero} x {contador} = {numero * contador}")

    contador +=1


"""Esse código é um programa em Python que exibe a tabuada de um número digitado pelo usuário. Vamos quebrar e entender cada parte:

📝 Explicação do Código:
python
Copiar
Editar
numero = int(input("Digite um Número para ver a tabuada: "))
O programa pede ao usuário para digitar um número.

O input() recebe esse valor como string, e int() converte para um número inteiro.

python
Copiar
Editar
contador = 1
A variável contador é inicializada com 1. Ela será usada para contar de 1 a 10 na tabuada.

python
Copiar
Editar
while contador <= 10:
Esse é um loop while, que executa o bloco de código repetidamente enquanto a condição contador <= 10 for verdadeira.

python
Copiar
Editar
print(f"{numero} x {contador} = {numero * contador}")
Esse comando exibe a multiplicação do número digitado (numero) pelo contador, formatando a saída no modelo "N × X = Resultado".

O f"" é uma f-string, que permite inserir variáveis diretamente na string.

python
Copiar
Editar
contador += 1
A cada repetição do loop, o contador é incrementado em 1 (contador = contador + 1).

Quando contador chega a 11, a condição contador <= 10 se torna falsa, e o loop para.

🔹 Exemplo de Execução:
Se o usuário digitar 5, a saída será:

css
Copiar
Editar
Digite um Número para ver a tabuada: 5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
🔹 Esse é um código simples para gerar a tabuada de qualquer número digitado pelo usuário! 🚀"""    