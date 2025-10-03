class Books:
    def __init__(self, author, title,copies = 1):
        self.author = author
        self.title = title
        self.copies = copies
    def __str__(self):
        return f"{self.title} by {self.author}, {self.copies} are available !"

class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
        print(f"{book.title} added to library")
    def show_books(self):
        for i in self.books:
            print(f"{i.title }")
    def remove_book(self, book):
        for b in self.books:
            if b.title == book.title:
                self.books.remove(b)
                print(f"{book.title} removed from library")
class User:
    def __init__(self, name):
       self.name = name
       self.borrowed_books = []
    def borrow_book(self,book):
        if book.copies > 0:
            book.copies -= 1
            self.borrowed_books.append(book) 
            print(f"{self.name} borrowed book:{book.title}")
            if book.copies == 0:
               library.remove_book(book)
        else:
            print("sorry {book.title} is not available")
    def returned_book(self, book):
        if book in self.borrowed_books:
            book.copies+=1
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}")
            library.add_book(book)
        else:
            print(f"{self.name} not borrowed {book.title}")
    def __str__(self):
        return f"User: {self.name}, Borrowed : {self.borrowed_books}"
      
   
library = Library()

book1 = Books("Eric Matthes", "Python Crash Course", 2)
book2 = Books("Robert C. Martin", "Clean Code", 1)
book3 = Books("Andrew Hunt", "The Pragmatic Programmer", 3)

print("\n--- Test 1: Add Books ---")
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book3)  # duplicate add test
library.show_books()

print("\n--- Test 2: Borrow Book (Normal) ---")
user = User("Som")
user.borrow_book(book1)
print(user)
library.show_books()

print("\n--- Test 3: Borrow Until Copies Exhaust ---")
while book3.copies > 0:
    user.borrow_book(book3)
library.show_books()
print(user)

print("\n--- Test 4: Borrow a Book With 0 Copies ---")
user.borrow_book(book3)  # should fail

print("\n--- Test 5: Return Book ---")
user.returned_book(book1)
library.show_books()
print(user)

print("\n--- Test 6: Return Book Not Borrowed ---")
fake_book = Books("Fake Author", "Fake Book", 1)
user.returned_book(fake_book)

print("\n--- Test 7: Show Books When Library Empty ---")
library.books.clear()
library.show_books()

print("\n--- Test 8: Multiple Users Borrowing Same Book ---")
library.add_book(book2)  # add back
user2 = User("Alex")
user.borrow_book(book2)
user2.borrow_book(book2)  # should fail if no copies
library.show_books()
print(user)
print(user2)