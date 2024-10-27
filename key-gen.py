import argparse
import os

import pgpy
from pgpy.constants import PubKeyAlgorithm, KeyFlags, HashAlgorithm, CompressionAlgorithm, SymmetricKeyAlgorithm

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='PGP keys generation tool')

    parser.add_argument('name', type=str, help='Your name')
    parser.add_argument('email', type=str, help='Email')
    parser.add_argument('key_size', type=int, help='Key size')

    args = parser.parse_args()

    print('Generating...')

    key = pgpy.PGPKey.new(PubKeyAlgorithm.RSAEncryptOrSign, args.key_size)
    uid = pgpy.PGPUID.new(args.name, email=args.email)

    key.add_uid(uid, usage={KeyFlags.EncryptCommunications, KeyFlags.EncryptStorage},
                hashes=[HashAlgorithm.SHA256], ciphers=[SymmetricKeyAlgorithm.AES256],
                compression=[CompressionAlgorithm.ZLIB])

    output_dir_path = f'{args.name} <{args.email}>'

    if not os.path.isdir(output_dir_path):
        os.mkdir(output_dir_path)

    with open(f'{output_dir_path}/private.asc', 'w') as f:
        f.write(str(key))

    with open(f'{output_dir_path}/public.asc', 'w') as f:
        f.write(str(key.pubkey))

    print(f'Saved to: "{os.path.abspath(output_dir_path)}"')