from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import json

class PersonalAI(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        
        self.label = Label(text="Mera AI Assistant", font_size='20sp')
        self.input_text = TextInput(hint_text="Aap kya chahte hain?", multiline=False)
        self.btn = Button(text="Bolo / Bhejo", on_press=self.process_command)
        
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.input_text)
        self.layout.add_widget(self.btn)
        
        return self.layout

    def process_command(self, instance):
        user_msg = self.input_text.text
        # Yahan aapka AI Memory aur Response logic aayega
        self.label.text = f"AI Javab: Aapne kaha '{user_msg}'"

if __name__ == '__main__':
    PersonalAI().run()
