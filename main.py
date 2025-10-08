import argparse
import menu
import read
import key
import encrypt
import decrypt

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pymophonic — Простая утилита на языке Python для шифрования файлов омофонической заменой")
    subparsers = parser.add_subparsers(dest="command")
    key_parser = subparsers.add_parser("key", help="Генерация ключа")
    key_parser.add_argument("file_path")
    key_parser.add_argument("new_key_file_path")
    key_parser.add_argument("--codes", type=int, default=256)
    key_parser.add_argument("--bytes", type=int, default=1)
    enc_parser = subparsers.add_parser("encrypt", help="Зашифровать файл")
    enc_parser.add_argument("file")
    enc_parser.add_argument("key_file")
    dec_parser = subparsers.add_parser("decrypt", help="Расшифровать файл")
    dec_parser.add_argument("file")
    dec_parser.add_argument("key_file")
    args = parser.parse_args()

    if not args.command:
        menu.main_menu()
    if args.command == "key":
        if 16**(args.bytes*2) < args.codes:
            print(f"Невозможно сгенерировать {args.codes} ключей из {args.bytes} байт.\nВыберите другие значения.")
            quit()
        if args.codes < 66:
            print(f"Файл шифруется в формате base32. Омофоническая замена невозможна если кодов меньше 66.\nВыберите другое значение.")
            quit()
        try:
            open(args.file_path, 'r')
        except FileNotFoundError:
            print("Файл не найден")
            quit()
        print("Чтение файла...")
        symbols_frequency = read.symbol_frequency(args.file_path, args.codes)
        print("Генерация ключа...")
        key.generate_key_file(symbols_frequency, args.bytes, args.new_key_file_path)
        print(f"Новый файл ключа {args.new_key_file_path}.pymo сгенерирован")
    if args.command == "encrypt" or args.command == "decrypt":
        try:
            open(args.file, 'r')
        except FileNotFoundError:
            print("Файл не найден")
            quit()
        try:
            open(args.key_file, 'r')
            if not args.key_file.endswith(".pymo"):
                print("Выбранный файл не является ключом")
                quit()
        except FileNotFoundError:
            print("Ключ не найден")
            quit()
        if args.command == "encrypt":
            print("Шифрование файла...")
            encrypted_file_name = encrypt.encrypt(args.file, args.key_file)
            print(f"Файл зашифрован. {encrypted_file_name}")
        else:
            print("Расшифрование файла...")
            decrypted_file_name = decrypt.decrypt(args.file, args.key_file)
            print(f"Файл {decrypted_file_name} расшифрован")

