from Crypto.Util.number import *

ACARUTO = 'Hey it\'s me Acaruto! I am the pillar of life. You don\'t know me, but I know everyone'.encode()

def encrypt(e, n):
    try:
        msg = input('Enter the message: ')
        assert msg.isascii()
    except AssertionError:
        print('Invalid input!')
    else:
        enc = pow(bytes_to_long(msg.encode()), e, n)
        print('Encrypted message in hex:', hex(enc)[2:])