# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def sum_recursion(numbers_list):
    if len(numbers_list) == 0:
        return 0
    return numbers_list[0] + sum_recursion(numbers_list[1:])

def max_recursion(numbers_list):

    if len(numbers_list) == 1:
        return numbers_list[0]
    else:
        max_value = max_recursion(numbers_list[1:])
        return max_value if max_value > numbers_list[0] else numbers_list[0]

def binary_search_recursion(numbers_list, element, start, end):
    mid = (start + end) // 2
    if element == numbers_list[mid]:
        return mid
    elif numbers_list[mid] > element:
        return binary_search_recursion(numbers_list, element, start, mid-1)
    else:
        return binary_search_recursion(numbers_list, element, start, mid + 1)
    return 0







# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    b = []
    type_b = str(type(b))
    print(type_b)
    if type_b == "<class 'list'>":
        print(type_b)

    numbers_list = [1, 2, 3, 23, 123]
    element = 3
    start = 0
    if len(numbers_list) % 2 > 0 :
        end = len(numbers_list)
    else:
        end = len(numbers_list) - 1

    print(sum_recursion(numbers_list), max_recursion(numbers_list), numbers_list[binary_search_recursion(numbers_list, element, start, end)])


# See PyCharm help at https://www.jetbrains.com/help/pycharm/



