class Book:
    title = None
    author = None
    year = None

    def get_info(self):
        return (f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}")

book1 = Book()
book1.title = 'Апельсин'
book1.author = 'Дмитрий Уткин'
book1.year = 1974
print(book1.get_info())
# book2 = Book()
# print(book2.get_info)