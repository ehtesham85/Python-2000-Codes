class Library:
  def __init__(self):
    self.no_of_books_count=0 
    self.books=[]

  def add(self):
    print("How many books do you want to add? ")
    b = int(input())
    for i in range(b):
      print(f"Enter the name of book {i+1}: ")
      book_name = input()
      self.books.append(book_name)
      self.no_of_books_count += 1

    print("Books added successfully\n")

  def get_no_of_books(self):
    return self.no_of_books_count

  def show_books(self):
    print("Books in the Library:\n")
    for i, book in enumerate(self.books, 1):
      print(f"{i}. {book}")


# 🧪 Using the Library class
library = Library()
library.add()
library.show_books()
print("\nTotal Books in Library:", library.get_no_of_books())
