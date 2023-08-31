# substitution0
## Description
A message has come in, but it seems to be all scrambled. Luckily it seems to have the key at the beginning. Can you crack this substitution cipher? Download the message [here](https://artifacts.picoctf.net/c/152/message.txt).

## Solution

This is a very simple substitution cipher where even the key which was used for encryption is known. Here is a Python solution:

```python
import string

key = 'DECKFMYIQJRWTZPXGNABUSOLVH' + 'DECKFMYIQJRWTZPXGNABUSOLVH'.lower()
alpha = string.ascii_uppercase + string.ascii_lowercase

def decryption(data):

	return "".join([alpha[key.find(x)] if x in key else x for x in data])


print(decryption("xqcpCBM{5UE5717U710Z_3S0WU710Z_59533D2F}"))
```
Using `key` and `alpha` strings, we map D $\rightarrow$ A, E $\rightarrow$ B, k $\rightarrow$ d, etc. Characters that don't appear in the Latin alphabet remain unchanged.

The flag we obtain is:

```
picoCTF{5UB5717U710N_3V0LU710N_59533A2E}
```




