import unittest
from parameterized import parameterized
from main import BooksCollector


class TestBooksCollector(unittest.TestCase):

    def setUp(self):
        self.collector = BooksCollector()

    @parameterized.expand([
        ('Гарри Поттер', True, ''),
        ('А'*41, False, None),
        ('А'*40, True, '')
    ])
    def test_add_new_book(self, book_name, should_exist, expected_genre):
        self.collector.add_new_book(book_name)
        if should_exist:
            self.assertIn(book_name, self.collector.books_genre)
            self.assertEqual(self.collector.books_genre[book_name], expected_genre)
        else:
            self.assertNotIn(book_name, self.collector.books_genre)

    @parameterized.expand([
        ('Гарри Поттер', 'Фантастика', 'Фантастика'),
        ('Гарри Поттер', 'Путешествия', '')
    ])
    def test_set_book_genre(self, book_name, genre, expected_genre):
        self.collector.add_new_book(book_name)
        self.collector.set_book_genre(book_name, genre)
        self.assertEqual(self.collector.books_genre[book_name], expected_genre)

    @parameterized.expand([
        ('Гарри Поттер', 'Фантастика', 'Фантастика'),
    ])
    def test_get_book_genre(self, book_name, genre, expected_genre):
        self.collector.add_new_book(book_name)
        self.collector.set_book_genre(book_name, genre)
        self.assertEqual(self.collector.get_book_genre(book_name), expected_genre)

    def test_get_books_with_specific_genre(self):
        self.collector.add_new_book('Гарри Поттер')
        self.collector.add_new_book('Властелин Колец')
        self.collector.set_book_genre('Гарри Поттер', 'Фантастика')
        self.collector.set_book_genre('Властелин Колец', 'Фантастика')

        books = self.collector.get_books_with_specific_genre('Фантастика')
        self.assertIn('Гарри Поттер', books)
        self.assertIn('Властелин Колец', books)

    def test_get_books_genre(self):
        self.collector.add_new_book('Гарри Поттер')
        self.assertEqual(self.collector.get_books_genre(), {'Гарри Поттер': ''})

    def test_get_books_for_children(self):
        self.collector.add_new_book('Гарри Поттер')
        self.collector.set_book_genre('Гарри Поттер', 'Фантастика')
        self.collector.add_new_book('Детектив')
        self.collector.set_book_genre('Детектив', 'Детективы')

        books_for_children = self.collector.get_books_for_children()
        self.assertIn('Гарри Поттер', books_for_children)
        self.assertNotIn('Детектив', books_for_children)

    def test_add_book_in_favorites(self):
        self.collector.add_new_book('Гарри Поттер')
        self.collector.add_book_in_favorites('Гарри Поттер')
        self.assertIn('Гарри Поттер', self.collector.favorites)

        self.collector.add_book_in_favorites('Гарри Поттер')
        self.assertEqual(self.collector.favorites.count('Гарри Поттер'), 1)

    def test_delete_book_from_favorites(self):
        self.collector.add_new_book('Гарри Поттер')
        self.collector.add_book_in_favorites('Гарри Поттер')
        self.collector.delete_book_from_favorites('Гарри Поттер')
        self.assertNotIn('Гарри Поттер', self.collector.favorites)

    def test_get_list_of_favorites_books(self):
        self.collector.add_new_book('Гарри Поттер')
        self.collector.add_book_in_favorites('Гарри Поттер')

        favorites = self.collector.get_list_of_favorites_books()
        self.assertIn('Гарри Поттер', favorites)


if __name__ == '__main__':
    unittest.main()
