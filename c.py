
def Encrypt(plaintext, key_val):
    ciphertext = ''
    for i in range(len(plaintext)):
        special = plaintext[i]
        new_special = special.lower()
        if new_special == " ":
            ciphertext += ' '
        elif special.isalpha():
            ciphertext += chr((ord(new_special) + key_val - 97) % 26 + 97)

    return ciphertext


def Decrypt(ciphertext, key_val):
    plaintext = ''
    for i in range(len(ciphertext)):
        special = ciphertext[i]
        new_special = special.lower()
        if new_special == " ":
            plaintext += ' '
        elif special.isalpha():
            plaintext += chr((ord(new_special) - key_val - 97) % 26 + 97)
    return plaintext


while True:
    print(
        '[*] Press 0 for Encryption \n [*] Press 1 for Decryption \n [*] Press 2 to exit ')
    choice = input('Insert Here : ')
    if choice.isdigit():
        if choice == '0':
            apple = input('Type your plaintext : ')
            key = int(input('Type the value you want to shift by) : '))
            print(50 * '-')
            print(f'Your encrypted text is: {Encrypt(apple, key)}')
            print(50 * '-')
            cat = input('Type Yes to continue the program, and no to exit.')
            if cat == 'no':
                print('Exiting')
                break
            else:
                pass
        elif choice == '1':
            orange = input('Insert the encrypted text : ')
            key = int(input('Insert shift value(Only integer values) : '))
            print(50 * '-')
            print(f'Your plaintext is: {Decrypt(orange, key)}')
            print(50 * '-')
            dog = input('Type Yes to continue the program, and no to exit.')
            if dog == 'no':
                print('Exiting')
                break
            else:
                pass
        elif choice == '2':
            print('Exiting..')
            break
        else:
            print('Error \n')








# i like cats