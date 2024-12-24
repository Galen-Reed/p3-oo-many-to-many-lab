class Author:

    all_authors=[]

    def __init__(self, name):
        if not isinstance(name, str) or not name.strip():
            raise Exception("Name must be a non-empty string.")
        self.name = name
        Author.all_authors.append(self)
        
    def contracts(self):
        # return list of related contracts
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        #return list of related books by using Contract class as intermediary
        return list({contract.book for contract in self.contracts()})

    def sign_contract(self, book, date, royalties):
        #create and return a new Contract object between author and specified books with data and royalties
        if not isinstance(book, Book):
            raise Exception("book must be an instance of the Book class.")
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        #return total amount of royalties that the author has earned all of their contracts
        return sum(contract.royalties for contract in self.contracts())

class Book:

    all_books=[]

    def __init__(self, title):
        if not isinstance(title, str) or not title.strip():
            raise Exception("Title must be a non-empty string.")
        self.title = title
        Book.all_books.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return list({contract.author for contract in self.contracts()})
        


class Contract:

    all=[]

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("author must be an instance of the Author class.")
        if not isinstance(book, Book):
            raise Exception("book must be an instance of the Book class.")
        if not isinstance(date, str) or not date.strip():
            raise Exception("Date must be a non-empty string.")
        if not isinstance(royalties, int) or royalties < 0:
            raise Exception("Royalties must be an integer.")
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @classmethod  
    def contracts_by_date(cls, date):
        #return all contracts that have same date as argument date
        filtered_contracts = [contract for contract in cls.all if contract.date == date]
        # Sort by book title to ensure a consistent order
        return sorted(filtered_contracts, key=lambda contract: (contract.book.title, contract.author.name))