#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
import os
from cryptography.fernet import Fernet
class Key_gen:
    def genrate_key(self):
        key_file="/Users/kpgarage/PasswordVault/.cryptokey"
        if os.path.exists(key_file):
            file = open(key_file,'rb')
            key = file.read()
            return key
        else:
            key = Fernet.generate_key()
            with open(key_file, 'wb') as file:
                file.write(key)
            return key

class Encrypt_password:
    """This class will take a string as input converts it to byte format and encrypt it"""
    def encrypt_passwd(self,password):
        self.password = password.encode()
        crypto_key = Key_gen.genrate_key(self)
        f = Fernet(crypto_key)
        cipher_text = f.encrypt(self.password)
        cipher_text = cipher_text.decode()
        return cipher_text
class Decrypt_password:
    """This class will take encrypted string and decrypt it to get necessary results"""
    def __init__(self,encrypted_str):
        self.encrypted_str = encrypted_str
    def decrypt_passwd(self):
        crypto_key = Key_gen.genrate_key(self)
        f = Fernet(crypto_key)
        plain_text = f.decrypt(self.encrypted_str)
        plain_text = plain_text.decode()
        return plain_text

encrypt = Encrypt_password().encrypt_passwd("test")
f = open("/tmp/encode_test", "w")
f.write(encrypt + "\n")
f.close()

f = open("/tmp/encode_test", "r")
encoded_part = f.read()
decrypted_str = encoded_part.encode()
plain_test = Decrypt_password(decrypted_str).decrypt_passwd()
print(plain_test)




