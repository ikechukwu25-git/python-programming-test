"""Challenge 22 - Library Book Records."""


class Book:
    def __init__(self, title, author, isbn, is_available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available

    def __str__(self):
        return (f"Book(title={self.title!r}, author={self.author!r}, "
                f"isbn={self.isbn!r}, available={self.is_available})")


if __name__ == "__main__":
    books = [Book("Python Basics", "N. Okafor", "BK001"),
             Book("Data Structures", "A. Bello", "BK002"),
             Book("Web Development", "C. Eze", "BK003", is_available=False)]
    for book in books:
        print(book)

    # Each object keeps its own state
    books[0].is_available = False
    print("\nAfter lending out BK001:")
    for book in books:
        print(f"{book.isbn}: available={book.is_available}")
    assert books[1].is_available is True and books[0].is_available is False
