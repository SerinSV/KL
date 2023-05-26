import uvicorn
from typing import Optional
from dotenv import  load_dotenv
from fastapi import FastAPI
from scripts.core.services import students_enrolment_service
from scripts.constants.app_configuration import *
# from scripts.utils.mongo_utility import MongoServer
#
# students = []
app = FastAPI()
# mongo_obj = MongoServer()

app.include_router(students_enrolment_service.student_router)

# @app.post("/students/")
# async def create_student(student: StudentInputModel):
#     mongo_obj.insert_one(student. dict())
#     students.append(student)
#     return students

#
# @app.get("/students/id")
# async def get_student(id: int):
#     student = students_details.find_one({"id": id})
#     if student:
#         return student
#     return {"error": "student not found"}
#
#
# @app.put("/students/{id}/courses")
# async def add_course_to_students(id: int, course: str):
#     student = students_details.find_one({"id": id})
#     if student:
#         student.courses.append(course)
#         return student
#     return {"error": "student not found"}


# @app.delete("/students/id")
# async def delete_student(id: int):
#     student = students_details.find_one({"id": id})
#     if student.id == id:
#         del student
#         return {"message": "Student successfully deleted"}
#     return {"error": "Student not found"}
#
#
# @app.get("/students")
# async def get_all_students():
#     students = students_details.find()
#     return students


if __name__ == "__main__":
    load_dotenv()
    uvicorn.run("app:app", host=str(HOST), port=int(PORT), reload=True)
