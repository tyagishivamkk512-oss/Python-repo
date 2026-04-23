def greeting(day_part,name):
    if day_part == 'evening':
        print(f"Good {day_part} {name}, the sun is about to set.")
        return
    elif day_part=='morning':
        print(f"Good {day_part} {name}, the sun is rising.")
        return

your_name = input("Enter your name: ")
part = input("morning/evening: ")
greeting(part,your_name)

# these are also positional arguments in which the order matters in which we are passing them