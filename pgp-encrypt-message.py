import argparse

import gnupg

parser = argparse.ArgumentParser(description='PGP messages encryption tool')

parser.add_argument('email', type=str, help="Recipient's email")
parser.add_argument('key_path', type=str, help='Path to public key')

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

message_text = multiline_input('Enter/Paste your content. Ctrl-D or Ctrl-Z (Windows) to finish.')
result = gpg.encrypt(message_text, [args.email])

print()

if result.ok:
    print(result.data.decode('utf-8'))
else:
    print(f'An error occurred: {result.status}')
