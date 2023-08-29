# basic-mod1
## Description
We found this weird message being passed around on the servers, we think we have a working decryption scheme. Download the message [here](https://artifacts.picoctf.net/c/129/message.txt). Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore.

## Solution

Firstly, we import the `string` library to create a string, which we later use to map the numbers to:

```python
import string

key = string.ascii_uppercase + string.digits + '_'
```

Now we block read the content of the file *message.txt* and split it into lines:

```python
with open('message.txt') as f:
    lines = f.read().splitlines() 
```

We then iterate through each number in the list, calculate its modulus $37$ and store the results in the new list.
For each modulus result in the new list, we use it as an index to retrieve the corresponding character from the `key` string and append it to the `ans` list.

```python
modded = [int(x)%37 for x in lines]
ans = [key[int(x)] for x in modded]
```

Finally, we use `" ".join(ans)` to concatenate the characters in the `ans` list to form the decrypted message, which is then printed.

```python
print("".join(ans))
```

We get the flag:

```
picoCTF{R0UND_N_R0UND_ADD17EC2}
```




