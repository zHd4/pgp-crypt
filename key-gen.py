import argparse

import pgpy
from pgpy.constants import PubKeyAlgorithm, KeyFlags, HashAlgorithm, CompressionAlgorithm, SymmetricKeyAlgorithm

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="PGP keys generation tool")

    parser.add_argument("name", type=str, help="Your name")
    parser.add_argument("email", type=str, help="Email")
    parser.add_argument("key_size", type=int, help="Key size")

    args = parser.parse_args()

    key = pgpy.PGPKey.new(PubKeyAlgorithm.RSAEncryptOrSign, args.key_size)
    uid = pgpy.PGPUID.new(args.name, email=args.email)

    key.add_uid(uid, usage={KeyFlags.EncryptCommunications, KeyFlags.EncryptStorage},
                hashes=[HashAlgorithm.SHA256], ciphers=[SymmetricKeyAlgorithm.AES256],
                compression=[CompressionAlgorithm.ZLIB])

    with open("private_key.asc", "w") as f:
        f.write(str(key))
    with open("public_key.asc", "w") as f:
        f.write(str(key.pubkey))