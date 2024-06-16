#Create a simple Library Management System using Python that demonstrates the basic concepts of Object-Oriented Programming (OOP).

class Book:

    def __init__(self, title, author, isbn, copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies

    def display_info(self):
        print(f'The details of the book are - Title : {self.title}, Author : {self.author}, isbn : {self.isbn}, copies : {self.copies}')

    def check_out(self):
        if self.copies > 0:
            self.copies -= 1
            print(f'The book {self.title} is checked out')
        else:
            print(f'The book {self.title} is not available')

    def return_book(self):
        self.copies += 1 
        print(f'The book {self.title} is returned')

class Member:

    def __init__(self,name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.copies > 0:
            book.checkout()
            self.borrowed_book.append(book)
            print(f'{self.name} has borrowed {book.title}')
        else:
            print("the book is not available")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f'{self.name} has returned {book.title}')
        else:
            print(f'{book.title} is not borrowed by {self.name}')

class Library:

    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f'The book {book.title} is added to the library')

    def add_member(self, member):
        self.members.append(member)
        print(f'{member.name} is added to the library')

    def find_book_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        else:
            None
        
    def find_member_by_id(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        else:
            None

class PremiumMember(Member):    #inheritance from the Member class

    def __init__(self,name,member_id, membership_fee):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
        self.membership_fee = membership_fee

    def borrow_book(self, book):     #method overriding due to same signature - polymorphism
        if len(self.borrowed_books) < 10:  
            if book.copies > 0:
                book.check_out()
                self.borrowed_books.append(book)

library = Library()

# Adding books to the library
book1 = Book("Hunger Games", "Suzzane Collins", "123456789", 2)
book2 = Book("Bridgerton", "Julia Quinn", "987654321", 3)

library.add_book(book1)
library.add_book(book2)

book1.display_info()
book2.display_info()









                  
            
        



     


    



    






