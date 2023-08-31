# basic-mod2
## Description
AOur data got corrupted on the way here. Luckily, nothing got replaced, but every block of 3 got scrambled around! The first word seems to be three letters long, maybe you can use that to recover the rest of the message. Download the corrupted message [here](https://artifacts.picoctf.net/c/192/message.txt).

## Solution

The message is:

```
heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V091B0AE}2
```

Looking closely at the first three characters, it's reasonable to assume that the first word in "The", therefore each block of 3 must have been scrambled (permutated) in a following way:

$$012 \rightarrow 201$$

where the numbers $$, $$ and ## represent an index in a 3-long string.

```python
message = "heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V091B0AE}2"

split = [message[i:i+3] for i in range(0,len(message),3)]

decrypted = "".join(["".join([x[2], x[0], x[1]]) for x in split])

print(decrypted)
```


we obrain the orignal data (and the flag!):

```
The flag is picoCTF{7R4N5P051N6_15_3XP3N51V3_109AB02E}
```




