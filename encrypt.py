from cryptography.fernet import Fernet
import time

while True:
    time.sleep(3)
    with open('instructions.txt', 'r') as infile:
        line1 = infile.readline().strip()
        line2 = infile.readline().strip()

        if line1 == 'Y':
            key1 = Fernet.generate_key()

            with open('key.key', 'wb') as outfile:
                outfile.write(key1)

        if line2 == 'E':
            with open('key.key', 'rb') as key_file:
                key = key_file.read()

            with open('e_request.txt', 'r') as e_in:
                data = e_in.read().encode('utf-8')

            fernet = Fernet(key)
            encrypted = fernet.encrypt(data)

            with open('e_response.txt', 'wb') as outfile:
                outfile.write(encrypted)

            with open('instructions.txt', 'w') as outfile:
                outfile.write('')

        elif line2 == 'D':
            with open('key.key', 'rb') as key_file:
                key = key_file.read()

            with open('e_response.txt', 'rb') as d_in:
                data = d_in.read()

            fernet = Fernet(key)
            decrypted = fernet.decrypt(data)
            decrypted = decrypted.decode('utf-8')
            print(decrypted)

            with open('d_response.txt', 'w') as outfile:
                outfile.write(decrypted)

            with open('instructions.txt', 'w') as outfile:
                outfile.write('')
