import cryptography
from cryptography.fernet import Fernet
from input import inputs

result={}
result=inputs()
print('\n')
key = Fernet.generate_key()
print('Key: ')
print(key)
print('Store Above Key For Future Use')
f = Fernet(key)
encrypted = f.encrypt(result['message'])
decrypted = f.decrypt(encrypted)
decryptToggle=result['decryptToggle']
if decryptToggle == 'Y':
    print('\n')
    print('Encrypted Message: ')
    print(encrypted)
    print('\n')
    print('Decrypted Message: ')
    print(decrypted)
elif decryptToggle == 'N':
    print('\n')
    print('Encrypted Message: ')
    print(encrypted)
else:
    print('Invalid Y/N Input')
