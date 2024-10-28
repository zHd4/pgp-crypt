import argparse

parser = argparse.ArgumentParser(description='PGP decryption tool')

parser.add_argument('private_key_path', type=str, help='Path to private key')
parser.add_argument('input_file_path', type=str, help='Path to file to be decrypted')
parser.add_argument('-o', '--output-path', type=str, help='Output path')