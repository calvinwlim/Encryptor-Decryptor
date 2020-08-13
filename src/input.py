import pyfiglet
import getpass

def inputs():
    banner = pyfiglet.figlet_format('Encryptor-Decryptor', font = "slant")
    print(banner)
    print('\n')
    message = getpass.getpass(prompt='Enter Message To Encrypt: ').encode()
    print('\n')
    decryptToggle = input('Do You Want To Display Decrypted Message As Well? Y/N ')

    return{'message':message,'decryptToggle':decryptToggle}
