import os
os.system('cls')

# کلاسی طراحی کنید که تعداد عدد از کاربر دریافت کرده و متود های
# محاسبه میانگین
# حذف عناصر تکراری
# را در آن پیاده سازی کنید

class Tools:
    my_list = []
    def __init__(self) -> None:
        while True:
            x = int(input('> '))
            if x == -1:
                break
            self.my_list.append(x)
    def avg(self):
        return sum(self.my_list) / len(self.my_list)
    def remove(self):
        self.my_list = list(set(self.my_list))
    def adder(self, a):
        self.my_list.append(a)
