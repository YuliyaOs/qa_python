from main import BooksCollector
import pytest


@pytest.fixture(autouse=True)
def collector():
    collector = BooksCollector()
    collector.add_new_book('Гарри Поттер')
    collector.add_new_book('Дракула')
    collector.add_new_book('Оно')
    collector.set_book_genre('Гарри Поттер', 'Фантастика')
    collector.set_book_genre('Дракула', 'Ужасы')
    collector.set_book_genre('Оно', 'Ужасы')
    return collector


@pytest.fixture(autouse=True)
def collector_empty():
    collector = BooksCollector()
    return collector
