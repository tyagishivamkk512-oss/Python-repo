
try: # to prevent errors
    a = int(input("Enter inteager :"))
    print(1/a)

except ZeroDivisionError:
    print("number can't be divided by zero")

except ValueError:
    print("only inteager allowed")

except Exception: # takes every error possible
    print("Something went wrong !")

finally: # runs everytime
    print("...")

# we can also use else with exception to print something if exception doesn't occur
# and we can raise exceptions like 
# age = -5
# if age < 0:
#   raise ValueError("Age can't be negative")
