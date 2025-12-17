from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.widget import Widget
import math

Window.clearcolor = (0.1, 0.1, 0.1, 1)

class CalculatorApp(App):
    def build(self):
        self.title = "حاسبة بسيطة"
        self.icon = "icon.png"  # أضف ملف أيقونة إذا أردت
        return CalculatorWidget()

class CalculatorWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(CalculatorWidget, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10
        self.padding = [10, 10, 10, 10]
        
        # شاشة العرض
        self.display = Label(
            text="0",
            font_size=48,
            halign='right',
            valign='middle',
            size_hint=(1, 0.3),
            color=(1, 1, 1, 1),
            text_size=(Window.width - 20, None)
        )
        self.display.bind(size=self.display.setter('text_size'))
        self.add_widget(self.display)
        
        # لوحة المفاتيح
        buttons_layout = GridLayout(cols=4, spacing=5, size_hint=(1, 0.7))
        
        # تعريف الأزرار
        buttons = [
            ('C', self.clear), ('⌫', self.backspace), ('%', self.percent), ('/', self.operation),
            ('7', self.number), ('8', self.number), ('9', self.number), ('×', self.operation),
            ('4', self.number), ('5', self.number), ('6', self.number), ('-', self.operation),
            ('1', self.number), ('2', self.number), ('3', self.number), ('+', self.operation),
            ('.', self.decimal), ('0', self.number), ('±', self.negate), ('=', self.calculate)
        ]
        
        # إنشاء الأزرار وإضافتها
        for text, callback in buttons:
            btn = Button(
                text=text,
                font_size=28,
                background_color=self.get_button_color(text),
                color=(1, 1, 1, 1)
            )
            btn.bind(on_press=callback)
            buttons_layout.add_widget(btn)
        
        self.add_widget(buttons_layout)
        
        # متغيرات الحاسبة
        self.current = "0"
        self.previous = ""
        self.operation = None
        self.new_input = True
    
    def get_button_color(self, text):
        """إرجاع لون الزر بناءً على النص"""
        if text in ['C', '⌫']:
            return (0.8, 0.2, 0.2, 1)  # أحمر
        elif text in ['+', '-', '×', '/', '=', '%', '±']:
            return (0.2, 0.6, 0.8, 1)  # أزرق
        else:
            return (0.3, 0.3, 0.3, 1)  # رمادي
    
    def update_display(self):
        """تحديث شاشة العرض"""
        self.display.text = self.current
    
    def number(self, instance):
        """معالجة الأرقام"""
        if self.new_input:
            self.current = instance.text
            self.new_input = False
        else:
            if self.current == "0":
                self.current = instance.text
            else:
                self.current += instance.text
        self.update_display()
    
    def decimal(self, instance):
        """إضافة الفاصلة العشرية"""
        if self.new_input:
            self.current = "0."
            self.new_input = False
        elif '.' not in self.current:
            self.current += '.'
        self.update_display()
    
    def operation(self, instance):
        """معالجة العمليات الحسابية"""
        if self.previous and not self.new_input:
            self.calculate(None)
        
        self.previous = self.current
        self.operation = instance.text
        self.new_input = True
    
    def calculate(self, instance):
        """تنفيذ العملية الحسابية"""
        if not self.previous or not self.operation:
            return
        
        try:
            prev = float(self.previous)
            curr = float(self.current)
            
            if self.operation == '+':
                result = prev + curr
            elif self.operation == '-':
                result = prev - curr
            elif self.operation == '×':
                result = prev * curr
            elif self.operation == '/':
                if curr == 0:
                    result = "خطأ: قسمة على صفر"
                else:
                    result = prev / curr
            elif self.operation == '%':
                result = prev % curr
            
            # تحويل النتيجة إلى سلسلة
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            
            self.current = str(result)
            self.previous = ""
            self.operation = None
            self.new_input = True
            
        except Exception as e:
            self.current = "خطأ"
            self.previous = ""
            self.operation = None
            self.new_input = True
        
        self.update_display()
    
    def clear(self, instance):
        """مسح الكل"""
        self.current = "0"
        self.previous = ""
        self.operation = None
        self.new_input = True
        self.update_display()
    
    def backspace(self, instance):
        """حذف آخر رقم"""
        if len(self.current) > 1:
            self.current = self.current[:-1]
        else:
            self.current = "0"
        self.update_display()
    
    def percent(self, instance):
        """حساب النسبة المئوية"""
        try:
            value = float(self.current)
            self.current = str(value / 100)
            self.new_input = True
            self.update_display()
        except:
            self.current = "خطأ"
            self.update_display()
    
    def negate(self, instance):
        """تغيير الإشارة"""
        try:
            value = float(self.current)
            self.current = str(-value)
            if self.new_input:
                self.previous = self.current
            self.update_display()
        except:
            self.current = "خطأ"
            self.update_display()

if __name__ == '__main__':
    CalculatorApp().run()
