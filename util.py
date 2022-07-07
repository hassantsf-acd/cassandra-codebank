from time import time


def get_current_ms():
    return int(time() * 1000)

def convert_string_to_list(string):
    string = string[2:-2]
    string = string.split("', '")
    return string

def convert_level_to_number(index):
    level = 2 * (ord(index[0]) - ord('A'))
    if len(index) == 1:
        level += 1
    else:
        level += int(index[1])

    return level

def convert_string_bigint(string):
    return int(string[1:])