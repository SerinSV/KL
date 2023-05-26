class AggregatorOperators:
    operators = [
        "$abs", "$add", "$addToSet", "$allElementsTrue", "$and", "$anyElementTrue", "$arrayElemAt",
        "$arrayToObject", "$avg", "$bitwiseAnd", "$bitwiseOr", "$bitwiseXor", "$ceil", "$cmp", "$concat",
        "$concatArrays", "$cond", "$convert", "$dateFromParts", "$dateFromString", "$dateToParts",
        "$dateToString", "$dayOfMonth", "$dayOfWeek", "$dayOfYear", "$divide", "$eq", "$exp", "$filter",
        "$first", "$floor", "$function", "$gt", "$gte", "$hour", "$ifNull", "$in", "$indexOfArray",
        "$indexOfBytes", "$indexOfCP", "$isArray", "$isoDayOfWeek", "$isoWeek", "$isoWeekYear", "$last",
        "$let", "$literal", "$ln", "$log", "$log10", "$lt", "$lte", "$ltrim", "$map", "$max", "$mergeObjects",
        "$meta", "$millisecond", "$min", "$minute", "$mod", "$month", "$multiply", "$ne", "$not",
        "$objectToArray", "$or", "$pow", "$push", "$range", "$reduce", "$regexFind", "$regexFindAll",
        "$regexMatch", "$replaceOne", "$replaceAll", "$reverseArray", "$rtrim", "$second", "$setDifference",
        "$setEquals", "$setIntersection", "$setIsSubset", "$setUnion", "$size", "$slice", "$split", "$sqrt",
        "$stdDevPop", "$stdDevSamp", "$strcasecmp", "$strLenBytes", "$strLenCP", "$substr", "$subtract",
        "$sum", "$switch", "$toBool", "$toDate", "$toDecimal", "$toDouble", "$toInt", "$toLong", "$toObjectId",
        "$toString", "$toLower", "$toUpper", "$trim", "$trunc", "$type", "$unset", "$unwind", "$week", "$year",
        "$zip"
    ]



# input:
{
  "stages": [
    {
      "operator": "$match",
      "field": "courses",
      "value": "English"
    }, {
      "operator": "$match",
      "field": "courses",
      "value": "Malayalam"
    }
  ]
}