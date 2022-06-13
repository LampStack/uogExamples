import os
os.system('CLS')

# برنامه ای بنویسید که محتوای یک فایل متنی را خوانده و خطوطی که
#  حرف کلمه اول آنها حرف بزرگ است را در فایلی جدید ذخیره کند

with open('./1.txt', 'r') as my_file:
    content = my_file.read()

new_file = open('./2.txt', 'a')

for line in content.split('\n'):
    if line[0].islower():
        new_file.write(line + '\n')
new_file.close()
