import random
import string


class randomData:
    def generate_random_string(self):
        first_two_integers = ''.join(random.choices(string.digits, k=2))
        five_uppercase_chars = ''.join(random.choices(string.ascii_uppercase, k=5))
        four_integers = ''.join(random.choices(string.digits, k=4))
        one_uppercase_char = random.choice(string.ascii_uppercase)
        one_integer = random.choice(string.digits) + 'Z'
        two_uppercase_chars = ''.join(random.choices(string.ascii_uppercase, k=1))

        return f"{first_two_integers}{five_uppercase_chars}{four_integers}{one_uppercase_char}{one_integer}{two_uppercase_chars}"

    def generate_random_Pan(self):
        five_uppercase_chars = ''.join(random.choices(string.ascii_uppercase, k=5))
        four_digits = ''.join(random.choices(string.digits, k=4))
        one_uppercase_char = random.choice(string.ascii_uppercase)

        return f"{five_uppercase_chars}{four_digits}{one_uppercase_char}"

    @staticmethod
    def genrate_random_phone():
        phone = '91' + ''.join(random.choices(string.digits, k=8))
        return phone

    phone_nu = genrate_random_phone()


    def random_email(self):
        mail = ''.join(random.choices(string.ascii_letters, k=6)) + '@gmail.com'
        return mail


