"""
THis is used for something
"""
from pydantic import BaseModel, EmailStr


class StudentInputModel(BaseModel):
    """
    This is the format of details of students who are enrolling
    """
    name: str
    id: int
    age: int
    email: EmailStr
    courses: list[str] = []


class CourseInputModel(BaseModel):
    course_name: str
    course_id: int
    course_fees: float


class AggregationStage(BaseModel):
    operator: str
    field: str
    value: str


class AggregationStages(BaseModel):
    stages: list[AggregationStage]


class StudentOutputModel(BaseModel):
    """
    This is the output display
    """
    response = dict


class OperatorsOfMongodb:
    operators = [
        "$abs", "$add", "$addToSet", "$allElementsTrue", "$and", "$anyElementTrue", "$arrayElemAt",
        "$arrayToObject", "$avg", "$bitwiseAnd", "$bitwiseOr", "$bitwiseXor", "$ceil", "$cmp", "$concat",
        "$concatArrays", "$cond", "$convert", "$dateFromParts", "$dateFromString", "$dateToParts",
        "$dateToString", "$dayOfMonth", "$dayOfWeek", "$dayOfYear", "$divide", "$eq", "$exp", "$filter",
        "$first", "$floor", "$function", "$gt", "$gte", "$hour", "$ifNull", "$in", "$indexOfArray",
        "$indexOfBytes", "$indexOfCP", "$isArray", "$isoDayOfWeek", "$isoWeek", "$isoWeekYear", "$last",
        "$let", "$literal", "$ln", "$log", "$log10", "$lt", "$lte", "$ltrim", "$map", "$max", "$mergeObjects",
        "$meta", "$match", "$millisecond", "$min", "$minute", "$mod", "$month", "$multiply", "$ne", "$not",
        "$objectToArray", "$or", "$pow", "$push", "$range", "$reduce", "$regexFind", "$regexFindAll",
        "$regexMatch", "$replaceOne", "$replaceAll", "$reverseArray", "$rtrim", "$second", "$setDifference",
        "$setEquals", "$setIntersection", "$setIsSubset", "$setUnion", "$size", "$slice", "$sort", "$split", "$sqrt",
        "$stdDevPop", "$stdDevSamp", "$strcasecmp", "$strLenBytes", "$strLenCP", "$substr", "$subtract",
        "$sum", "$switch", "$toBool", "$toDate", "$toDecimal", "$toDouble", "$toInt", "$toLong", "$toObjectId",
        "$toString", "$toLower", "$toUpper", "$trim", "$trunc", "$type", "$unset", "$unwind", "$week", "$year",
        "$zip"
    ]
