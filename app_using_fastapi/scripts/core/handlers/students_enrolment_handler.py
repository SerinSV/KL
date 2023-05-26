"""
This is the students enrolment handler
this is for <this> purpose
"""
import json

from fastapi.encoders import jsonable_encoder

from scripts.utils.mongo_utility import MongoServer
from scripts.exceptions.student_information_exceptions import StudentInformationException
from scripts.core.models.students_enrolment_model import StudentInputModel, AggregationStage, AggregationStages, \
    OperatorsOfMongodb


class StudentInformation:
    """
    This is the class information
    """

    def __init__(self):
        self.mongo_obj = MongoServer()

    def create_info_student(self, request_json=StudentInputModel):
        try:

            id_of_entered_student = request_json.id
            request_json = jsonable_encoder(request_json)
            if self.mongo_obj.read_one(id_of_entered_student):
                return {"Status": "Failure", "Message": "id already exists"}
            else:
                response_student = self.mongo_obj.insert_data(json_data=request_json)
                return {"Status": "Success", "Data": f"Object id of student is {response_student}",
                        "Message": "Student is Entered"}
        except Exception as es:
            print(StudentInformationException.SIE001, str(es))

    # def create_info_student(self, request_json):
    #     print(request_json)
    #     print(type(request_json))
    #     try:
    #         # id_of_entered_student = request_json.id
    #         id_of_entered_student = request_json.get("id")
    #         if self.mongo_obj.read_one(id_of_entered_student):
    #             return {"Status": "Failure", "Message": "id already exists"}
    #         else:
    #             response_student = self.mongo_obj.insert_data(json_data=request_json)
    #             return {"Status": "Success", "Data": f"Object id of student is {response_student}",
    #                     "Message": "Student is Entered"}
    #     except Exception as es:
    #         print(StudentInformationException.SIE001, str(es))

    def find_student_with_id(self, id=int):
        try:
            response_student = self.mongo_obj.read_one(id)
            if response_student:
                response_student.pop("_id")
                return {"Status": "Success", "Data": response_student,
                        "Message": "Student is Found"}
            else:
                return {"Status": "failure", "Message": "student with this id doesnt exist"}
        except Exception as e:
            print(StudentInformationException.SIE002, str(e))

    def to_delete_a_student(self, id=int):
        try:
            student = self.mongo_obj.read_one(id)
            if student:
                self.mongo_obj.delete_one(id)
                return {"Status": "Success",
                        "Message": f"Student with id:{id} is deleted"}
            else:
                return {"Status": "Failure", "Message": f"Student with id:{id} doesnt exist"}
        except Exception as err:
            print(StudentInformationException.SIE003, str(err))

    def find_with_name(self, name=str):
        try:
            response_student = self.mongo_obj.find_with_condition(name)
            if response_student:
                for item in response_student:
                    del item['_id']
                print(response_student)
                return {"Status": "Success", "Data": response_student,
                        "Message": "Student is Found"}
            else:
                return {"Status": "Failure", "Message": "Student with name doesnt exist"}
        except Exception as err:
            print(StudentInformationException.SIE005, str(err))

    def find_with_course(self, course=str):
        try:
            print("hello")
            response_student = self.mongo_obj.find_with_condition_course(course)
            result = []
            if response_student:
                for data in response_student:
                    del data['_id']
                    result.append(data)
                return {"Status": "Success", "Data": result,
                        "Message": f"Students studying {course} are found"}
            else:
                return {"Status": "Failure", "Message": f"Student studying {course} doesnt exist"}
        except Exception as err:
            print(StudentInformationException.SIE008, str(err))

    def update_courses(self, id: int, course: list[str]):
        try:
            student_obj = StudentInformation()
            response_result = self.mongo_obj.read_one(id)
            if response_result:
                response_student = self.mongo_obj.update_data(id, course)
                result = self.mongo_obj.read_one(id)
                result.pop("_id")
                return {"Status": "Success", "Data": result,
                        "Message": "Course is updated"}
            else:
                return {"Status": "failure", "Message": "student with this id doesnt exist"}
        except Exception as err:
            print(StudentInformationException.SIE004, str(err))

    def add_courses(self, id: int, course: list[str]):
        try:
            student_obj = StudentInformation()
            mongo_response = self.mongo_obj.read_one(id)
            if mongo_response:
                response_student = self.mongo_obj.add_data(id, course)
                response_result = self.mongo_obj.read_one(id)
                response_result.pop("_id")
                return {"Status": "Success", "Data": response_result,
                        "Message": "Course is added"}
            else:
                return {"Status": "failure", "Message": "student with this id doesnt exist"}
        except Exception as err:
            print(StudentInformationException.SIE006, str(err))

    def get_all_students(self):
        try:
            response_student = self.mongo_obj.get_all()
            if response_student:
                for item in response_student:
                    del item['_id']
                return {"Status": "Success", "Data": response_student,
                        "Message": "Details of all students are displayed"}
            else:
                return {"Status": "failure", "Message": "Details doesn't exist"}
        except Exception as err:
            print(StudentInformationException.SIE007, str(err))

    # def mongo_aggregation(self, aggregation_stages):
    #     try:
    #         response_student = self.mongo_obj.get_by_aggregation(aggregation_stages)
    #         if response_student:
    #             for item in response_student:
    #                 del item['_id']
    #             return {"Status": "Success", "Data": response_student,
    #                     "Message": "Details of selected students are displayed"}
    #         else:
    #             return {"Status": "Failure", "Message": "Details don't exist"}
    #     except Exception as err:
    #         print(StudentInformationException.SIE009, str(err))

    def mongo_aggregation(self, aggregation_stages_input: AggregationStages):
        try:

            stages = aggregation_stages_input.stages

            list_containing_aggregation_stages = []
            for stage in stages:
                if stage.operator in OperatorsOfMongodb.operators:
                    operator = stage.operator
                else:
                    return {"Status": "Failure", "Message": f"Invalid operator: {stage.operator}"}
                print(type(stage.value))

                try:
                    value = int(stage.value)
                except:
                    value = str(stage.value)

                condition = {
                    stage.field: value}

                list_containing_aggregation_stages.append({
                    operator: condition
                })

            response_student = self.mongo_obj.get_by_aggregation(list_containing_aggregation_stages)

            if response_student:
                for item in response_student:
                    del item['_id']
                return {"Status": "Success", "Data": response_student,
                        "Message": "Details of selected students are displayed"}
            else:
                return {"Status": "Failure", "Message": "Details don't exist"}
        except Exception as err:
            print(StudentInformationException.SIE009, str(err))

    # def mongo_aggregation(self):
    #     try:
    #         response_student = self.mongo_obj.get_by_aggregation(
    #             [
    #                 {
    #                     '$match': {
    #                         'courses': 'English'
    #                     }
    #                 }, {
    #                 '$sort': {
    #                     'age': 1
    #                 }
    #             }, {
    #                 '$match': {
    #                     'age': {
    #                         '$gt': 22
    #                     }
    #                 }
    #             }
    #             ]
    #         )
    #         if response_student:
    #             for item in response_student:
    #                 del item['_id']
    #             return {"Status": "Success", "Data": response_student,
    #                     "Message": "Details of selected students are displayed"}
    #         else:
    #             return {"Status": "failure", "Message": "Details doesn't exist"}
    #     except Exception as err:
    #         print(StudentInformationException.SIE007, str(err))
    #

#
