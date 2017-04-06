import itertools
from django.db import connection

def queryNames(limit):
    # Build firstName query
    query = "SELECT firstName FROM FirstName LIMIT " + str(limit) + ";"
    with connection.cursor() as cursor:
        cursor.execute(query)
        for row in cursor.fetchall():
            print row

def permuteNameByRace(names, race, limit):
    permu = dict()
    count = 0
    isLimit = False

    while (isLimit == False):
        for r in itertools.product(names, race):
            if count < limit:
                permu = str(r[0]) + str(r[1])
                count += 1
                print count
            else:
                isLimit = True
    return permu

def joinNames(arr1, arr2, limit):
    result = dict()
    names = []
    count = 0
    isLimit = False

    while (isLimit == False):
        for r in itertools.product(arr1, arr2):
            if count < limit:
                newName = str(r[0]) + str(r[1])
                names.append(newName)
                print "count = ", count,", name = ", newName
                count += 1
            else:
                isLimit = True
                break
    result["Name"] = names
    return result

a = [1,2,3]
b = ['a','b','c']

queryNames(10)
# print joinNames(b, a, 10)
