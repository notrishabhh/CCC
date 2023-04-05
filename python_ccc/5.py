ref = input()
vowels = "aeiou"
blank_str = ""
for i in range(len(ref)):
    if ref[i] in vowels:
        blank_str+=ref[i]*(i+2)
    else:
        blank_str+=ref[i]
print(blank_str)
    