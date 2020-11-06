from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database import DataBase
from search import Search



class CreateAccountWindow(Screen):
    user_name = ObjectProperty(None)
    user_pass = ObjectProperty(None)

    def submit(self):
        if self.user_name.text != "" and self.user_pass != "":      
            if db.add_user(self.user_name.text, self.user_pass.text) == 1 : 
                self.reset()
                sm.current = "login" 
            else:
                userFound()                       
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.user_name.text = ""
        self.user_pass.text = ""

class LoginWindow(Screen):
    user_name = ObjectProperty(None)
    user_pass = ObjectProperty(None)

    def loginBtn(self):
        if db.validate(self.user_name.text, self.user_pass.text):
            self.reset()
            sm.current = "main"
        else:
            invalidLogin()

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.user_name.text = ""
        self.user_pass.text = ""


class MainWindow(Screen):
    soal = ObjectProperty(None)
    keshvar = ObjectProperty(None)

    def logOut(self):
        sm.current = "login"

    def serachBtn(self):
        if self.soal.text != "":
            if ser.validate(self.soal.text) != '':                
                self.keshvar.text = ser.validate(self.soal.text)
            else:
                self.keshvar.text = "Not Found"
        else:
            invalidForm()
    
class WindowManager(ScreenManager):
    pass

def invalidLogin():
    pop = Popup(title='Invalid Login',
                  content=Label(text='Invalid username or password.'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()

def userFound():
    pop = Popup(title='Invalid Username',
                  content=Label(text='UserName exists already.'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()

def invalidForm():
    pop = Popup(title='Invalid Form',
                  content=Label(text='Please fill in all inputs with valid information.'),
                  size_hint=(None, None), size=(400, 400))

    pop.open()



kv = Builder.load_file("windows.kv")

db = DataBase("user.json")
ser = Search("countries.txt")

sm = WindowManager()


screens = [CreateAccountWindow(name="create"), LoginWindow(name="login"), MainWindow(name="main")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "create"


class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()