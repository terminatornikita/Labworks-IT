a= input("Введите название книги: ")
b= input("Введите автора: ")
c= int(input("Введите год издания: "))
class book:
    def __init__(self, tittle, author, year):
        self.tittle = tittle
        self.author = author
        self.year = year
    def get_info(self):
        return f"Название книги: {self.tittle}. Автор: {self.author}. Год издания: {self.year}."
book_instance = book(a, b, c)
print(book_instance.get_info())
