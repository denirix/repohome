# Ex_1
class Publication:
    publisher = 'Atria Publishing Group'

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display(self):
        return f'Title: {self.title}\nAuthor: {self.author}\nYear: {self.year}'

    @classmethod
    def get_publisher(cls):
        return f'Publisher: {cls.publisher}'


class Book(Publication):
    def __init__(self, title, author, year, isbn):
        super().__init__(title, author, year)
        self.isbn = isbn

    def display(self):
        return super().display() + f'\nisbn: {self.isbn}'


class Magazine(Publication):
    def __init__(self, title, author, year, issue_number):
        super().__init__(title, author, year)
        self.issue_number = issue_number

    def display(self):
        return super().display() + f'isbn: {self.issue_number}'


book_1 = Book('The Adventures of Tom Sawyer.', 'Mark Twain', 1876, '9780195810400')
print(book_1.display())
print(book_1.get_publisher())

# Ex_2
class BankAccount:
    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f'Add {amount} to your account.')
            print(f'Total: {self.balance}')
        else:
            print('Wrong amount!')

    def withdraw(self, amount):
        if amount > 0:
            self.balance -= amount
            self.transactions.append(f'Subtract {amount} from your account.')
            print(f'Total: {self.balance}')
        else:
            print('Wrong amount!')

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        self.transactions.append(f'Add {interest} to your account.')
        print(f'Total: {self.balance}')

    def history(self):
        for transaction in self.transactions:
            print(transaction)


account = BankAccount(10000, 10)
account.deposit(50)
account.withdraw(50)
account.add_interest()
account.history()
