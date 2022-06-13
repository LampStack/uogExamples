import os
os.system('CLS')

# برنامه ای بنوییسید که محتوای یک فایل تکست را خوانده
# و تمام اعداد آن فایل را با فاصله در یک فایل جدید ذخیره کند.

with open('./1.txt', 'r') as my_file:
    content = [x for x in list(set(my_file.read().replace('\n', ' ').split())) if x.isdigit()]

new_file = open('./2.txt', 'w')

new_file.write(' '.join(content))

new_file.close()
