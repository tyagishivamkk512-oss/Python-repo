def greetings(greeting,title,first,last):
    print(f"{greeting} {title}{first} {last}")

greetings("Hello","Mr.","Shivam","Tyagi")
greetings(title="Mr.",greeting="Hello",last="Tyagi",first="Shivam")
#we add keyword to every argument we pass so the order doesn't matter

greetings("Hello",title="Mr.",last="Tyagi",first="Shivam")
#if we are passing positional aargument, it should be before keyword argument