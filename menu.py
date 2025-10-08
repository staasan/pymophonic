import os
import read
import key
import encrypt
import decrypt
try:
    from tkinter import filedialog
except ModuleNotFoundErrorx:
    print("Библиотека tkinter для Python не найдена. Установите её")
    quit()


def key_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Выберите файл")
    selected_file_name = filedialog.askopenfilename()
    print("Куда сохранить ключ?")
    key_file_name = filedialog.asksaveasfilename()
    while True:
        codes_amount = int(input("Сколько кодовых слов должно быть в ключе?"))
        code_bytes = int(input("Сколько байт должно содержать одно кодовое слово?"))
        if 16**code_bytes < codes_amount:
            print(f"Невозможно сгенерировать {codes_amount} ключей из {codes_byte} байт/n Выберите другие значения.")
    print("Чтение файла...")
    symbols_frequency = read.symbol_frequency(selected_file_name,codes_amount)
    print("Генерация ключа...")
    key_file_name = key.generate_key_file(symbols_frequency,code_bytes,key_file_name)
    print(f"Файл ключа {key_file_name} сгенерирован")
    print("Нажмите Enter для продолжения...")
    input()
    os.system('cls' if os.name == 'nt' else 'clear')
    main_menu()


def enc_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Выберите файл")
    selected_file_name = filedialog.askopenfilename()
    print("Выберите ключ")
    key_file_name = ""
    while ".pymo" not in key_file_name:
        key_file_name = filedialog.askopenfilename()
        if "pymo" in key_file_name: break
        else: print("Выбранный файл не является ключом")
    print("Шифрование файла...")
    encrypted_file_name = encrypt.encrypt(selected_file_name,key_file_name)
    print(f"Файл зашифрован. {encrypted_file_name}")
    print("Нажмите Enter для продолжения...")
    input()
    os.system('cls' if os.name == 'nt' else 'clear')
    main_menu()

def dec_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Выберите файл")
    selected_file_name = filedialog.askopenfilename()
    print("Выберите ключ")
    while True:
        key_file_name = filedialog.askopenfilename()
        if ".pymo" in key_file_name:
            break
        print("Selected file is not a key file")
    print("Расшифрование файла...")
    try:
        decrypted_file_name = decrypt.decrypt(selected_file_name, key_file_name)
    except KeyError:
        print("Неверный ключ")
        print("Нажмите Enter для продолжения...")
        input()
        os.system('cls' if os.name == 'nt' else 'clear')
        main_menu()
        
    print(f"File {decrypted_file_name} was decrypted")
    print("Нажмите Enter для продолжения...")
    input()
    os.system('cls' if os.name == 'nt' else 'clear')
    main_menu()


def main_menu():
    print("Pymophonic. Запустите файл main.py с аргументом -h чтобы прочитать руководство")
    while True:
        pressed_key = input("\n[1] Генерация ключа \n[2] Шифрование файла \n[3] Дешифрование файла\n[4] Выход\n")[0]
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
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Неверный ввод")



