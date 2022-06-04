import os
os.system('CLS')

# برنامه ای بنویسید که یک فایل متنی باز کرده و یک لیستی از کلمات اون متن نمایش بده
# کلمات میتونن با کاربر های فاصله, کاما, ادساین و نقطه از هم جدا بشن.

myFile = open('myfile.txt', 'r').read()
my_words_list = myFile.replace('.', ' ').replace('-', ' ').replace(',', ' ').replace('\n', ' ').split()
print(my_words_list)
