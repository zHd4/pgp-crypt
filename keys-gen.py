import argparse
import os
from getpass import getpass
import gnupg


def get_password() -> str or None:
    password = getpass('Password: ')
    password_confirmation = getpass('Confirm password: ')

    if password == password_confirmation:
        return password


parser = argparse.ArgumentParser(description='PGP keys generation tool')

parser.add_argument('email', type=str, help='Email')
parser.add_argument('key_size', type=int, help='Key size')

args = parser.parse_args()
gpg = gnupg.GPG()

key_password = get_password()

if key_password is None:
    print("Passwords don't match")
    exit()

print('Generating...')

input_data = gpg.gen_key_input(name_email=args.email, passphrase=key_password)
key = gpg.gen_key(input_data)

output_dir_path = f'{args.email}'

if not os.path.isdir(output_dir_path):
    os.mkdir(output_dir_path)

with open(f'{output_dir_path}/public.asc', 'w') as f:
    f.write(gpg.export_keys(key.fingerprint))

with open(f'{output_dir_path}/private.asc', 'w') as f:
    f.write(gpg.export_keys(key.fingerprint, True, passphrase=key_password))

print(f'Saved to: "{os.path.abspath(output_dir_path)}"')
