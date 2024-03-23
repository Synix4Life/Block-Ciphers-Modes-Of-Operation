<h1>Block Cipher Modes Of Operation</h1>

---

![Version](https://img.shields.io/badge/Version-1.0.0-darkblue?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-darkblue?style=flat-square)
![Language](https://img.shields.io/badge/Python-darkblue?style=flat-square&logo=python&logoColor=yellow)

<i>Please read <span style="color: red;">Further Informations</span> before using the provided code!</i>

<a name="section-two"></a>

---
<h2>Description</h2>
The Block Cipher Modes of Operation belongs to the group of symmetric cryptography. 

They can be used to encrypt data with a key and, depending on the mode, also with other parameters.

<h3>Example Implementation </h3>

```python
#Encrpytion using CBC
from encryption_modes import cbc_encryption as cbc

result = cbc("Plaintext", "Key", 0, 3, False)
print(result)
```

---
<h2>Python requirements</h2>
<i>None</i>
---
<h2>Using this implementation</h2>
To use the provided methods, just clone the source code via GitHub and start implementing it in youre own programs.

The provided code supports the file Example.py with predefined example implementations.

---
<h2>Further information</h2>

This is just an implementation of the Block Cipher Modes of Operation. 

<b>Do not under any circumstances use this for any encryption of actual important information nor vulnerable data nor 
send or stored data in general!</b>

The provided methods do not guarantee a safe and flawless encryption of the data and are therefore meant for experimental and 
learning purposes only!

Please use other encryption librarys with proven correctness for encrypting youre data!

<b><i>Never roll your own crypto </i></b>

---

<h3>Miscellaneous</h3>
If you have any other modes you want to be implemented or there are any errors, please feel free to fix them yourself or contact me! :fire:
