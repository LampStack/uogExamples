import os
os.system('CLS')

# کلاسی برای مستطیل بنویسید که دارای متودهای زیر باشد :
# محیط
# مساحت
# تشخیص مربع بودن

class rectangle:
    a, b = 0, 0
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b
    def primeter(self):
        return 2 * (self.a + self.b)
    def area(self):
        return self.a * self.b
    def isSquare(self):
        return self.a == self.b

my_obj = rectangle(4, 4)
print(my_obj.isSquare())
