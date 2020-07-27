class Author:
    def __init__(self,author_name,author_age,author_nationality):
        self.author_name=author_name
        self.author_age=author_age
        self.author_nationality=author_nationality

    def get_author_name(self):
        return self.author_name

class Book:
    def __init__(self,book_name,book_price,author_name,author_age,author_nationality):
        self.book_name=book_name
        self.book_price=book_price
        self.author=Author(author_name,author_age,author_nationality)
        
    def get_book_name(self):
        return self.book_name
    
    def get_book_price(self):
        return self.book_price

    def affortable_price_book(self):
        if self.book_price<1000:
            return self.book_name,self.author.author_name
        

class BookWorld:
    def __init__(self,books):
        self.books=books

    def print_affortable_books(self):
        book_name=[]
        for book in books:
            check_book_price=book.affortable_price_book()
            if check_book_price is None:
                pass
            else:
                book_name.append(check_book_price)
        return book_name

    def total_price_of_book(self):
        total_cost=0
        for book in books:
            total_cost+=book.get_book_price()
        return total_cost

    def print_author_name(self):
        author=[]
        for book in books:
            author.append(book.author.author_name)
        print(' ,'.join( author))

def total_number_of_book(books,given_author):
    book_count=0
    for book in books:
        if book.author.author_name==given_author:
             book_count+=1
    return(book_count)
                


python = Book("Python",999,"Guido van rossum",64,"Dutch")
scala = Book("scala",1500,"Martin Odersky",61,"German")
java = Book("Java",800,"James Gosling",65,"Canadian")
c = Book("C",1999,"Dennis Ritche",79,"American")
c_plus_plus = Book("C++",1499,"Bjarne Stroustrup",69,"Danish")
generic_java = Book("Generic Java",500,"Martin Odersky",61,"German")

books =[python,scala,c,java,c_plus_plus,generic_java]

bookworld=BookWorld(books)

print("Total price of Books:",bookworld.total_price_of_book())

bookworld.print_author_name()

given_author=input("Enter any one of author name:")

print("Total number of books written by this author is:",total_number_of_book(books,given_author))

print("Affortable price books:\n",bookworld.print_affortable_books())
