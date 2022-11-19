even_numbers = lambda x: x % 2 == 0

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers_list:
    if even_numbers(num):
        print(num)