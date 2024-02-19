import os

class Library:
    def __init__(self):
        self.file_name = "books.txt"
        self.file = open(self.file_name, "a+")
        self.file.seek(0)

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        lines = self.file.read().splitlines()
        for line in lines:
            book_info = line.split(',')
            print(f"Book: {book_info[0]}, Author: {book_info[1]}")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author: ")
        release_year = input("Enter release year: ")
        num_pages = input("Enter number of pages: ")

        # a+ sondan başladığı için cursoru sona götürmemiz gerek
        self.file.seek(0, 2)

        book_info = f"{title},{author},{release_year},{num_pages}\n"
        self.file.write(book_info)

        print("Book has been added.")

    def remove_book(self):
        remove = input("Enter the title of the book to remove: ")
        found = False  # Kitabın varlığını kontrol et

        # Baştan itibaren bütün lineları oku
        self.file.seek(0)
        lines = self.file.readlines()

        #Bulunduysa dosyayı truncate et
        self.file.seek(0)
        self.file.truncate()

        for line in lines:
           
            if remove in line:
                found = True
                # Silinmesi gereken dosyayı atla
            else:
                #kalanını tekrar yaz
                self.file.write(line)


        if not found:
            print(f"Book '{remove}' not found, please check to see if you wrote the name correctly.")
        else:
            print(f"Book '{remove}' removed.")

lib = Library()

while True:
    print("\n*** MENU ***")
    print("1) List Books\n2) Add Book(s)\n3) Remove Book")

    choice = input("Enter your choice (1-3, or 'q'/'Q' to quit): ")

    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    elif choice.lower() == 'q' or choice.upper() == 'Q':
        print("Exiting the program. Changes saved.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 3, or 'q'/'Q' to quit.")
