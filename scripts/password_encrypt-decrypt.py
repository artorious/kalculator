#!/usr/bin/env python3
'''Password Encryption/Decryption Program

The program allows a user to encrypt and decrypt passwords containing 
uppercase/lowercase characters, digits, and special characters. 

The script utilizes the following programming features:
    * for loop
    * nested sequences (tuples)
'''

def encrypt_decrypt():
    '''encrypt and decrypt passwords containing uppercase/lowercase characters, 
    digits, and special characters.'''
    terminate = False   # Control program termination

    while not terminate:
        ### Init vars
        password_out = ''   # Hold the encrypted/decrypted output

        case_changer = ord('a') - ord('A') # 32 - constant for aplphabets

        # Tuple(s) for encryption/decryption
        # TODO: Add keys for digits, and special characters
        encryption_key = (('a','m'), ('b','h'), ('c','t'), ('d','f'), ('e','g'), 
            ('f','k'), ('g','b'), ('h','p'), ('i','j'), ('j','w'), ('k','e'), ('l', 'r'),
            ('m','q'), ('n','s'), ('o','l'), ('p','n'), ('q','i'), ('r','u'), ('s','o'),
            ('t','x'), ('u','z'), ('v','y'), ('w','v'), ('x','d'), ('y','c'), ('z','a'))

        # Program Greeting
        print(format(' PASSWORD ENCRYPTION-DECRYPTION PROGRAM ', '=^80'))   
        print("~" * 80)
        print(format('This program will encrypt and decrypt user passwords', '^80'))
        print("~" * 80)

        which_op = input('Enter (e) to ENCRYPT a password or (d) to DECRYPT:  ')    # get selection encrypt/decrypt

        while which_op.lower() != 'e' and which_op.lower() != 'd':  # Check for valid input
            which_op = input('\nINVALID  -  Enter (e) to ENCRYPT  or (d) to DECRYPT:  ')

        encrypting = (which_op.lower() == 'e') # Assign Boolean Flag

        password_in = input('Enter password: ') # Get password 

        #### perform encryption/decryption
        ## set 'direction' of substitution of letters
        if encrypting:  
            from_index = 0
            to_index = 1
        else:
            from_index = 1
            to_index = 0

        for letter in password_in: # Iterate over input
            letter_found = False  # Init char-search status

            for codex in encryption_key: # Iterate over pairs of letters in the encryption keys
                if ('a' <= letter and letter <= 'z') and letter == codex[from_index]:
                    password_out += codex[to_index] # Append each translated char one-at-a-time
                    letter_found = True # set char-search status

                elif ('A' <= letter and letter <= 'Z') and chr(ord(letter) + 32) == codex[from_index]:
                    password_out += chr(ord(codex[to_index]) - case_changer)    # Append each translated char one-at-a-time
                    letter_found = True # set char-search status
            # Deal with unfound chars
            if not letter_found:
                password_out += letter # Append each non-translated char one-at-a-time

        # Display Output
        if encrypting:
            print('~' * 80)
            print('Your encrypted password is {0}'.format(password_out))
            print('~' * 80)
        else:
            print('~' * 80)
            print('Your dencrypted password is {0}'.format(password_out))
            print('~' * 80)

        # Continue?
        print('Do you want to Encrypt/Decrypt another passphrase?')
        response = input('Enter [y/N]: ')
        
        while response.upper() != 'Y' and response.upper() != 'N':
            response = input('Please ENTER EITHER "y" OR "n": ')
        
        if response.lower() == 'n':
            terminate = True # Terminate program
            
if __name__ == '__main__':
    encrypt_decrypt()

