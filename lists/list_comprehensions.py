numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = [str(number) for number in numbers if number % 2 == 0]

print(f"Even numbers are: {', '.join(even_numbers)}")
