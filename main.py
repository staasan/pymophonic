import argparse
import menu
import read
import key
import encrypt
import decrypt

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pymophonic — homophonic substitution cipher utility written in Python")
    subparsers = parser.add_subparsers(dest="command")
    key_parser = subparsers.add_parser("key", help="Generate key")
    key_parser.add_argument("file_path")
    key_parser.add_argument("new_key_file_path")
    key_parser.add_argument("--codes", type=int, default=256)
    key_parser.add_argument("--bytes", type=int, default=1)
    enc_parser = subparsers.add_parser("encrypt", help="Encrypt file")
    enc_parser.add_argument("file")
    enc_parser.add_argument("key_file")
    dec_parser = subparsers.add_parser("decrypt", help="Decrypt file")
    dec_parser.add_argument("file")
    dec_parser.add_argument("key_file")
    args = parser.parse_args()

    if not args.command:
        menu.main_menu()
    if args.command == "key":
        try:
            open(args.file_path, 'r')
        except FileNotFoundError:
            print("File not found")
            quit()
        print("Reading file...")
        symbols_frequency = read.symbol_frequency(args.file_path, args.codes)
        print("Generating key...")
        key.generate_key_file(symbols_frequency, args.bytes, args.new_key_file_path)
        print(f"New key file {args.new_key_file_path}.pymo has been generated")
    if args.command == "encrypt":
        try:
            open(args.file, 'r')
        except FileNotFoundError:
            print("File for encryption not found")
            quit()
        try:
            open(args.key_file, 'r')
            if not args.key_file.endswith(".pymo"):
                print("Not key file selected")
                quit()
        except FileNotFoundError:
            print("Key file not found")
            quit()
        print("Encrypting file...")
        encrypted_file_name = encrypt.encrypt(args.file, args.key_file)
        print(f"File was encrypted. {encrypted_file_name}")
    if args.command == "decrypt":
        try:
            open(args.file, 'r')
        except FileNotFoundError:
            print("File for decryption not found")
            quit()
        try:
            open(args.key_file, 'r')
            if not args.key_file.endswith(".pymo"):
                print("Not key file selected")
                quit()
        except FileNotFoundError:
            print("Key file not found")
            quit()
        print("Decrypting file...")
        decrypted_file_name = decrypt.decrypt(args.file, args.key_file)
        print(f"File {decrypted_file_name} was decrypted")