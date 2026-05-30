class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    # Controls how object looks when printed
    def __str__(self):
        return f"'{self.title}' by {self.author}"

    # Controls how == works between objects
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    # For <
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    # same __gt__ for greater than >

    # For addition between objects
    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"
    
    # For finding keywords in objects
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    #For accessing objects like dictionaries
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else: 
            return f"{key} was not found"


book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("The Hobbit", "J.R.R. Tolkien", 295)
book3 = Book("Harry Potter", "J.K. Rowling", 223)


print(book1)

print(book1 == book2)   
print(book1 == book3)   

print(book2 < book1)

print(book1 + book2)

print("Hobbit" in book1)
print("Rowling" in book1)

print(book1["title"])
print(book2["author"])
print(book3["num_pages"])