import random

def otoslotto():
    numbers = []
    while len(numbers) < 5:
        number = random.randint(1, 90)
        if number not in numbers:
            numbers.append(number)
    return sorted(numbers)
