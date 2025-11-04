key = 3
choice = input("Enter 'e' to encode or 'd' to decode: ")
text = input("Enter message: ")
shift = key if choice[0] == "e" else -key
result = ""
for ch in text:
    code = ord(ch)
    if 97 <= code <= 122:  # a-z
        result += chr((code - 97 + shift) % 26 + 97)
    elif 65 <= code <= 90:  # A-Z
        result += chr((code - 65 + shift) % 26 + 65)
    else:
        result += ch
print(result)