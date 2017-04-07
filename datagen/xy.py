import itertools
from django.db import connections
import decimal

def queryNames(limit):
    # Build firstName query
    query = "SELECT firstName FROM FirstName LIMIT " + str(limit) + ";"
    try:
        cursor = connections['postgres'].cursor()
        cursor.execute(query)
        for row in cursor.fetchall():
            print row
    finally:
        cursor.close()

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

a = [["a", "b", "c"], ["1", "2", "3"]]

# print a[0] + " " + a[1]

# c = []
# for i in range(0, len(a[0])):
#     c.append(str(a[0][i]) + " " + str(a[1][i]))
# print c
#
# a[0].extend(a[1])
# print a[0]
