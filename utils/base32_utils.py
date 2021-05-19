import re
from base64 import b32decode, b32encode
from io import BytesIO
from typing import List


def decode_base32(data: str, altchars='+/') -> bytes:
    """
    Decode base32, python requires additional padding
    """
    data = re.sub(rf'[^a-zA-Z0-9{altchars}]+', '', data)  # normalize
    missing_padding = len(data) % 8
    if missing_padding:
        data += '=' * (8 - missing_padding)
    return b32decode(data, altchars)


def byte_to_int(single_byte: bytes) -> int:
    """
    Gets a byte and returns an integer
    :param single_byte: Single byte to convert to integer
    :return: Integer representation of the bytes
    """
    shift = 0
    result = 0
    if single_byte == b"" or single_byte == "":
        raise EOFError("Unexpected EOF while reading varint")
    i = ord(single_byte)
    result |= (i & 0x7f) << shift
    return result


def int_list(data: bytes) -> list:
    """
    Get a set bytes and return a list of integers representing the bytes
    :param data: Bytes
    :return: List of integers
    """
    byte_data = BytesIO(data)
    byte_list = []
    single_byte = byte_data.read(1)
    while single_byte != b"" and single_byte != "":
        single_int = byte_to_int(single_byte)
        byte_list.append(single_int)
        single_byte = byte_data.read(1)
    return byte_list


def encode_base32_from_list(list_of_int: List[int]) -> str:
    """
    Returns a base 32 string from a list of integers
    :param list_of_int: List of integers
    :return: Base32 string
    """
    data = BytesIO()
    for i in list_of_int:
        buf = b""
        while True:
            towrite = i & 0x7f
            i >>= 7
            if i:
                buf += bytes((towrite | 0x80,))
            else:
                buf += bytes((towrite,))
                break
        data.write(buf)
    data.seek(0)
    return b32encode(data.read()).decode().replace('=', '')