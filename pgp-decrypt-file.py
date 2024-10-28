import argparse
import os
from getpass import getpass

import gnupg

parser = argparse.ArgumentParser(description='PGP decryption tool')

parser.add_argument('private_key_path', type=str, help='Path to private key')
parser.add_argument('encrypted_file_path', type=str, help='Path to encrypted file')
parser.add_argument('-o', '--output-path', type=str, help='Output path')

args = parser.parse_args()
gpg = gnupg.GPG()

if args.output_path is not None:
    if os.path.isdir(args.output_path):
        output_path = os.path.join(args.output_path, os.path.basename(args.encrypted_file_path) + '.gpg')
    else:
        output_path = args.output_path
else:
    output_path = args.encrypted_file_path + '.gpg'

print('Importing key...')

with open(args.private_key_path) as file:
    gpg.import_keys(file.read())

password = getpass('Password: ')

with open(args.encrypted_file_path, 'rb') as file:
    print('Decrypting...')
    status = gpg.decrypt_file(file, passphrase=password, output=output_path)

if status.ok:
    print(f'File encrypted! Saved to: {output_path}')
else:
    print(f'An error occurred: {status.status}')