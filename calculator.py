import os
os.environ['KIVY_NO_ARGS'] = '1'

from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'system')
Config.set('graphics', 'multisamples', '0')
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

Window.clearcolor = get_color_from_hex('#1e1e1e')

class CalculatorApp(App):
    def build(self):
        self.icon = 'icon.png' if os.path.exists('icon.png') else ''
        self.expression = ""
        
        main_layout = BoxLayout(orientation='vertical', padding=15, spacing=15)
        
        # شاشة العرض
        self.display = TextInput(
            text='0',
            multiline=False,
            readonly=True,
            font_size=45,
            halign='right',
            background_color=get_color_from_hex('#2d2d2d'),
            foreground_color=get_color_from_hex('#ffffff'),
            cursor_color=get_color_from_hex('#ffffff'),
            padding=[20, 20],
            size_hint=(1, 0.25)
        )
        main_layout.add_widget(self.display)
        
        # لوحة الأزرار
        buttons_layout = GridLayout(cols=4, spacing=10, size_hint=(1, 0.75))
        
        # تعريف الأزرار
        buttons = [
            ('C', self.clear, '#ff6b6b'),
            ('⌫', self.backspace, '#ffa726'),
            ('(', self.add_char, '#5c6bc0'),
            (')', self.add_char, '#5c6bc0'),
            ('7', self.add_char, '#424242'),
            ('8', self.add_char, '#424242'),
            ('9', self.add_char, '#424242'),
            ('÷', self.add_char, '#5c6bc0'),
            ('4', self.add_char, '#424242'),
            ('5', self.add_char, '#424242'),
            ('6', self.add_char, '#424242'),
            ('×', self.add_char, '#5c6bc0'),
            ('1', self.add_char, '#424242'),
            ('2', self.add_char, '#424242'),
            ('3', self.add_char, '#424242'),
            ('-', self.add_char, '#5c6bc0'),
            ('0', self.add_char, '#424242'),
            ('.', self.add_char, '#424242'),
            ('=', self.calculate, '#66bb6a'),
            ('+', self.add_char, '#5c6bc0'),
        ]
        
        for text, callback, color in buttons:
            btn = Button(
                text=text,
                font_size=32,
                background_color=get_color_from_hex(color),
                background_normal='',
                size_hint=(1, 1),
                color=get_color_from_hex('#ffffff')
            )
            btn.bind(on_press=callback)
            buttons_layout.add_widget(btn)
        
        main_layout.add_widget(buttons_layout)
        return main_layout
    
    def add_char(self, instance):
        if self.display.text == '0' or self.display.text == 'خطأ':
            self.display.text = ''
        
        char = instance.text
        if char == '×':
            char = '*'
        elif char == '÷':
            char = '/'
        
        self.expression += char
        self.display.text = self.expression
    
    def clear(self, instance):
        self.expression = ""
        self.display.text = "0"
    
    def backspace(self, instance):
        if self.expression:
            self.expression = self.expression[:-1]
            self.display.text = self.expression if self.expression else "0"
    
    def calculate(self, instance):
        try:
            if not self.expression:
                return
            
            expr = self.expression.replace('×', '*').replace('÷', '/')
            result = eval(expr)
            
            # تقريب النتيجة إذا كانت عشرية
            if isinstance(result, float):
                if result.is_integer():
                    result = int(result)
                else:
                    result = round(result, 10)
            
            self.expression = str(result)
            self.display.text = self.expression
            
        except ZeroDivisionError:
            self.expression = ""
            self.display.text = "لا يمكن القسمة على صفر"
            
        except Exception as e:
            self.expression = ""
            self.display.text = "خطأ في العملية"

if __name__ == '__main__':
    CalculatorApp().run()
