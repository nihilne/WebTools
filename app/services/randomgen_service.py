import hashlib
import secrets
import time
import uuid


class RandomGenService:
    @staticmethod
    def generate_custom_sha1():
        key = str(time.time() + (secrets.randbelow(9999999) + 1))
        return hashlib.sha1(key.encode()).hexdigest()

    @staticmethod
    def generate_uuidv4():
        return uuid.uuid4()
