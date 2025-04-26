"""from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QComboBox, QMessageBox


class Calculadora(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora Moderna")
        self.setGeometry(300, 300, 400, 200)

        # Layout principal
        container = QWidget()
        layout = QVBoxLayout()

        # Entrada de números
        self.label1 = QLabel("Primeiro número:")
        layout.addWidget(self.label1)
        self.input1 = QLineEdit()
        layout.addWidget(self.input1)

        self.label2 = QLabel("Segundo número:")
        layout.addWidget(self.label2)
        self.input2 = QLineEdit()
        layout.addWidget(self.input2)

        # Operação
        self.label_op = QLabel("Selecione a operação:")
        layout.addWidget(self.label_op)
        self.operacao = QComboBox()
        self.operacao.addItems(
            ["Adição", "Subtração", "Multiplicação", "Divisão"])
        layout.addWidget(self.operacao)

        # Botão para calcular
        self.calcular = QPushButton("Calcular")
        self.calcular.clicked.connect(self.realizar_calculo)
        layout.addWidget(self.calcular)

        # Exibição do resultado
        self.resultado = QLabel("Resultado: ")
        layout.addWidget(self.resultado)

        # Configurando o layout
        container.setLayout(layout)
        self.setCentralWidget(container)

    def realizar_calculo(self):
        try:
            numero1 = float(self.input1.text())
            numero2 = float(self.input2.text())
            operacao = self.operacao.currentText()

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
                    QMessageBox.critical(
                        self, "Erro", "Divisão por zero não é permitida!")
                    return
            self.resultado.setText(f"Resultado: {resultado}")
        except ValueError:
            QMessageBox.warning(
                self, "Erro", "Por favor, insira números válidos!")


# Executando a aplicação
if __name__ == "__main__":
    app = QApplication([])
    janela = Calculadora()
    janela.show()
    app.exec_()"""

"""
# Solicitar informações ao usuário
nome = input("Qual o seu nome? : ")
idade = input("Qual a sua idade? :")
hobby = input("Qual o seu hobby favorito? : ")

print(f"Olá {nome}, espero que esteja bem,é um prazer conhecê-lo.")
print(
    f"Fico muito feliz em saber que você goste de praticar {hobby},geralmente as peesoas aos {idade} anos, não gostam tanto.")
print(f"Continue fazendo aquilo que você gosta!")
"""


"""class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = input("Digite o nome do aluno(a):")
        self.matricula = input("Digite a matrícula do aluno: ")
        self.curso = input("Qual o curso do aluno? : ")

    def apresentar_aluno(self):
        print(f"Aluno: {self.nome}")
        print(f"Matrícula: {self.matricula}")
        print(f"Curso: {self.curso}")


# Criando um objeto Aluno
aluno1 = Aluno("Maria", "2023123456", "Engenharia")
aluno1.apresentar_aluno()
"""

# Método __init__


class contaBancaria:
    def __init__(self, titular, documento, saldo):
        self.titular = input("Qual o nome do titular da conta? :")
        if titular == jc:
            print("OLá JC,seja bem vindo.")
        else:
            print("Usuario incorreto.")

        self.documento = input("Qual documento cadastrado? :")
        self.saldo = saldo


# Método depositar

    def __init__(self, valor):
        self.saldo += valor
        print(
            f"Depósito de R$ {valor:.2f} realizado com sucesso. Saldo atual da sua conta é R$ {self.saldo:.2f}")


# Método sacar

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(
                f"Saque de R$ {valor:.2f} realizado com sucesso. O saldo atual: de sua conta é de R$ {self.saldo:.2f}")

        else:
            print("Saldo insuficiente.")

    # Criando conta e realizando operações

    conta1 = ContaBancaria("José", 5000.00)
    conta1.depositar(13.569, 36)
    conta1.sacar(9000)


"""
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso. Saldo atual: R$ {self.saldo:.2f}")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso. Saldo atual: R$ {self.saldo:.2f}")
        else:
            print("Saldo insuficiente!")

# Criando conta e realizando operações
conta1 = ContaBancaria("Zé", 1000.00)
conta1.depositar(500.00)
conta1.sacar(300.00)"""
