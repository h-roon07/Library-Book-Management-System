# Defining the Book class to represent inidvidual books. 
class Book:
    def __init__(self, title, author, isbn):
        '''
        Initializing the book with a title, author, and isbn as well as assigning parameters to these attributes. 
        '''
        self.title = title
        self.author = author
        self.isbn = isbn

    def get_details(self):
        '''
        Defining a method to return a books details.
        '''
        return '"' + self.title + '" (' + self.author + ', ISBN: ' + self.isbn + ')'


# Defining the Library class that manages borrowing, returning, and viewing books. 
class Library:
    def __init__(self):
        '''
        Initializing an empty list that will be used to store books in a Last-In-First-Out stack.
        '''
        self.books_stack = []

    def borrow_book(self, book):
        '''
        Defining a method for borrowing a book by adding the book object to the stack of books. The latest 
        borrowed book is added to the top of the stack. A confirmation message is also printed.
        '''
        self.books_stack.append(book)
        print('Book "' + book.title + '" borrowed successfully!')

    def return_book(self):
        '''
        Defining a method for returning the most recently borrowed book using index -1. The stack is first
        checked in case it is empty, an error message is printed if this is true. Otherwise, the last item in
        the stack is deleted to remove the most recently borrowed book. A confirmation message is also printed.
        '''
        if not self.books_stack:
            print("No books to return!")
        else:
            returned_book = self.books_stack[-1]
            del self.books_stack[-1]
            print(returned_book.title + '" returned successfully!')

    def reverse_list(self, items):
        '''
        Defining a method to reverse a list by first creating an empty list, then iterating through another list and 
        appending each element to the empty list from the end of the other list to the start, and finally returning 
        the new, reversed list.
        '''
        reversed_items = []
        for i in range(len(items)):
            reversed_items.append(items[len(items) - 1 - i])
        return reversed_items

    def view_current_books(self):
        '''
        Defining a method for viewing all books that are currently borrowed. The stack is first checked in case it is
        empty, an error message is printed if this is true. A title is printed and the borrowed books are reversed
        using the previous method, then the book details along with its position in the list are printed. 
        '''
        if not self.books_stack:
            print("No books are currently borrowed.")
        else:
            print("Currently borrowed books:")
            count = 1
            for book in self.reverse_list(self.books_stack):
                print(str(count) + '. ' + book.get_details())
                count += 1


def main():
    '''
    Defining the main function which handles the processes, (especially front-end) of the program. 
    '''
    # Creating an instance of the Library class.
    library = Library()

    # Using an infinite loop that keeps the program running until the user inputs the exit command.
    while True:
        print("\nLibrary Book Management System")
        print("-------------------------------")
        print("Commands:")
        print("1. Borrow a book")
        print("2. Return a book")
        print("3. View current borrowed books")
        print("4. Exit")

        # Taking the users input choice from the main menu.
        choice = input("Enter your choice: ")

        # If the user picks choice 1, they are asked to input the books details.
        if choice == "1":
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")

            # Validating that the entered book is not duplicated or already existing by checking if 
            # the title, autor, and isbn match the users inputs. If a duplicate is found, an error
            # message is printed, otherwise, a new book object is created and added to the stack. 
            duplicate = False
            for book in library.books_stack:
                if book.title == title and book.author == author and book.isbn == isbn:
                    duplicate = True
                    break
            if duplicate:
                print("This book is already borrowed!")
            else:
                book = Book(title, author, isbn)
                library.borrow_book(book)

        # If the user picks choice 2, the most recently borrowed book is returned.
        elif choice == "2":
            library.return_book()

        # If the user picks choice 3, the list of borrowed books is printed.
        elif choice == "3":
            library.view_current_books()

        # If the user picks choice 4, a thank you message is printed and the program ends.
        elif choice == "4":
            print("Thank you for using the Library Book Management System!")
            break

        # If the user picks any number other than 1-5, an error message is printed and the program is
        # repeated, allowing them to input thier choice again. 
        else:
            print("Invalid choice, please try again.")
        
main()