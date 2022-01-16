def encdec(text):
    ans = ""
    for c in text:
        if c >= 'a' and c <= 'z':
            ans += chr( ord('a') + ord('z') - ord(c) )
        elif c >='A' and c <='Z':
            ans += chr( ord('A') + ord('Z') - ord(c) )
        else:
            ans += c
    return ans

print(encdec("+Sahil"))
