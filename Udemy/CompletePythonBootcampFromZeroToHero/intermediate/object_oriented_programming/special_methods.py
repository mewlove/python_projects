# (control + '/' for comments)

#Magic/Dunder methods

class Book():
    def __init__(self, title:str, author:str, pages:int) -> None:
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self) -> str:
        return f"{self.title} by {self.author}"

    def __len__(self) -> int:
        return self.pages

book = Book("MyTitle","Me",200)
print(book)
print(len(book))