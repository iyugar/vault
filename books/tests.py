from django.test import TestCase
from books.models import Book
from users.models import CustomUser


class BookTestCase(TestCase):
    def setUp(self):
        test_user = CustomUser.objects.create(
            username='testUser', password='testPassword', email='test@mail.com')

        Book.objects.create(owner=test_user, title="Test Book",
                            author="John Doe", startDate="2022-01-01", endDate="2022-02-01")
        Book.objects.create(owner=test_user, title="Test Book 2",
                            author="Jane Doe", startDate="2022-01-01")

    def test_book_complete(self):
        '''Test if a book is complete'''

        book1 = Book.objects.get(title="Test Book")
        book2 = Book.objects.get(title="Test Book 2")

        self.assertEqual(book1.is_complete(),True)
        self.assertEqual(book2.is_complete(),False)
