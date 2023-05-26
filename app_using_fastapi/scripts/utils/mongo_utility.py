from pymongo import MongoClient


# from scripts.constants.app_configuration import *


class MongoServer:

    # def __init__(self):
    #     try:
    #         self.mongo_uri = MongoClient("mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23")
    #         self.mongo_db_name = "interns_b2_23"
    #         self.mongo_collection_name = "serin_student_enrollment"
    #         print("connected")
    #     except Exception as e:
    #         raise Exception(str(e))

    def __init__(self):
        try:
            self.mongo_uri = MongoClient(
                "mongodb+srv://serinsvarghese16:Serin%402000@cluster0.gsdzul4.mongodb.net/?retryWrites=true&w=majority")
            self.mongo_db_name = "my_db"
            self.mongo_collection_name = "my_collection"
            print("connected")
        except Exception as e:
            raise Exception(str(e))

    # def __init__(self, mongo_host=None, mongo_port=None,
    #              user_name=None, password=None):
    # def __init__(self):
    #     try:
    #         self.mongo_uri = MongoClient(
    #             host=MONGO_HOST,
    #             port=int(MONGO_PORT),
    #             username=MONGO_USERNAME,
    #             password="intern@123"
    #         )
    #         self.__mongo_OBJ__ = MongoClient("mongodb+srv://serinsvarghese16:Serin%402000@cluster0.gsdzul4.mongodb.net/?retryWrites=true&w=majority")
    #     except Exception as e:
    #         raise Exception(str(e))
    #
    #

    def insert_data(self, json_data):
        try:
            mongo_pointer = self.mongo_uri[self.mongo_db_name][self.mongo_collection_name]
            return str(mongo_pointer.insert_one(json_data).inserted_id)
        except Exception as e:
            raise Exception(print("exception in insert_one", str(e)))

    def read_one(self, id):
        try:
            mongo_pointer = self.mongo_uri[self.mongo_db_name][self.mongo_collection_name]
            mongo_response = mongo_pointer.find_one({"id": id})
            return mongo_response
        except Exception as e:
            raise Exception(print("id doesnt' exist", str(e)))

    def delete_one(self, id):
        try:
            mongo_pointer = self.mongo_uri[self.mongo_db_name][self.mongo_collection_name]
            mongo_response = mongo_pointer.delete_one({"id": id})
            return mongo_response
        except Exception as e:
            raise Exception(print("id doesnt' exist", str(e)))

    def find_with_condition(self, name=str):
        try:
            mongo_pointer = self.mongo_uri[self.mongo_db_name][self.mongo_collection_name]
            mongo_response = mongo_pointer.find({"name": name})
            return list(mongo_response)
        except Exception as e:

            raise Exception(str(e))

    def find_with_condition_course(self, course=str):
        try:
            mongo_pointer = self.mongo_uri[self.mongo_db_name][self.mongo_collection_name]
            mongo_response = mongo_pointer.find({"courses": f"{course}"})
            return mongo_response
        except Exception as e:
            raise Exception(str(e))

    def update_data(self, id: int, course: list[str]):
        try:
            mongo_pointer = self.mongo_uri[self.mongo_db_name][self.mongo_collection_name]
            mongo_result = mongo_pointer.update_one({"id": id}, {"$set": {"courses": course}})
            return {"success"}
        except Exception as e:
            raise Exception(str(e))

    def add_data(self, id: int, course: list[str]):
        try:
            mongo_pointer = self.mongo_uri[self.mongo_db_name][self.mongo_collection_name]
            mongo_result = mongo_pointer.update_one({"id": id}, {"$push": {"courses": {"$each": course}}})
            return {"success"}
        except Exception as e:
            raise Exception(str(e))

    def get_all(self):
        try:
            mongo_pointer = self.mongo_uri[self.mongo_db_name][self.mongo_collection_name]
            mongo_response = list(mongo_pointer.find())
            return mongo_response
        except Exception as e:
            raise Exception(str(e))

    def get_by_aggregation(self, list_containing_aggregation_stages):
        try:
            print("util")
            mongo_pointer = self.mongo_uri[self.mongo_db_name][self.mongo_collection_name]
            mongo_response = mongo_pointer.aggregate(list_containing_aggregation_stages)
            mongo_result = list(mongo_response)
            print(mongo_result)
            return mongo_result
        except Exception as e:
            raise Exception(str(e))
