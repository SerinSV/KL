from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

from scripts.constants.app_constants import CommonConstants
from scripts.core.models.students_enrolment_model import StudentInputModel, AggregationStages

from fastapi import APIRouter, HTTPException
from scripts.core.handlers.students_enrolment_handler import StudentInformation
from scripts.core.handlers.email_handler import EmailHandler, Email

# This is the router for <your purpose>
student_router = APIRouter()

student_info_obj = StudentInformation()


@student_router.post(CommonConstants.STUDENT_ENDPOINT)
def insert_student(student: StudentInputModel):
    try:
        response_list = student_info_obj.create_info_student(request_json=student)
        return response_list
    except Exception as e:
        print("Exception while Inserting the student data." + str(e))


# @student_router.post(CommonConstants.STUDENT_ENDPOINT)
# def insert_student(student: StudentInputModel):
#     student_json = jsonable_encoder(student)
#     print("student_json:", type(student_json))
#     print("student: ", type(student))
#     try:
#         response_list = student_info_obj.create_info_student(request_json=student_json)
#         # response_list = student_info_obj.create_info_student(request_json=student)
#         return response_list
#     except Exception as e:
#         print("Exception while Inserting the student data." + str(e))


@student_router.get(CommonConstants.STUDENT_FIND_ENDPOINT)
def find_a_student(id: int):
    try:
        response = student_info_obj.find_student_with_id(id)
        return response
    except Exception as e:
        print("Exception while finding the student data with id." + str(e))


@student_router.delete(CommonConstants.STUDENT_ID_ENDPOINT)
def delete_student(id: int):
    try:
        response = student_info_obj.to_delete_a_student(id)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@student_router.get(CommonConstants.STUDENT_NAME_ENDPOINT)
def student_by_name(name: str):
    try:
        response = student_info_obj.find_with_name(name)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@student_router.post(CommonConstants.STUDENT_ADD_ENDPOINT)
def student_by_course(course: str):
    try:
        response = student_info_obj.find_with_course(course)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@student_router.put(CommonConstants.STUDENT_ENDPOINT)
def update_courses_of_student(id: int, course: list[str]):
    try:
        response = student_info_obj.update_courses(id, course)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@student_router.put(CommonConstants.STUDENT_ADD_ENDPOINT)
def add_courses_to_student(id: int, course: list[str]):
    try:
        response = student_info_obj.add_courses(id, course)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@student_router.get(CommonConstants.STUDENT_ENDPOINT)
def get_details_of_all_students():
    try:
        response = student_info_obj.get_all_students()
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# @student_router.post(CommonConstants.AGGREGATE_ENDPOINT)
# def get_aggregation(aggregation_stages: AggregationStages):
#     try:
#         stages = aggregation_stages.stages
#         response = student_info_obj.mongo_aggregation(stages)
#         return response
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))


@student_router.post(CommonConstants.EMAIL_ENDPOINT)
def send_email(email: Email):
    try:
        return EmailHandler().send_email(email)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@student_router.post(CommonConstants.AGGREGATE_ENDPOINT)
def perform_aggregation(aggregation_stages_input: AggregationStages):
    try:
        response = student_info_obj.mongo_aggregation(aggregation_stages_input)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# @student_router.post("/aggregate")
# def perform_aggregation(aggregation_stages_input: AggregationStages):
#     try:
#         response = student_info_obj.mongo_aggregation(aggregation_stages_input)
#         # Access the aggregation stages from the request model
#         stages = aggregation_stages_input.stages
#
#         # Create the pipeline by constructing the stages dynamically
#         pipeline = []
#         for stage in stages:
#             # Validate the operator against the available operators list
#             if stage.operator in OperatorsOfMongodb.operators:
#                 operator = stage.operator
#             else:
#                 return {"Status": "Failure", "Message": f"Invalid operator: {stage.operator}"}
#             print(type(stage.value))
#
#             try:
#                 value = int(stage.value)
#             except:
#                 value = str(stage.value)
#
#             condition = {
#                 stage.field: value}
#
#             pipeline.append({
#                 operator: condition
#             })
#
#         print(pipeline)
#         response = student_info_obj.mongo_aggregation(pipeline)
#         return response
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
