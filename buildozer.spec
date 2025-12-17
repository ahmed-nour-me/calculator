[app]

# عنوان التطبيق
title = الحاسبة البسيطة

# اسم الحزمة (يجب أن يكون فريداً)
package.name = simplecalculator

# اسم المجال
package.domain = org.example

# إصدار التطبيق
version = 1.0

# مصادر التطبيق
source.dir = .

# الملف الرئيسي للتطبيق
source.main = calculator.py

# إصدار Android SDK (محدث)
android.sdk = 31
android.minapi = 21
android.ndk = 25b

# استخدام android.archs بدلاً من android.arch
android.archs = arm64-v8a, armeabi-v7a

# أذونات Android
android.permissions = INTERNET

# ميزات Android
android.features = 

# أيقونة التطبيق
# icon.filename = icon.png

# شاشة التحميل
# presplash.filename = presplash.png

# التوجه
orientation = portrait

# المفاتيح الكاملة
fullscreen = 0

# حزم التضمين
requirements = python3==3.9.13, kivy==2.1.0

# مكتبات Python الإضافية
p4a.branch = develop

# إعدادات Python
python.version = 3.9

# نوع البناء (تغيير من debug إلى release)
# build.type = release

# تكوينات إضافية
log_level = 2

# حجم الذاكرة
android.add_libs_armeabi_v7a = 
android.add_libs_arm64_v8a = 
android.add_libs_x86 = 
android.add_libs_x86_64 = 

# أوامر البناء
# build.args.release = --window

# حفظ مساحة البناء
build.keep_build_of_armeabi_v7a = False
build.keep_build_of_arm64_v8a = True
