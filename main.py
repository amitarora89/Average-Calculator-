from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

# Yellow Background
Window.clearcolor = (1, 1, 0, 1)

class AverageLayout(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.inputs = []

        # Jai Shri Krishna
        self.add_widget(Label(
            text="Jai Shri Krishna",
            font_size=64,
            color=(0.5, 0, 0, 1),
            size_hint=(1, None),
            height=70,
            pos_hint={"center_x": 0.5, "top": 0.99}
        ))

        # Average Calculator Title
        self.add_widget(Label(
            text="Average Calculator",
            font_size=56,
            bold=True,
            color=(0.2, 0, 0.5, 1),
            size_hint=(1, None),
            height=60,
            pos_hint={"center_x": 0.5, "top": 0.925}
        ))

        # Input Boxes
        top_pos = 0.85
        for i in range(6):
            ti = TextInput(
                font_size=56,
                multiline=False,
                input_filter='float',
                foreground_color=(0.5, 0, 0, 1),
                size_hint=(0.9, None),
                height=100,
                pos_hint={"center_x": 0.5, "top": top_pos}
            )
            ti.bind(text=self.calculate_average)
            ti.bind(on_text_validate=self.move_focus_next)
            self.inputs.append(ti)
            self.add_widget(ti)
            top_pos -= 0.11

        # Result Label (Average)
        self.result_label = Label(
            text="Average: 0.0",
            font_size=60,
            bold=True,
            color=(0, 0, 0.6, 1),
            size_hint=(0.9, None),
            height=80,
            pos_hint={"center_x": 0.5, "top": top_pos - 0.02}
        )
        self.add_widget(self.result_label)

        # ✅ Updated Clear All Button – bigger, higher, better
        clear_btn = Button(
            text="CLEAR ALL",
            font_size=52,  # Bigger font
            bold=True,
            background_color=(1, 0.4, 0.1, 1),  # Orange
            color=(1, 1, 1, 1),  # White text
            size_hint=(0.6, None),
            height=140,  # DOUBLE height
            pos_hint={"center_x": 0.5, "top": top_pos - 0.10}  # Higher on screen
        )
        clear_btn.bind(on_press=self.clear_all_inputs)
        self.add_widget(clear_btn)

    def calculate_average(self, instance, value):
        total = 0
        count = 0
        for box in self.inputs:
            text = box.text.strip()
            if text:
                try:
                    num = float(text)
                    total += num
                    count += 1
                except:
                    pass
        avg = total / count if count else 0
        self.result_label.text = f"Average: {round(avg, 2)}"

    def move_focus_next(self, instance):
        try:
            idx = self.inputs.index(instance)
            if idx < len(self.inputs) - 1:
                self.inputs[idx + 1].focus = True
        except:
            pass

    def clear_all_inputs(self, instance):
        for box in self.inputs:
            box.text = ""
        self.result_label.text = "Average: 0.0"

class AverageApp(App):
    def build(self):
        return AverageLayout()

AverageApp().run()
