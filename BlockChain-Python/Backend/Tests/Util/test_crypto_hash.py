from Backend.Util.crypto_hash import get_crypto_hash

def test_get_crypto_hash():
    assert get_crypto_hash(1, '2', [3, 'Fourier']) != get_crypto_hash('2', ['Fourier', 3], 1)
    assert get_crypto_hash('Jyotil') == 'fcf78ed73419014961dc9ea9a1fe4d42bd70781dfdd52aae09438a31d769c045'