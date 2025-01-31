# Block Cipher Modes Of Operation

---

![Version](https://img.shields.io/badge/Version-1.3.2-blue?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)
![Tests](https://img.shields.io/badge/Tests-Passed_(55/55)-blue?style=flat-square)
![Language](https://img.shields.io/badge/Python-blue?style=flat-square&logo=python&logoColor=yellow)

<i>Please read <span style="color: red;">Further Informations</span> before using the provided code!</i>

<a name="section-two"></a>

---
## Description
The Block Cipher Modes of Operation belongs to the group of symmetric cryptography. 

They can be used to encrypt data with a key and, depending on the mode, also with other parameters.

### Example Implementation

```python
#Encrpytion and decryption using CBC
from src.encryption_modes import cbc_encryption
from src.decryption_modes import cbc_decryption
from src.Essentials.converter import hex_to_ascii

encrypted = cbc_encryption("Plaintext", "Key", 0, 3)

print(encrypted)
print(hex_to_ascii(encrypted))

decrypted = cbc_decryption(
    hex_to_ascii(encrypted), "Key", 0, 3, True
)

print(decrypted)
```

```
-------------- CONSOLE OUTPUT ---------------
    >> 1B0918390215171F18
    >> 	9
    >> Plaintext
```

---

## Python requirements
<i>None</i>

---

## Using this implementation
To use the provided methods, just clone the source code via GitHub and start implementing it in youre own programs.

The provided code supports the file Example.py with predefined example implementations.

---
## Further information

This is just an implementation of the Block Cipher Modes of Operation. 

<b>Do not under any circumstances use this for any encryption of actual important information nor vulnerable data nor 
send or stored data in general!</b>

The provided methods do not guarantee a safe and flawless encryption of the data and are therefore meant for experimental and 
learning purposes only!

Please use other encryption librarys with proven correctness for encrypting youre data!

<b><i>Never roll your own crypto </i></b>

---

### Miscellaneous
If you have any other modes you want to be implemented or there are any errors, please feel free to fix them yourself or contact me! :fire:

---

## Changelog

- $\textsf{\color{aqua}Version 1.0.0}$
  - Basic encryption and decryption featuring the modes:
    - CBC
    - CTR
    - ECB
  - Necessary dependencies
  - $\textsf{\color{aqua}Version 1.1.0}$
    - Docstring fix
    - Added direct ASCII output from the methods
    - UPLOADED TESTS
    - $\textsf{\color{aqua}Version 1.1.1}$
      - \_\_pycache\_\_ added to .gitignore
    - $\textsf{\color{aqua}Version 1.1.2}$
      - File design (naming Imports and Methods)
      - README.txt example implementation extension
      - Testing Encryption Exceptions
      - Small fixes
    - $\textsf{\color{aqua}Version 1.1.3}$
      - File structure changed
    - $\textsf{\color{aqua}Version 1.1.4}$
      - Added Example Outputs
    - $\textsf{\color{aqua}Version 1.1.5}$
      - Changelog to README
    - $\textsf{\color{aqua}Version 1.1.6}$
      - Added a test count to README
  - $\textsf{\color{aqua}Version 1.2.0}$
    - Converted the directories to packages
    - Moved the tests to a dedicated folder
  - $\textsf{\color{aqua}Version 1.3.0}$
    - Cleanup
    - Added preprocessing to simplify code
    - $\textsf{\color{aqua}Version 1.3.1}$
      - Further Cleanup
    - $\textsf{\color{aqua}Version 1.3.2}$
      - Small README changes
