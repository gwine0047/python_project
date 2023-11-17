import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup


class RegistrationApp(App):
    def build(self):
        self.title = "Registration form"
        self.names = []
        layout = BoxLayout(orientation='vertical', padding=30, spacing=10)

        head_label = Label(text="GLOBAL HARVEST CHURCH, MAGBORO", font_size=26, bold=True, height=40)
        subhead_label = Label(text="School Of Discipleship", font_size=20, height=40)

        #adding labels
        name_label = Label(text="Name: ", font_size=18)
        self.name_input = TextInput(multiline=False, font_size=18)

        email_label= Label(text="Email: ", font_size=18)
        self.email_input = TextInput(multiline=False, font_size=18)

        password_label = Label(text="Password: ", font_size=18)
        self.password_input = TextInput(multiline=False, font_size=18, password=True)

        confirmpassword_label = Label(text="confirm Password: ", font_size=18)
        self.confirmpassword_input = TextInput(multiline=False, font_size=18, password=True)

        # button
        submit_btn = Button(text="Register", font_size=18, on_press=self.register)
        
        layout.add_widget(head_label)
        layout.add_widget(subhead_label)
        layout.add_widget(name_label)
        layout.add_widget(self.name_input)
        layout.add_widget(email_label)
        layout.add_widget(self.email_input)
        layout.add_widget(password_label)
        layout.add_widget(self.password_input)
        layout.add_widget(confirmpassword_label)
        layout.add_widget(self.confirmpassword_input)
        layout.add_widget(submit_btn)

        return layout

    def register(self, instance):
        #Collecting data
        name = self.name_input.text
        email = self.email_input.text
        password = self.password_input.text
        confirmpassword = self.confirmpassword_input.text

        # validation
        if name.strip() == '' or email.strip() == '' or password.strip() == '' or confirmpassword.strip() == '':
            message = "Please fill in all fields"
        elif password != confirmpassword:
            message = "Passwords do not match."

        else:
            self.names.append(name)
            with open("school.txt", 'a') as file:
                file.write("Name: {}\n".format(name))
                file.write("Email: {}\n".format(email))
            message = "Registration Successful!\nName: {}\nEmail: {}".format(name, email)
            print(self.names)
    
        # pop up function
        popup = Popup(title = 'Registration Status', content = Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()
if __name__ == "__main__":
    RegistrationApp().run()