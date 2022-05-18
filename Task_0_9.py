def find_vowels(word):
    word = word.lower()
    vowels = ("a", "e", "i", "o", "u")
    output = ""
    remover = "%s"
    
    for letter in word:
        if letter not in output:
            output = output + letter
            if letter in vowels:
                print(remover % letter, end="")
                remover = ",%s"
            else:
                continue

print("vowels: ")
find_vowels("Umuzi")
