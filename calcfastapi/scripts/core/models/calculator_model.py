from pydantic import BaseModel
from typing import Optional

"""Input Models"""


class CalculatorInput(BaseModel):
    x: float or int
    y: float or int


"""Output Models"""


class CalculatorOutput(BaseModel):
    result: float



