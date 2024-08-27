import zlib

def generate_crc32(input_text):
    # Convert data to byte
    byte_data = input_text.encode('utf-8')

    # Calculate CRC32 checksum
    crc32_hash = zlib.crc32(byte_data)

    # Convert it to 8 character hexadecimal number
    crc32_hash_hex = format(crc32_hash & 0xFFFFFFFF, '08x')

    return crc32_hash_hex
