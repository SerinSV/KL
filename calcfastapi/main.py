import uvicorn
from fastapi import FastAPI,APIRouter
from typing import Optional
from scripts.constants.app_configurations import *
from scripts.core.services import calculator_service

calculator_app = FastAPI()

calculator_app.include_router(calculator_service.app)



if __name__ == "__main__":
    uvicorn.run(calculator_app, host=str(HOST), port=int(PORT))
