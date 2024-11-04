<h1>pgp-crypt</h1>
<p>Collection of PGP Python scripts</p>

<h2>Usages</h2>

<h3>pgp-keys-gen.py</h3>

```text
usage: pgp-keys-gen.py [-h] email key_size

PGP keys generation tool

positional arguments:
  email       Email
  key_size    Key size

options:
  -h, --help  show this help message and exit
```

<h3>pgp-encrypt-message.py</h3>

```text
usage: pgp-encrypt-message.py [-h] email key_path

PGP messages encryption tool

positional arguments:
  email       Recipient's email
  key_path    Path to public key

options:
  -h, --help  show this help message and exit
```

<h3>pgp-decrypt-message.py</h3>

```text
usage: pgp-decrypt-message.py [-h] email key_path

PGP messages decryption tool

positional arguments:
  email       Recipient's email
  key_path    Path to private key

options:
  -h, --help  show this help message and exit
```

<h3>pgp-encrypt-file.py</h3>

```text
usage: pgp-encrypt-file.py [-h] [-o OUTPUT_PATH] [-a] email public_key_path input_file_path

PGP file encryption tool

positional arguments:
  email                 Recipient's email
  public_key_path       Path to public key
  input_file_path       Path to file to be encrypted

options:
  -h, --help            show this help message and exit
  -o OUTPUT_PATH, --output-path OUTPUT_PATH
                        Output path
  -a, --armor           Text output
```

<h3>pgp-decrypt-file.py</h3>

```text
usage: pgp-decrypt-file.py [-h] [-o OUTPUT_PATH] private_key_path encrypted_file_path

PGP file decryption tool

positional arguments:
  private_key_path      Path to private key
  encrypted_file_path   Path to encrypted file

options:
  -h, --help            show this help message and exit
  -o OUTPUT_PATH, --output-path OUTPUT_PATH
                        Output path
```