import pytest

from books.models import Author, Book

pytestmark = pytest.mark.django_db


@pytest.fixture()
def authors(db):
    authors = [
        Author(first_name='Massimo', last_name='Costa'),
        Author(first_name='Roberto', last_name='Costa'),
    ]
    return Author.objects.bulk_create(authors)


@pytest.fixture()
def authors_and_books(authors):
    books = [
        Book(title=f'Book {a.id} {i + 1}', author=a)
        for a in authors
        for i in range(3)
    ]
    return authors, Book.objects.bulk_create(books)


def test_authors(authors):
    print('authors:', authors)
    assert Author.objects.count() == len(authors)


def test_authors_and_books(authors_and_books):
    authors, books = authors_and_books
    assert Author.objects.count() == len(authors)
    assert Book.objects.count() == len(books)
    assert Book.objects.filter(copies_sold__gt=0).count == 0
    
    author = authors[0]
    assert author.books.count() == 3


def test_citext_filtering(authors):
    assert Author.objects.filter(last_name='costa').count() == 2
    assert Author.objects.filter(first_name='MASSIMO').count() == 1
    assert Author.objects.filter(first_name='ROBERTO').count() == 1
