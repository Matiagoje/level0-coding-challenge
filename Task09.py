word = "Umuzi"
word = word.lower()
vowels = ("a", "e", "i", "o", "u")
output = ""

print("Vowels: ")
for letter in word:
    if letter not in output:
        output = output + letter
        if letter in vowels:
            print(letter, end= " ")
        else:
            continue
