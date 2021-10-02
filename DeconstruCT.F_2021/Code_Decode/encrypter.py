from random import choice

inputstring = input("Enter plaintext: ")

# Reads 'cypher.txt' and selects a random key and its corresponding value and returns them
def read_encryption_details():
    with open("cypher.txt") as file:
        encrypt_text = eval(file.read())
        encrypt_key = choice(list(encrypt_text.keys()))
        character_key = encrypt_text[encrypt_key]
    return encrypt_key, character_key

# Returns a dictionary with each letter from charstring as key and each corresponding letter from character_key(value returned from above func) as a value #Max_length of flag is 45 as the length of charstring is 45 and zip function always considers the smallest string or list as its size-limitting structure
def create_encryption(character_key):
    charstring = "abcdefghijklmnopqrstuvwxyz1234567890 _+{}-,.:"
    final_encryption = {}
    for i, j in zip(charstring, character_key):
        final_encryption[i] = j
    return final_encryption

# Returns cipher text in the form of key[:3]+cypher_text+key[3:]
def convert_plaintext_to_cypher(inputstring, final_encryption, encrypt_key):
    cypher_text = ""
    for i in inputstring:
        cypher_text += final_encryption[i]
    cypher_text = encrypt_key[:3] + cypher_text + encrypt_key[3:]
    return cypher_text


encrypt_key, character_key = read_encryption_details()
final_encryption = create_encryption(character_key)
cypher_text = convert_plaintext_to_cypher(inputstring, final_encryption, encrypt_key)

print(cypher_text)
