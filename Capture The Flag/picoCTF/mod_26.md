# Mod 26
## Description
Cryptography can be easy, do you know what ROT13 is? 

## Solution

  Firstly, we need to import library `string` for the uppercase and lowercase alphabet strings.


```python
import string

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
```


Then, define `rot13` function that takes a string as an input and encrypt/decrypt it using a list comprehension. For more info, please refer to [Cryptography/Ciphers/ROT13](https://github.com/miarecki/Cryptography/tree/main/Ciphers/ROT13):


```python
def rot13(data):

	new_data = [uppercase[(uppercase.find(c)+13) % 26] if c in uppercase
				 else lowercase[(lowercase.find(c)+13)%26] if c in lowercase
				 else c for c in data]
	return "".join(new_data)
```

Finally, we print out the flag:

```python
print("".join(rot13('cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_uJdSftmh}')))
```

which turns out to be:
```
picoCTF{next_time_I'll_try_2_rounds_of_rot13_hWqFsgzu}
```






