import os
from tkinter.tix import InputOnly
os.system('cls')

# تابعی تعریف کنید که تعدادی نام دانشجو دریافت و برعکس ترتیب ورودی نمایش دهد.

def check_prime(num):
    if num==1:
        return False
    elif num==2:
        return True
    else:
        for x in range(2, num):
            if num % x==0:
                return False
        return True

while True:
    num = int(input('> '))
    if check_prime(num) :
        print('AVAL')
    else:
        print('MORAKAB')
