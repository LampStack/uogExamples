import os
os.system('cls')

class Calculator:
    def setter(self, a, b) -> None:
        self.a = a
        self.b = b
    def jam(self):
        return self.a + self.b
    def tafriq(self):
        return self.a - self.b
    def zarb(self):
        return self.a * self.b
    def taqsim(self):
        if self.b == 0:
            return -1
        return self.a / self.b
