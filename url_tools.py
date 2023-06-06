import hashlib


BASE62 = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encode(input_number: int, alphabet: str = BASE62):
    """Give a representation for `input_number` in the provided alphabet.

    What basically is being done is to represent `input_number` in the base `len(alphabet)` and then replacing the
    numerical representatives by the characters in alphabet.

    The default alphabet consists of all alpha-numerical characters.

    Note: unlike the usual base representation, the order of the representatives is not reversed here!

    :param input_number:
    :param alphabet:
    :return:
    """
    len_alphabet = len(alphabet)

    result = []
    number = input_number

    while number != 0:
        (value, remainder) = divmod(number, len_alphabet)
        result.append(alphabet[remainder])
        number = value

    return "".join(result)


def shorten_string(string: str, string_length: int):
    """Give a shortend string of desired length for provided string

    In order to achieve this, the md5 hash of the string is calculated and the int value of that string
    is transformed using the `encode` function.

    :param string:
        string for which a shortened representation is needed
    :param string_length:
        length the new representation should have
    :return:
        a representation of the string in desired length
    """
    md5_hash = hashlib.md5(string.encode())
    transformed_string = encode(int(md5_hash.hexdigest(), base=16))
    return transformed_string[0:string_length]
