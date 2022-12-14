import unittest
from repositories.user_repository import user_repository
from models.user import User
from repositories.citation_repository import citation_repository
from models.citation import Citation
from models.book import Book


class TestCitationRepository(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        citation_repository.delete_all_citations()
        user_repository.delete_all_users()
        user_repository.create_new_user(
            User(username="Jaakko", password="salasana1"))
        self.omistaja_id = 1

    def test_delete_book_citation(self):
        poistettava = citation_repository.create_new_book_citation(
            Book(owner_id=self.omistaja_id, given_id=1, author="Stephen Hawking", title="A Brief History of Time", year=1988))

        citation_repository.delete_citation(poistettava.id, "book")

        citations = citation_repository.get_all_citations(
            self.omistaja_id).count()
        self.assertEqual(citations, 0)

    def test_delete_book_citation_a_second_time(self):
        poistettava = citation_repository.create_new_book_citation(
            Book(owner_id=self.omistaja_id, given_id=1, author="Stephen Hawking", title="A Brief History of Time", year=1988))

        citation_repository.delete_citation(poistettava.id, "book")

        citations = citation_repository.get_all_citations(
            self.omistaja_id).count()
        self.assertEqual(citations, 0)

    def test_delete_one_book_citation_of_two(self):
        poistettava = citation_repository.create_new_book_citation(
            Book(owner_id=self.omistaja_id, given_id=1, author="Stephen Hawking", title="A Brief History of Time", year=1988))
        citation_repository.create_new_book_citation(
            Book(owner_id=self.omistaja_id, given_id=2, author="Richard Feynman", title="The Feynman Lectures on Physics", year=1963))

        citation_repository.delete_citation(poistettava.id, "book")

        citations = citation_repository.get_all_citations(
            self.omistaja_id).count()
        self.assertEqual(citations, 1)
