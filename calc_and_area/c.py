import typer


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
        return ans

    def exponential_of_two_numbers(self):
        ans = self.firstNumber ** self.secondNumber
        print(ans)


def main(first_number: float, second_number: float):
    calculator = Calculator(first_number, second_number)
    calculator.addition_of_two_numbers()
    calculator.subtraction_of_two_numbers()
    calculator.multiplication_of_two_numbers()
    calculator.division_of_two_numbers()
    calculator.exponential_of_two_numbers()


if __name__ == "__main__":
    typer.run(main)
