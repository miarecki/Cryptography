#!/usr/bin/env python3

import string

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase

def rot13(data):
    new_data = [
        uppercase[(uppercase.find(c) + 13) % 26] if c in uppercase
        else lowercase[(lowercase.find(c) + 13) % 26] if c in lowercase
        else c for c in data
    ]
    return "".join(new_data)

if __name__ == '__main__':
    while True:
        input_data = input("Enter data to encrypt/decrypt: \n")
        print(rot13(input_data))
