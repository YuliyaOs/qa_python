from main import BooksCollector
import pytest
import random
from conftest import collector, collector_empty


class TestBooksCollector:

    def test_init_books_genre_default(self, collector_empty):
        assert collector_empty.books_genre == {}

    def test_init_favorites_default(self, collector_empty):
        assert collector_empty.favorites == []

    def test_init_genre_and_genre_age_rating(self, collector_empty):
        assert collector_empty.genre == ['Фантастика', 'Ужасы',
                                         'Детективы', 'Мультфильмы', 'Комедии']
        assert collector_empty.genre_age_rating == ['Ужасы', 'Детективы']

    @pytest.mark.parametrize('name', ['З', 'За', 'Защита Лужина',
                                      'Искусство войны с комментариями и иллюс',
                                      'Искусство войны с комментариями и иллюст'])
    def test_add_new_book_true(self, collector, name):
        collector.add_new_book(name)
        assert collector.books_genre[name] == ''

    @pytest.mark.parametrize('name', ['Искусство войны с комментариями и иллюстр',
                                      'Искусство войны с комментариями и иллюстра',
                                      'Искусство войны с комментариями и иллюстрациями'])
    def test_add_new_book_name_41_and_more_symbols_false(self, collector, name):
        collector.add_new_book(name)
        assert collector.books_genre.get(name) == None

    def test_set_book_genre_true(self, collector):
        name = 'Рождественская песнь'
        collector.add_new_book(name)
        genre = random.choice(collector.genre)
        collector.set_book_genre(name, genre)
        assert collector.books_genre[name] == genre

    def test_set_book_genre_if_no_add_book_false(self, collector):
        name = 'Недобавленная книга'
        genre = random.choice(collector.genre)
        collector.set_book_genre(name, genre)
        assert collector.books_genre.get(name) == None

    def test_set_book_genre_if_genre_no_exists_false(self, collector):
        name = 'Рождественская песнь'
        collector.add_new_book(name)
        collector.set_book_genre(name, 'Жанр')
        assert collector.books_genre.get(name) == ''

    def test_get_book_genre_true(self, collector):
        name = list(collector.books_genre.keys())[0]
        assert collector.get_book_genre(name) == collector.books_genre[name]

    def test_get_book_genre_if_no_book_false(self, collector):
        assert collector.get_book_genre('Недобавленная книга') == None

    @pytest.mark.parametrize('genre,name', [['Фантастика', ['Гарри Поттер']],
                                            ['Ужасы', ['Дракула', 'Оно']]])
    def test_get_books_with_specific_genre_true(self, collector, genre, name):
        assert collector.get_books_with_specific_genre(genre) == name

    def test_get_books_genre_true(self, collector):
        assert collector.get_books_genre() == collector.books_genre

    def test_get_books_for_children_true(self, collector):
        assert collector.get_books_for_children() == ['Гарри Поттер']

    def test_add_book_in_favorites_true(self, collector):
        name = list(collector.books_genre.keys())[0]
        collector.add_book_in_favorites(name)
        assert collector.favorites == [name]

    def test_delete_book_from_favorites_true(self, collector):
        name = list(collector.books_genre.keys())[0]
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        assert collector.favorites == []

    def test_get_list_of_favorites_books_true(self, collector):
        name = list(collector.books_genre.keys())[0]
        collector.add_book_in_favorites(name)
        assert collector.get_list_of_favorites_books() == [name]
