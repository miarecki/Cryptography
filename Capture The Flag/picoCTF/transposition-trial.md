# transposition-trial
## Description
Our data got corrupted on the way here. Luckily, nothing got replaced, but every block of $3$ got scrambled around! The first word seems to be three letters long, maybe you can use that to recover the rest of the message. Download the corrupted message [here](https://artifacts.picoctf.net/c/192/message.txt).

## Solution

The message is:

```
heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V091B0AE}2
```

Upon close examination of the first three characters, it's reasonable to assume that the first word is *"The"*. Therefore, each block of $3$ must have been scrambled (permutated) in the following way:

$$012 \rightarrow 201$$

where the numbers $0$, $1$ and $2$ represent an index in a string of length $3$.

Here is a solution in Python. Note that we split the message into blocks of $3$ and then we take each character in those blocks and permute them as described above.

```python
message = "heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V091B0AE}2"

split = [message[i:i+3] for i in range(0,len(message),3)]

decrypted = "".join(["".join([x[2], x[0], x[1]]) for x in split])

print(decrypted)
```

We obtain the original data (and the flag!):

```
The flag is picoCTF{7R4N5P051N6_15_3XP3N51V3_109AB02E}
```




