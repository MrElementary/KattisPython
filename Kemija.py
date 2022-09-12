text = input()
plaintext = ""
skip = 0

for i in text:
    if 0 < skip:
        skip -= 1
        continue

    if i in "aeiou":
        skip = 2

    plaintext += i

print(plaintext)
