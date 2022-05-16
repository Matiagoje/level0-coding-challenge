first_string = "house"
second_string = "computers"

print("common letters: ")
for i in first_string:
    for x in second_string:
        if i == x:
            print(x, end = " , ")
        else:
            continue