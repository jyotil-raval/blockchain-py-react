from Backend.Util.crypto_hash import get_crypto_hash


HEX_TO_BINARY_CONVERSION_TABLE = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'a': '1010',
    'b': '1011',
    'c': '1100',
    'd': '1101',
    'e': '1110',
    'f': '1111'
}

def hex_to_binary(hex_string):
    binary_string = ''

    for hex_char in hex_string:
        binary_string += HEX_TO_BINARY_CONVERSION_TABLE[hex_char]

    return binary_string

def main():
    number = 451
    hex_number = hex(number)[2:]
    print(f'Hexadecimal number: {hex_number}')
    binary_number = hex_to_binary(hex_number)
    print(f'Binary number: {binary_number}')
    original_number = int(binary_number, 2)
    print(f'original number: {original_number}')

    test_data = 'test_data'
    crypto_hash  = get_crypto_hash(test_data)
    hex_to_binary_crypto_hash = hex_to_binary(crypto_hash)
    print(f'hex_to_binary_crypto_hash: {hex_to_binary_crypto_hash}')
    
if __name__ == '__main__':
    main()