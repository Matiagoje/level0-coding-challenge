def number_to_hours_mins(num):
    hours = num//60
    minutes = num % 60
    if hours > 1 :
        if minutes > 1 or minutes == 0:
            print(f"{hours} hours, {minutes} minutes")
        else:
            print(f"{hours} hours, {minutes} minute")
    if hours <= 1:
        if minutes > 1 or minutes == 0:
            print(f"{hours} hour, {minutes} minutes")
        else:
            print(f"{hours} hour, {minutes} minute")
                   
number_to_hours_mins(1)
