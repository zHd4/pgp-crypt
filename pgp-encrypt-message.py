import argparse

import gnupg

parser = argparse.ArgumentParser(description='PGP messages encryption tool')

parser.add_argument('-e', '--email', type=str, help="Recipient's email")
parser.add_argument('-k', '--key', type=str, help='Path to public key')

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


if args.email is None:
    email = input("Recipient's email: ")
else:
    email = args.email

if args.key is None:
    key = multiline_input('Paste your PGP public key here:\n')
else:
    with open(args.key, 'r') as file:
        key = file.read()

gpg.import_keys(key)

message_text = multiline_input('\nEnter your message '
                               '(Ctrl+Enter to move to a new line, '
                               'Ctrl+C to cancel, Enter to finish):\n')

print()
result = gpg.encrypt(message_text, [email])

if result.ok:
    print(result.data.decode('utf-8'))
else:
    print(f'An error occurred: {result.status}')
