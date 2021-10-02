# Code Decode

---

(Cryptography, 250, 74 Solves)

Around 5 years ago, I made this killer program that encodes the string into a cyphertext. The unique feature of this program is that for the same exact plaintext, it generates a different cyphertext every time you run the program. Yesterday I was nosing around in some old stuff and found an encrypted message!

`2njlgkma2bv1i0v}22lv19vuo19va2bvl2{-5x`

Sadly I realized that I lost the decryption program. I have the encryption program though. Do you think you can help me out and decrypt this message for me?

[cypher.txt](https://github.com/gddaredevil/writeups/blob/master/DeconstruCT.F_2021/Code_Decode/cypher.txt) &emsp; [encrypter.py](https://github.com/gddaredevil/writeups/blob/master/DeconstruCT.F_2021/Code_Decode/encrypter.py) &emsp; [encrypted_text.txt](https://github.com/gddaredevil/writeups/blob/master/DeconstruCT.F_2021/Code_Decode/encrypted_text.txt)

---

### Investigation

Proper Analysis of the code is provided in the encrypter.py file.
`cypher.txt` contains data in key:value pairs. The length of each key is 6 characters. 
The value associated with each key contains a string with printable ASCII characters in random positions.
There's a charstring of lowercase alphabets, numbers and a few special characters in the program. Each alphabet in the charstring is mapped to each character in any of the values in the `cypher.txt` and a new cipher text is obtained.
The first half and second half of the key, whose value is used in making the cipher text, is prepended and appended to the cipher text respectively. 

The pattern will be similar to: `key[:3] + cipher_text + key[3:]`

So, proper analysis of the provided encrypted message `2njlgkma2bv1i0v}22lv19vuo19va2bvl2{-5x` reveals that

Key: `2nj-5x`

Cipher_text: '`lgkma2bv1i0v}22lv19vuo19va2bvl2{`

The value corresponding to this key in `cypher.txt`: `cxkl,_}o 4+tzrwe7ig9bfu5a-sy01.hpn628v3m{d:jq`

The charstring in the program: `abcdefghijklmnopqrstuvwxyz1234567890 _+{}-,.:`

So, I wrote a tiny python program called 'decrypter.py' to traverse cipher_text and search for each of its char in value of key-value pair and replace the char with the corresponding element in the charstring.

The flag obtained after decryption was:

`dsc{y0u_4r3_g00d_4t_wh4t_y0u_d0}`


