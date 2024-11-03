import argparse

import gnupg

parser = argparse.ArgumentParser(description='PGP messages encryption tool')

parser.add_argument('email', type=str, help="Recipient's email")
parser.add_argument('key', type=str, help='Path to public key')

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

with open(args.key, 'r') as file:
    key = file.read()

gpg.import_keys(key)

message_text = multiline_input('\nEnter your message '
                               '(Ctrl+Enter to move to a new line, '
                               'Ctrl+C to cancel, Enter to finish):\n')

print()
result = gpg.encrypt(message_text, [args.key])

if result.ok:
    print(result.data.decode('utf-8'))
else:
    print(f'An error occurred: {result.status}')
