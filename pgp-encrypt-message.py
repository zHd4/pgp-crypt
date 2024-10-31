import argparse
import sys

import gnupg

parser = argparse.ArgumentParser(description='PGP messages encryption tool')

parser.add_argument('-e', '--email', type=str, help="Recipient's email")
parser.add_argument('-k', '--key', type=str, help='Path to public key')

args = parser.parse_args()
gpg = gnupg.GPG()


if args.email is None:
    email = input("Recipient's email: ")
else:
    email = args.email

if args.key is None:
    print('Paste your PGP public key here:\n')
    key = sys.stdin.read()
else:
    with open(args.key, 'r') as file:
        key = file.read()

gpg.import_keys(key)

print('\nEnter your message (Ctrl+Enter to move to a new line, Ctrl+C to cancel, Enter to finish):\n')
message_text = sys.stdin.read()

print()
result = gpg.encrypt(message_text, [email])

if result.ok:
    print(result.data)
else:
    print(f'An error occurred: {result.status}')