class LibraryBook:
    def _init_(self, book_name, author, price):
        self.book_name = book_name
        self.author = author
        self.price = price

    def display_book_info(self):
        print("Book:", self.book_name)
        print("Author:", self.author)
        print("Price:", self.price)
        print()

b1 = LibraryBook("Python", "Guido", 500)
b2 = LibraryBook("Data Science", "John", 700)
b3 = LibraryBook("AI Basics", "Smith", 600)

b1.display_book_info()
b2.display_book_info()
b3.display_book_info()
