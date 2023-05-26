from scripts.core.handlers.calculator_handler import Calculator
from scripts.core.models.calculator_model import *
from fastapi import APIRouter, HTTPException
from scripts.constants.app_constants import *

calculator_obj = Calculator()
app = APIRouter()


@app.get(CommonConstants.CALCULATOR_ENDPOINT)
async def welcome():
    print("in service")
    return calculator_obj.hello()


@app.post(CommonConstants.CALCULATOR_SUBTRACT_ENDPOINT)
async def subtract_two_numbers(FirstNumber: float or int, SecondNumber: float or int):
    return calculator_obj.subtract(FirstNumber, SecondNumber)


@app.post(CommonConstants.CALCULATOR_ADD_ENDPOINT)
async def add_two_numbers(FirstNumber: float or int, SecondNumber: float or int):
    return calculator_obj.add(FirstNumber, SecondNumber)


@app.put(CommonConstants.CALCULATOR_MULTIPLY_ENDPOINT)
async def multiply_two_numbers(FirstNumber: float or int, SecondNumber: float or int):
    return calculator_obj.multiply(FirstNumber, SecondNumber)


@app.post(CommonConstants.CALCULATOR_DIVIDE_ENDPOINT)
async def divide_two_numbers(FirstNumber: float or int, SecondNumber: float or int):
    return calculator_obj.divide(FirstNumber, SecondNumber)

@app.put(CommonConstants.CALCULATOR_EXPONENT_ENDPOINT)
async def exponent_a_number(FirstNumber: float or int, SecondNumber: float or int):
    return calculator_obj.exponent(FirstNumber, SecondNumber)