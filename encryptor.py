import argparse
import os

import gnupg

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='PGP encryption tool')

    parser.add_argument('email', type=str, help="Recipient's email")
    parser.add_argument('public_key_path', type=str, help='Path to public key')
    parser.add_argument('input_file_path', type=str, help='Path to file to be encrypted')
    parser.add_argument('-o', '--output-path', type=str, help='Output path')
    parser.add_argument('-a', '--armor', action='store_true', help='Text output')

    args = parser.parse_args()
    gpg = gnupg.GPG()

    if args.output_path is not None:
        if os.path.isdir(args.output_path):
            output_path = os.path.join(args.output_path, os.path.basename(args.input_file_path) + '.gpg')
        else:
            output_path = args.output_path
    else:
        output_path = args.input_file_path + '.gpg'

    with open(args.public_key_path) as file:
        gpg.import_keys(file.read())

    with open(args.input_file_path, 'rb') as file:
        print('Encrypting...')
        status = gpg.encrypt_file(file, recipients=[args.email], output=output_path, armor=args.armor)

    if status.ok:
        print(f'File encrypted! Saved to: {output_path}')
    else:
        print(f'An error occurred: {status.status}')