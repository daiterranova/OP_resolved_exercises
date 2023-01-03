from functools import reduce
numbers = [0, 1, 3, 587, 4, 5, 89, 44, 190]


def filter_numbers(number):
    if number % 2 != 0:
        return True
    return False


filtered_list = filter(filter_numbers, numbers)
odd_numbers = list(filtered_list)
result = reduce(lambda num1, num2: num1 + num2, odd_numbers)
print(result)
