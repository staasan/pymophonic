import os
import read
import key
import encrypt
import decrypt
from tkinter import filedialog

def key_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Select file for key generation")
    selected_file_name = filedialog.askopenfilename()
    print("Select which name key file should have and its save path")
    key_file_name = filedialog.asksaveasfilename()
    codes_amount = int(input("How many codewords key file should have? "))
    code_bytes = int(input("How many bytes codeword in key should have? "))
    print("File reading...")
    symbols_frequency = read.symbol_frequency(selected_file_name,codes_amount)
    print("Key generation...")
    key_file_name = key.generate_key_file(symbols_frequency,code_bytes,key_file_name)
    print(f"Key file {key_file_name} was generated!")
    print("Press Enter to continue...")
    input()
    os.system('cls' if os.name == 'nt' else 'clear')
    main_menu()


def enc_menu():
    os.system('cls')
    print("Select file to encrypt")
    selected_file_name = filedialog.askopenfilename()
    print("Select key file")
    key_file_name = ""
    while ".pymo" not in key_file_name:
        key_file_name = filedialog.askopenfilename()
        if "pymo" in key_file_name: break
        else: print("Selected file is not a key file")
    print("Encrypting...")
    encrypted_file_name = encrypt.encrypt(selected_file_name,key_file_name)
    print(f"File was encrypted! {encrypted_file_name}")
    print("Press Enter to continue...")
    input()
    os.system('cls'*(os.name == "nt")+"clear"*(os.name == "posix"))
    main_menu()

def dec_menu():
    os.system('cls')
    print("Selected encrypted file")
    selected_file_name = filedialog.askopenfilename()
    print("Select key file")
    key_file_name = ""
    while ".pymo" not in key_file_name:
        key_file_name = filedialog.askopenfilename()
        if ".pymo" in key_file_name:
            break
        else:
            print("Selected file is not a key file")
    print("Decrypting...")
    decrypted_file_name = decrypt.decrypt(selected_file_name, key_file_name)
    print(f"File {decrypted_file_name} was decrypted")
    print("Press Enter to continue...")
    input()
    os.system('cls'*(os.name == "nt")+"clear"*(os.name == "posix"))
    main_menu()


def main_menu():
    print("Pymophonic ver. 1.0.0. Execute main.py -h to read manual")
    while True:
        pressed_key = input("\n[1] Key generation \n[2] File encryption \n[3] File decryption\n[4] Quit\n")[0]
        match pressed_key:
            case "1":
                key_menu()
            case "2":
                enc_menu()
            case "3":
                dec_menu()
            case "4":
                quit()
            case _:
                os.system('cls'*(os.name == "nt")+"clear"*(os.name == "posix"))
                print("Invalid input")
