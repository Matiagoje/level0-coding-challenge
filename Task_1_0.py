def common_letters(first_string, second_string):
    first_string = first_string.lower()
    second_string = second_string.lower()
    remover = "%s"
    
    for letters in first_string:
        for characters in second_string:
            if letters == characters:
                print(remover % characters, end = "")
                remover = ",%s"
            else:
                continue
        
print("common letters: ")
common_letters("house","computers")