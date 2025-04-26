"""from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class MeuApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")
        label = Label(text="Olá José,seja bem-vindo ao meu app!")
        botao = Button(text="Clique aqui!")
        botao.bind(on_press=self.botao_clicado)
        layout.add_widget(label)
        layout.add_widget(botao)
        return layout

    def botao_clicado(self, instance):
        instance.text = "Você clicou!"


if __name__ == "__main__":
    MeuApp().run()
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MeuNovoApp(App):
    def build(self):
        # Layout principal
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        # Adicionando um rótulo
        self.label = Label(text="Digite algo abaixo:", font_size=24)
        layout.add_widget(self.label)

        # Caixa de entrada de texto
        self.text_input = TextInput(hint_text="Escreva aqui", multiline=False)
        layout.add_widget(self.text_input)

        # Botão para ação
        botao = Button(text="Clique para exibir!", size_hint=(1, 0.5))
        botao.bind(on_press=self.mostrar_texto)
        layout.add_widget(botao)

        return layout

    def mostrar_texto(self, instance):
        # Atualiza o texto do rótulo com o que foi digitado
        texto_digitado = self.text_input.text
        if texto_digitado.strip():
            self.label.text = f"Você digitou: {texto_digitado}"
        else:
            self.label.text = "Por favor, digite algo!"


if __name__ == '__main__':
    MeuNovoApp().run()
