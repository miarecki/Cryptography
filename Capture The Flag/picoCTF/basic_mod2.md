# basic-mod2
## Description
A new modular challenge! Download the message.txt [here](https://artifacts.picoctf.net/c/179/message.txt). Take each number mod 41 and find the modular inverse for the result. Then map to the following character set: 1-26 are the alphabet, 27-36 are the decimal digits, and 37 is an underscore.

## Solution

  Firstly, we need to import some libraries:
  + `string` for the alphabet and digit strings.
  + `from Crypto.Util.number import inverse` fto calculate modular inverses.

Next, we import the numbers from *message.txt* into a list. 

```python
with open("message.txt", 'r') as f:
    numbers = [[int(num) for num in line.split()] for line in f][0]
```


Then, calculate modular (multiplicative) inverses mod $41$ for each of them. In other words, we need to find an integer $a$ such that $ax \equiv 1 \pmod{41}$ 

```python
numbers_inv_mod41 = [inverse(x,41) for x in numbers]
```
Now, let's map the numbers from `numbers_inv_mod41` as requested using a list comprehension:

```python
result = [
    alphabet[x - 1] if x <= 26 else digits[x % 27] if x != 37 else "_"
    for x in numbers_inv_mod41
]
```

Finally, we print out the flag:

```python
flag = "".join(result)
print(f'picoCTF\u007b{flag}\u007d')
```

which turns out to be:
```
picoCTF{1nv3r53ly_h4rd_dadaacaa}
```





