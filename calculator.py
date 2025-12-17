import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget

# لون النافذة
Window.clearcolor = (0.1, 0.1, 0.1, 1)

class CalculatorApp(App):
    def build(self):
        self.title = "الحاسبة البسيطة"
        self.expression = ""
        
        # التصميم الرئيسي
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # شاشة العرض
        self.display = TextInput(
            text='',
            multiline=False,
            readonly=True,
            font_size=40,
            halign='right',
            background_color=(0.2, 0.2, 0.2, 1),
            foreground_color=(1, 1, 1, 1),
            cursor_color=(1, 1, 1, 1),
            padding=[20, 20]
        )
        main_layout.add_widget(self.display)
        
        # لوحة الأزرار
        buttons_layout = GridLayout(cols=4, spacing=10, size_hint=(1, 1))
        
        # قائمة الأزرار
        buttons = [
            ('C', self.clear_all),
            ('⌫', self.backspace),
            ('(', self.add_to_expression),
            (')', self.add_to_expression),
            ('7', self.add_to_expression),
            ('8', self.add_to_expression),
            ('9', self.add_to_expression),
            ('÷', self.add_to_expression),
            ('4', self.add_to_expression),
            ('5', self.add_to_expression),
            ('6', self.add_to_expression),
            ('×', self.add_to_expression),
            ('1', self.add_to_expression),
            ('2', self.add_to_expression),
            ('3', self.add_to_expression),
            ('-', self.add_to_expression),
            ('0', self.add_to_expression),
            ('.', self.add_to_expression),
            ('=', self.calculate),
            ('+', self.add_to_expression),
        ]
        
        # إنشاء الأزرار
        for text, callback in buttons:
            btn = Button(
                text=text,
                font_size=30,
                background_color=self.get_button_color(text),
                background_normal=''
            )
            btn.bind(on_press=callback)
            buttons_layout.add_widget(btn)
        
        main_layout.add_widget(buttons_layout)
        
        return main_layout
    
    def get_button_color(self, text):
        """إرجاع لون الزر بناءً على نوعه"""
        if text in ['C', '⌫']:
            return (0.9, 0.3, 0.3, 1)  # أحمر
        elif text == '=':
            return (0.2, 0.6, 0.2, 1)  # أخضر
        elif text in ['+', '-', '×', '÷']:
            return (0.3, 0.5, 0.8, 1)  # أزرق
        else:
            return (0.4, 0.4, 0.4, 1)  # رمادي
    
    def add_to_expression(self, instance):
        """إضافة رمز إلى التعبير"""
        if self.expression == "خطأ":
            self.expression = ""
        
        text = instance.text
        
        # استبدال الرموز للعمليات الرياضية
        if text == '×':
            text = '*'
        elif text == '÷':
            text = '/'
        
        self.expression += text
        self.display.text = self.expression
    
    def clear_all(self, instance):
        """مسح كل شيء"""
        self.expression = ""
        self.display.text = ""
    
    def backspace(self, instance):
        """حذف آخر رمز"""
        if self.expression == "خطأ":
            self.expression = ""
        elif self.expression:
            self.expression = self.expression[:-1]
            self.display.text = self.expression
    
    def calculate(self, instance):
        """حساب النتيجة"""
        try:
            if not self.expression:
                return
            
            # تنظيف التعبير واستبدال الرموز
            expr = self.expression.replace('×', '*').replace('÷', '/')
            
            # الحساب الآمن
            result = str(eval(expr))
            self.expression = result
            self.display.text = result
            
        except ZeroDivisionError:
            self.expression = "خطأ: قسمة على صفر"
            self.display.text = self.expression
            
        except Exception as e:
            self.expression = "خطأ"
            self.display.text = self.expression

if __name__ == '__main__':
    CalculatorApp().run()
