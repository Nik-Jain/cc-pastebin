import zlib
import os
import bcrypt

def generate_crc32(input_text):
    # Convert data to byte
    byte_data = input_text.encode('utf-8')

    # Calculate CRC32 checksum
    crc32_hash = zlib.crc32(byte_data)

    # Convert it to 8 character hexadecimal number
    crc32_hash_hex = format(crc32_hash & 0xFFFFFFFF, '08x')

    return crc32_hash_hex

def generate_random_salt(length=16):
    # Generate a random salt of the specified length
    return os.urandom(length)

def generate_hash_password(plain_password):
    # Hash a password with some random salt
    return bcrypt.hashpw(plain_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def check_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
