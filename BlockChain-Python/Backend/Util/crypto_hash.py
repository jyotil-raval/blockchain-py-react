import hashlib
import json

# * below function is not needed as it directly used in line 14.
# def stringify(value):
#     return json.dumps(value)

def get_crypto_hash(*args):
    """
        Return a sha256 hash of given data which can be any type
    """
    # ? stringify_args = map(stringify, args) 
    # * stringify method can be replaced with 'lambda' keyword as arrow function in Javascript.
    stringify_args = sorted(map(lambda data: json.dumps(data), args))
    joined_args = ''.join(stringify_args)
    hash_sha256 = hashlib.sha256(joined_args.encode('utf-8')).hexdigest()
    return hash_sha256

def main():
    data = 'Jyotil'
    print(f"File: blockchain_py/crypto_hash.py:18 - get_crypto_hash({data}, 1, [2, 3, 4, 'Raval']): {get_crypto_hash(data, 1, [2, 3, 4, 'Raval'])}")
    
if __name__ == '__main__':
    main()