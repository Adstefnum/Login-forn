import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
import hashlib

class Design(Widget):
    name = ObjectProperty(None)
    email = ObjectProperty(None)
    surname = ObjectProperty(None)
    password = ObjectProperty(None)
       
    
    def pressed(self):
        kName = self.name.text
        kLast = self.surname.text
        kEmail = self.email.text
        hPassword = self.password.text.encode('utf-8')
        aPassword = hashlib.md5(hPassword.strip()).hexdigest()


        try:
            file = open("login.txt","a")
            file.write('\n\nName: '+ kName )
            file.write(', Lastname: '+ kLast )
            file.write(', Password: '+ aPassword)
            file.close()

        except:
            print('unable to write to server')

        try:
            file = open("EmailList.txt","a")
            file.write('\n'+kEmail)
            file.close()

        except:
            print('unable to write to server')


        self.name.text = ""
        self.surname.text = ""
        self.email.text = ""
        self.password.text = ""


class FloatLogin(App):
    def build(self):
        return Design()

FloatLogin().run()
