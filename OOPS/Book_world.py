class Author:
    def __init__(self,author_name,author_age,author_nationality):
        self.author_name=author_name
        self.author_age=author_age
        self.author_nationality=author_nationality

class Book:
    def __init__(self,book_name,book_price,author_name,author_age,author_nationality):
        self.book_name=book_name
        self.book_price=book_price
        self.author=Author(author_name,author_age,author_nationality)

def book_total_price(books):
        total_price=0
        for book in books:
            total_price=total_price+book.book_price
        return total_price

def total_number_of_book(books,given_author):
     book_count=0
     for book in books:
         if book.author.author_name==given_author:
             book_count+=1     
     return(book_count)

def affortable_price_books(books):
    print("Book name \t Author Name")
    for book in books:
        if book.book_price < 1000:
            print(book.book_name+"\t\t "+book.author.author_name)

def print_author_name(books):
    author=[]
    for book in books:
        author.append(book.author.author_name)
    print(' ,'.join( author))



python = Book("Python",999,"Guido van rossum",64,"Dutch")
scala = Book("scala",1500,"Martin Odersky",61,"German")
java = Book("Java",800,"James Gosling",65,"Canadian")
c = Book("C",1999,"Dennis Ritche",79,"American")
c_plus_plus = Book("C++",1499,"Bjarne Stroustrup",69,"Danish")
generic_java = Book("Generic Java",500,"Martin Odersky",61,"German")

books =[python,scala,c,java,c_plus_plus,generic_java]

print("Total price of Books:",book_total_price(books))

print("\nAuthor Names:")
print_author_name(books)

given_author=input("\nEnter the author name to get number of books written by author:")

print("\nTotal number of book written by "+given_author+" is :"+str(total_number_of_book(books,given_author)))

affortable_price_books(books)

"""
Total price of Books: 6596

Author Names:
Guido van rossum ,Martin Odersky ,Dennis Ritche ,Bjarne Stroustrup ,Martin Odersky

Enter the author name to get number of books written by author:Guido van rossum

Total number of book written by Guido van rossum is :1
Book name 	 Author Name
Python		 Guido van rossum
Java             James Gosling
Generic Java	 Martin Odersky
"""

