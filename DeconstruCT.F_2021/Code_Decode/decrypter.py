cipher = "lgkma2bv1i0v}22lv19vuo19va2bvl2{"
value = "cxkl,_}o 4+tzrwe7ig9bfu5a-sy01.hpn628v3m{d:jq"
charstring = "abcdefghijklmnopqrstuvwxyz1234567890 _+{}-,.:"
decrypted_msg = ""
for i in cipher:
    decrypted_msg += charstring[value.index(i)]
print(decrypted_msg)
