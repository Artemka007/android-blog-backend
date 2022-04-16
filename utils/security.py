import base64

import rsa
from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
from django.conf import settings


def encrypt_string(string):
    string = base64.b64encode(bytes(string, "utf-8"))

    pemFile = open(settings.BASE_DIR / "security/public_key.pem", 'rb')
    keyData = pemFile.read()
    
    cipher = PKCS1_v1_5.new(keyData)

    result = cipher.encrypt(keyData)

    return result


def decrypt_string(ciphertext):
    ciphertext = base64.b64decode(ciphertext)

    private_key = open(settings.BASE_DIR / "security/private_key.pem", 'rb').read()
    private_key = RSA.importKey(private_key)
    
    sentinel = Random.new().read(256)
    cipher = PKCS1_v1_5.new(private_key)

    result = cipher.decrypt(ciphertext, sentinel)

    return result.decode("utf-8")
