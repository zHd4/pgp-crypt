import argparse
import os

import gnupg

def get_password() -> str or None:
    user_password = input('Password: ')
    password_confirmation = input('Confirm password: ')

    if user_password == password_confirmation:
        return user_password


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='PGP keys generation tool')

    parser.add_argument('email', type=str, help='Email')
    parser.add_argument('key_size', type=int, help='Key size')

    args = parser.parse_args()
    gpg = gnupg.GPG()

    password = get_password()

    if password is None:
        print("Passwords don't match")
        exit()

    print('Generating...')

    input_data = gpg.gen_key_input(name_email=args.email, passphrase=password)
    key = gpg.gen_key(input_data)

    output_dir_path = f'{args.email}'

    if not os.path.isdir(output_dir_path):
        os.mkdir(output_dir_path)

    with open(f'{output_dir_path}/public.asc', 'w') as f:
        f.write(gpg.export_keys(key.fingerprint))

    with open(f'{output_dir_path}/private.asc', 'w') as f:
        f.write(gpg.export_keys(key.fingerprint, True, passphrase=password))

    print(f'Saved to: "{os.path.abspath(output_dir_path)}"')