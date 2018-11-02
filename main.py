#!/usr/bin/python3
import cipher

if __name__ == '__main__':
    while True:
        print()
        print('----- CipherIT -----')
        print('1. Encrypt')
        print('2. Decrypt')
        print('3. Exit')

        menu_input = int(input('Choice: '))
        print()

        if menu_input == 1:
            text = input('Text: ')
            key = input('Key: ')
            print("Cipher text: " + cipher.encrypt(text, key))
        
        elif menu_input == 2:
            text = input('Text: ')
            key = input('Key: ')
            print("Original text: " + cipher.decrypt(text, key))
        
        elif menu_input == 3:
            break
        
        else:
            print('Unknown input: ' + str(menu_input))
