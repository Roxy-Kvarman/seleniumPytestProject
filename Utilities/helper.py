import random
import string


class Helper:

    @classmethod
    def string_generator(self, count):
        random_value = ""
        chars = string.ascii_letters + string.digits
        for _ in range(count):
            rnd = random.choice(chars)
            random_value += ''.join(rnd)
        return random_value

    @classmethod
    def number_generator(self, count):
        return random.randint(0, count)