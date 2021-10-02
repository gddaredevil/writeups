cipher = "2njlgkma2bv1i0v}22lv19vuo19va2bvl2{-5x"
key = cipher[:3]+cipher[-3:]
enc_str = cipher[3:-3]
file = open("cypher.txt","r")
dict = eval(file.read())
value = dict[key]
charstring = "abcdefghijklmnopqrstuvwxyz1234567890 _+{}-,.:"
decrypted_msg = ""
for i in enc_str:
    decrypted_msg += charstring[value.index(i)]
print(decrypted_msg)
