
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