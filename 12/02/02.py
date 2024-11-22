import string
import random


def generate_index():
    letters = string.ascii_uppercase
    return f'{random.choice(letters)}{random.choice(letters)}{random.randint(0, 99)}_{random.randint(0, 99)}{random.choice(letters)}{random.choice(letters)}'
