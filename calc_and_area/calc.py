# Calculator

class Calculator:
    def __init__(self, firstNumber: float, secondNumber: float):
        self.firstNumber = firstNumber
        self.secondNumber = secondNumber

    def addition_of_two_numbers(self):
        ans = self.firstNumber + self.secondNumber
        print(ans)

    def subtraction_of_two_numbers(self):
        ans = self.firstNumber - self.secondNumber
        print(ans)

    def multiplication_of_two_numbers(self):
        ans = self.firstNumber * self.secondNumber
        print(ans)

    def division_of_two_numbers(self):
        ans = self.firstNumber / self.secondNumber
        print(ans)

    def exponential_of_two_numbers(self):
        ans = self.firstNumber ** self.secondNumber
        print(ans)


d = Calculator(4, 6)
d.addition_of_two_numbers()
d.subtraction_of_two_numbers()
d.multiplication_of_two_numbers()
d.division_of_two_numbers()
d.exponential_of_two_numbers()


ww