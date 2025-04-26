from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class ContadorApp(App):
    def build(self):
        self.contador = 0  # Inicializa o contador

        # Criando layout vertical
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Criando um rótulo (texto)
        self.label = Label(text="Contador: 0", font_size=40)

        # Criando um botão
        botao = Button(text="Clique para aumentar",
                       font_size=30, size_hint=(1, 0.5))
        botao.bind(on_press=self.incrementar)

        # Adicionando os elementos ao layout
        layout.add_widget(self.label)
        layout.add_widget(botao)

        return layout

    def incrementar(self, instance):
        """Aumenta o contador e atualiza o texto."""
        self.contador += 1
        self.label.text = f"Contador: {self.contador}"


# Executa o app
if __name__ == '__main__':
    ContadorApp().run()
