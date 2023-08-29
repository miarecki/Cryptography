# basic-mod2
## Description
A new modular challenge! Download the message.txt [here](https://artifacts.picoctf.net/c/179/message.txt). Take each number mod 41 and find the modular inverse for the result. Then map to the following character set: 1-26 are the alphabet, 27-36 are the decimal digits, and 37 is an underscore.

## Solution

  Firstly, let's import some libraries:
  + `string` for the alphabet and digits strings
  + `from Crypto.Util.number import inverse` for calculating modular inverses

Then let's import numbers from *message.txt* into a list. 

```
with open("message.txt", 'r') as f:
    numbers = [[int(num) for num in line.split()] for line in f][0]
```

Calculate modular (multiplicative) inverse inverses mod $41$ for each of them; that is we need to find an integer $a$ such that $ax \equiv 1 \pmod{41}$ 

```
numbers_inv_mod41 = [inverse(x,41) for x in numbers]
```
Now let's map our numbers from `numbers_inv_mod41` as requested using list comprehension:

```
result = [
    alphabet[x - 1] if x <= 26 else digits[x % 27] if x != 37 else "_"
    for x in numbers_inv_mod41
]
```

Now to print out the flag:

```
flag = "".join(result)
print(f'picoCTF\u007b{flag}\u007d')
```

We get
```
picoCTF{1nv3r53ly_h4rd_dadaacaa}
```





