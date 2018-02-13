from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from jnius import autoclass
from kivy.properties import StringProperty

lang={'en':"press",'sk':"stlač"}

def java_lang():
    ac=autoclass('java.util.Locale')
    language=ac.getDefault().getLanguage() 
    return language
'''def android_lang():
    ac2=autoclass('android.content.res.Resources')
    str2=ac2.getSystem().getConfiguration().getLocales().get(0)
    return str2'''

app = App.get_running_app()
locale=java_lang()

class HelloApp(App):
    name=StringProperty('')
    def build(self):
        box=BoxLayout()
        button=Button()
        label=Label()
        if locale in lang:
            self.name=lang[locale]
        else:
            self.name=lang[locale]
        label.text=self.name
        ti=TextInput()
        box.add_widget(button)
        box.add_widget(label)
        box.add_widget(ti)
        return box
        
if __name__=='__main__':
    HelloApp().run()

