from cryptography.fernet import Fernet
import time

while True:
    time.sleep(3)

    # Open the instructions text file to read how to proceed.
    with open('instructions.txt', 'r') as infile:
        line1 = infile.readline().strip()
        line2 = infile.readline().strip()

    # If the first line reads "Y" generate a new key.
    if line1 == 'Y':
        key1 = Fernet.generate_key()

        # Save the generated key to the file key.key. Used later when decrypted and encrypting text.
        with open('key.key', 'wb') as outfile:
            outfile.write(key1)

    # If line 2 is "E" encrypt the text in e_request.txt and return it to the user as e_response.txt
    if line2 == 'E':
        with open('key.key', 'rb') as key_file:
            key = key_file.read()

        with open('e_request.txt', 'r') as e_in:
            data = e_in.read().encode('utf-8')

        fernet = Fernet(key)
        encrypted = fernet.encrypt(data)

        with open('e_response.txt', 'wb') as outfile:
            outfile.write(encrypted)

        # Change instructions to be blank to ensure new keys aren't generated or text is continuously encrypted.
        with open('instructions.txt', 'w') as outfile:
            outfile.write('')

    # If line 2  is "D" open e_response.txt and decrypt the text and return it to the user as d_response.txt.
    elif line2 == 'D':
        with open('key.key', 'rb') as key_file:
            key = key_file.read()

        with open('e_response.txt', 'rb') as d_in:
            data = d_in.read()

        fernet = Fernet(key)
        decrypted = fernet.decrypt(data)
        decrypted = decrypted.decode('utf-8')

        with open('d_response.txt', 'w') as outfile:
            outfile.write(decrypted)

        # As before clear instructions.txt
        with open('instructions.txt', 'w') as outfile:
            outfile.write('')
