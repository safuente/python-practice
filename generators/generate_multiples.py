def generate_multiples(input_number,limit):
    for multiple in range(input_number, limit):
        if multiple % input_number == 0:
            yield multiple


for num in generate_multiples(4, 20):
    print(num)
