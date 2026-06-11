# list --> [] or list()
# squares= [2, 4, 9, 16]
# index    0  1  2  3
# colors= list({'red', 'green', 'blue', 'orange', 'white', 'black'})
# print(colors)

# adding items to a list 
# squares.append(25)
# colors.append('pink')

# removing items from a list
# squares.pop(1)
# colors.remove('red')

# print(squares)
# print(colors)
# print(squares[3])

# tuple --> () or tuple()
# fruits = ("orange", "bannana", "mango")
# countries = tuple(["France", "Uk","Ghana"])
# print(type(fruits))
# print(countries)

# dictionary --> {key: value} or dict()
# student = {
#     "name": "Goodluck Austine",
#     "age": 6,
#     "gender": "male"
# }

# student.pop('name')
# student.update({'name': 'Ijeoma'})
# student.update({'gender': 'female'})
# student.update({'age': 3})

# print(student)
# print(student['age'])
# print(student.get("age"))


# set --> {} or set()
cities_1 = {'London', 'New York', 'California', 'Paris', 'London'}
cities_2 = set({'Leeds', 'Hull','Newcastle','London'})
cities_1.add('Abuja')


print(cities_1.intersection(cities_2))

print(cities_1.union(cities_2))



