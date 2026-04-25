from time import time
from random import randint
from hashlib import sha1


class YFKeygenService:
    @staticmethod
    def generate_key():
        key = str(time() + randint(1, 9999999))
        return sha1(key.encode()).hexdigest()
