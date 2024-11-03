import argparse
from getpass import getpass

import gnupg

parser = argparse.ArgumentParser(description='PGP messages decryption tool')

parser.add_argument('email', type=str, help="Recipient's email")
parser.add_argument('key_path', type=str, help='Path to private key')

args = parser.parse_args()
gpg = gnupg.GPG()


def multiline_input(message: str) -> str:
    print(message)
    contents = []

    while True:
        try:
            line = input()
        except EOFError:
            break

        contents.append(line)

    return '\n'.join(contents)


with open(args.key_path, 'r') as file:
    key = file.read()

gpg.import_keys(key)

password = getpass('Password: ')
encrypted_message = multiline_input('Paste your encrypted PGP message block and press Ctrl-D or Ctrl-Z (Windows)')
result = gpg.decrypt(encrypted_message, passphrase=password)

print()

if result.ok:
    print(result.data.decode('utf-8'))
else:
    print(f'An error occurred: {result.status}')
