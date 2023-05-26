class Calculator:

    def hello(self):
        print("in handler")
        return {"Response": "Hello, Welcome to the Calculator API."}

    def subtract(self, firstNumber, secondNumber):
        try:
            result = firstNumber - secondNumber
            response = {
                "status": "success",
                "result": f"{firstNumber} - {secondNumber} = {result}"
            }
            return response
        except TypeError:
            return {"error": "Please provide valid numeric values for x and y."}

    def add(self, firstNumber, secondNumber):
        try:
            result = firstNumber + secondNumber
            response = {
                "status": "success",
                "result": f"{firstNumber} + {secondNumber} = {result}"
            }
            return response
        except TypeError:
            return {"error": "Please provide valid numeric values for x and y."}

    def multiply(self, firstNumber, secondNumber):
        try:
            result = firstNumber * secondNumber
            response = {
                "status": "success",
                "result": f"{firstNumber} * {secondNumber} = {result}"
            }
            return response
        except TypeError:
            return {"error": "Please provide valid numeric values for x and y."}

    def divide(self, firstNumber, secondNumber):
        try:
            if secondNumber == 0:
                return {"error": "Division by zero is not possible"}
            result = firstNumber / secondNumber
            response = {
                "status": "success",
                "result": f"{firstNumber} / {secondNumber} = {result}"
            }
            return response
        except TypeError:
            return {"error": "Please provide valid numeric values for x and y."}

    def exponent(self, firstNumber, secondNumber):
        try:
            result = firstNumber ** secondNumber
            response = {
                "status": "success",
                "result": f"{firstNumber} ** {secondNumber} = {result}"
            }
            return response
        except TypeError:
            return {"error": "Please provide valid numeric values for x and y."}
