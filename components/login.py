from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = 'vertical'
        self.padding = 50

        self.add_widget(Label(text='Username'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label(text='Password'))
        self.password = TextInput(multiline=False, password=True)
        self.add_widget(self.password)

        self.submit_button = Button(text='Login')
        self.submit_button.bind(on_press=self.submit)
        self.add_widget(self.submit_button)

    def submit(self, instance):
        username = self.username.text
        password = self.password.text

        # Aqui você pode adicionar a lógica para autenticar o usuário e redirecioná-lo para o dashboard

class LoginApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    LoginApp().run()
