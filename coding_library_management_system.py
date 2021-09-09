class Library:


    def __init__(self,listOfBooks):
        self.books=listOfBooks

    def displayAvailableBooks(self):
        print("The Books Present in this Library are: ")
        for book in self.books:
            print(" *" + book)

    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. please keep it safe and return it within 30 days")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry!,This books is either not available or has been issued to some one else.Please Wait until the book is refund or available in this Library")
            return False

    def returnBook(self,bookName):
        if bookName==" ":
            print("Sorry! You Entered the Bookname is Invalid.Please Entered the Valid Bookname")
        else:
            if bookName in self.books:
                self.books.append(bookName)
                print("Thanks for Returning this book!Hope you enjoyed reading it.Have a great day ahead!")
            else:
                print("Sorry,You have not borrowed this book from this Library.Please Enter the Actual Book Name which you Borrowed from this Library")
                print("If You would not return this book within the proper time the Library Authority would push charge for you perday RS 2.0 after expiry date")

class Student:

    def requestBook(self):
        self.book=input("Please Enter the Name of the Book which you want to Borrow: ")
        return self.book

    def returnBook(self):
        self.book=input("Please Enter the Name of the Book which you want Return: ")
        return self.book
    
    

if __name__=="__main__":
    codingLibrary=Library(["C","C++","Java","Python","Web development(HTML,CSS,JAVASCRIPT)","Full stack development(MERN)","Django","Machine Learning","Deep Learning"])
    student=Student()

    while(True):
        welcomeMsg='''\n @@@@@@@@@@@@ Welcome to Coding Library Management System @@@@@@@@@@@@@@@
        please choose an option:
        1.List all the Books Available in the Library
        2.Request a Book
        3.Return a Book
        4.Exit the Library
         '''
        print(welcomeMsg)
        a=int(input("Please Enter of Your Choice: "))
        if a==1:
            codingLibrary.displayAvailableBooks()
        elif a==2:
            codingLibrary.borrowBook(student.requestBook())
        elif a==3:
            codingLibrary.returnBook(student.returnBook())
        elif a==4:
            print("Thanks for using this Library!Have a great day ahead")
            exit()
        else:
            print("Invalid Choice!,Please choose the right one and Enjoy to this Management System")
                  
