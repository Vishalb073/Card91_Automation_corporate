import random
import string


class randomData:
    def generate_random_string(self):
        gst_prefix = ''.join(random.choices('0123456789', k=2))
        gst_mid = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=5))
        gst_year = ''.join(random.choices('0123456789', k=4))
        gst_month = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=1))
        gst_day = ''.join(random.choices('0123456789', k=1))
        gst_suffix = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=1))

        return f"{gst_prefix}{gst_mid}{gst_year}{gst_month}{gst_day}{'Z'}{gst_suffix}"


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


