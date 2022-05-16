num = int(input())

def number_to_hours_mins(num):
    hours = num//60
    minutes = num % 60
    print(hours, " hour(s), ", minutes, " minutes.")

number_to_hours_mins(num)
