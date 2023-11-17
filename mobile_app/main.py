from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        self.icon = "calc2.jpg"
        self.operators = ["/", "-", "+", "*"]
        self.last_was_operator = None
        self.last_button = None

        main_layout = BoxLayout(orientation = "vertical")
        self.solution = TextInput(background_color = "black", foreground_color = "white", 
                                multiline=False, halign="right", font_size=55,readonly=True)

        main_layout.add_widget(self.solution)
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "+"],
            [".", "0", "C", "-"]
        ]

        # create an h_layout for each row
        for row in buttons:
            h_layout = BoxLayout()
        # create a button for each label
            for label in row:
                button = Button(
                    text = label, font_size = 30, background_color="grey", pos_hint={"certain_x":0.5, "certain_y":0.5}
                )
                button.bind(on_press=self.on_button_press)
                # insert button into the h_layout
                h_layout.add_widget(button)
                # add h_layout to main_layout
            main_layout.add_widget(h_layout)
        
        equal_btn = Button(
                    text = "=", font_size = 30, background_color="grey", pos_hint={"certain_x":0.5, "certain_y":0.5}
        )
        equal_btn.bind(on_press=self.on_solution)
        # add equal_btn to main_layout
        main_layout.add_widget(equal_btn)

        return main_layout
    
    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == 'C':
            self.solution.text = ""
        else:
            # if an operator is on screen and another is typed, just return
            if current and (
                self.last_was_operator and button_text in self.operators):
                return
            # if screen is blank and operator is first typed, just return
            elif current == "" and button_text in self.operators:
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators
        #  equal button solution, on hitting the sign, display the sign the carry out an eval and return it to solution as str, then display it
    def on_solution(self, instance):
        text = self.solution.text
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution


if __name__ == "__main__":
    app = MainApp()
    app.run()