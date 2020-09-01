from flask import Flask, request, jsonify
from sqlalchemy import Column, Integer, String, create_engine
app = Flask(__name__)
DATABASE_URL = "postgres+psycopg2://postgres:priya@localhost/Bookworld"
db = create_engine(DATABASE_URL)

@app.route("/")
def home():
  return "Welcome to !! <h1>Priya Store</h1>"    

@app.route('/books',methods=['GET'])
def get_books():
    books = db.execute('select * from book.tblbookdetails')
    result = [dict(row) for row in books]
    return jsonify(result)
  
@app.route('/newbook', methods=['POST'])
def new_book():
    if request.method == 'POST':
        bookname = request.form['name']
        bookprice = request.form['price']
        db.execute("INSERT INTO book.tblbookdetails(bookid,bookname,bookprice) VALUES('{}','{}','{}')".format(5,bookname,bookprice))
        return 'New book inserted'
  
@app.route("/books/<name>/<price>")
def book(name,price):
  return f"book Name:{name},book price is:{price}"

if __name__ == '__main__' :
    app.run(debug=True)