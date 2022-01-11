import random
from random import choice
from string import ascii_letters


class Randomizer:
    def __init__(self, length):
        self.length = length

    def get_block(self):
        a = choice(ascii_letters)
        b = choice(ascii_letters)
        c = str(random.randint(0, 9))
        block = a + b + c
        return block

    def big_rand_string(self):
        result_string = ''.join(self.get_block() for i in range(self.length))
        return result_string

    def get_rand_string(self):
        big_string = self.big_rand_string()
        string = ''
        for i in range(0, self.length, 1):
            string += big_string[i]
        return string

    def get_rand_int(self):
        result = random.randint(1, 50)
        result = result/10
        print(result)
        return result
