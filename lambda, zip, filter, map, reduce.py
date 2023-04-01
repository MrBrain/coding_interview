#lambda arguments: expression
multiply = lambda x,y: x * y
print(multiply(21, 2))

#map

old_list = ['1', '2', '3', '4', '5', '6', '7']

new_list = []
for item in old_list:
    new_list.append(int(item))

print(new_list)

#[1, 2, 3, 4, 5, 6, 7]

#the same with map
old_list = ['1', '2', '3', '4', '5', '6', '7']
new_list = list(map(int, old_list))
print(new_list)

#[1, 2, 3, 4, 5, 6, 7]


def miles_to_kilometers(num_miles):
    """ Converts miles to the kilometers """
    return num_miles * 1.6


mile_distances = [1.0, 6.5, 17.4, 2.4, 9]
kilometer_distances = list(map(miles_to_kilometers, mile_distances))
print(kilometer_distances)

#[1.6, 10.4, 27.84, 3.84, 14.4]

mile_distances = [1.0, 6.5, 17.4, 2.4, 9]
kilometer_distances = list(map(lambda x: x * 1.6, mile_distances))

print(kilometer_distances)

#[1.6, 10.4, 27.84, 3.84, 14.4]

from functools import reduce

items = [1, 24, 17, 14, 9, 32, 2]
all_max = reduce(lambda a, b: a if (a > b) else b, items)

print(all_max)

#http://pythonicway.com/python-functinal-programming



