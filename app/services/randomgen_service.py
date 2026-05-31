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

    @staticmethod
    def generate_minecraft_uuid(username: str):
        """Generates the offline UUID of a Minecraft username"""
        name = f"OfflinePlayer:{username.strip()}".encode("utf-8")
        md5 = hashlib.md5(name).digest()
        byte_array = bytearray(md5)
        byte_array[6] = (byte_array[6] & 0x0F) | 0x30
        byte_array[8] = (byte_array[8] & 0x3F) | 0x80
        return str(uuid.UUID(bytes=bytes(byte_array)))
