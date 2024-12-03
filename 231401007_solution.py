############ Do not change the assignment code value ############
assignment_code = 140110202
name = "Yekta"
surname = "Soytürk"
student_id = "231401007"
### Do not change the variable names above, just fill them in ###

import json

class Book:
    def __init__(self, title, author, publish_date, isbn, is_borrow = False, borrower = None):
        self.title = title
        self.author = author
        self.publish_date = publish_date
        self.isbn = isbn
        self.is_borrowed = is_borrow
        self.borrower = borrower
        
class User:
    def __init__(self, first_name, last_name, student_id):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.data_file = "library_data.json"
        self._load_data()

    def _save_data(self):
        books_data = []
        for book in self.books:
            book_data = {
                'title': book.title,
                'author': book.author,
                'publish_date': book.publish_date,
                'isbn': book.isbn,
                'is_borrowed': book.is_borrowed,
                'borrower': book.borrower,
            }
            books_data.append(book_data)

        users_data = []
        for user in self.users:
            user_data = {
                'first_name': user.first_name,
                'last_name': user.last_name,
                'student_id': user.student_id
            }
            users_data.append(user_data)

        with open(self.data_file, 'w', encoding="utf-8") as file:
            json.dump({
                'books': books_data,
                'users': users_data,
            }, file, indent=2, ensure_ascii=False)

    def _load_data(self):
        try:
            with open(self.data_file, 'r') as file:
                data = json.load(file)
                for book_data in data.get('books', []):
                    title = book_data['title']
                    author = book_data['author']
                    publish_date = book_data['publish_date']
                    isbn = book_data['isbn']
                    is_borrowed = book_data.get('is_borrowed', False)
                    borrower = book_data.get('borrower', None)

                    book_obj = Book(title, author, publish_date, isbn, is_borrowed, borrower)
                    self.books.append(book_obj)

                for user_data in data.get('users', []):
                    first_name = user_data['first_name']
                    last_name = user_data['last_name']
                    student_id = user_data['student_id']
                    user_obj = User(first_name, last_name, student_id)
                    self.users.append(user_obj)

        except FileNotFoundError:
            self._save_data()
            
    def add_book(self, title, author, publish_date, isbn):
        
        a_book = Book(title, author, publish_date, isbn)
           
        for i in self.books:
            if i.isbn == isbn:
                return False
            
        self.books.append(a_book)
        self._save_data()
        return a_book.title
        
    def add_user(self, first_name, last_name, student_id):
        
        a_user = User(first_name, last_name, student_id)
           
        for i in self.users:
            if i.student_id ==student_id:
                return False
            
        self.users.append(a_user)
        self._save_data()
        return a_user.student_id
    
    def check_book_by_isbn(self, isbn):
        
        for i in self.books:
            if i.isbn == isbn:
                return True

        return False
    
    def remove_book(self, isbn):
        
        for i in self.books:
            if i.isbn == isbn and i.is_borrowed == False:
                self.books.remove(i)
                self._save_data()
                return i.title
        return False
    
    def delete_user(self, student_id):

        for i in self.books:
            if i.borrower == student_id:
                return False
        for i in self.users:
            if i.student_id == student_id:
                self.users.remove(i)
                self._save_data()
                return student_id
        return False
        
    def list_books(self):
        
        book_list = []
        for i in self.books:
            book_list.append(i.isbn)   
        return book_list

    def borrow_book(self, isbn, student_id):
        
        for i in self.users:
            if i.student_id == student_id:
                for i in self.books:
                    if i.isbn == isbn and i.is_borrowed == False:  
                        i.is_borrowed = True
                        i.borrower = student_id
                        self._save_data()
                        return True
        return False

    def return_book(self, isbn):
        
        for i in self.books:
            if i.isbn == isbn and i.is_borrowed == True:  
                i.is_borrowed = False
                i.borrower = None
                self._save_data()
            
                return True
        return False
