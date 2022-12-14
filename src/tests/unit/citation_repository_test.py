import unittest

from models.book import Book
from models.user import User
from models.othercitation import OtherCitation
from models.article import Article
from repositories.citation_repository import citation_repository
from repositories.user_repository import user_repository


class TestCitationRepository(unittest.TestCase):

    def setUp(self):
        citation_repository.delete_all_citations()
        user_repository.delete_all_users()
        user_repository.create_new_user(
            User(username="Jaakko", password="salasana1"))
        self.omistaja_id = 1

    def test_create_new_book_citation(self):
        citation_repository.create_new_book_citation(
            Book(owner_id=self.omistaja_id, given_id="Stephen_Hawking_A_Brief_History_Of_Time", author="Stephen Hawking", editor="Unknown", title="A Brief History of Time", publisher="Unknown", year=1988))
        self.assertEqual(
            len(citation_repository.get_all_citations(self.omistaja_id)), 1)

    def test_create_new_article_citation(self):
        citation_repository.create_new_article_citation(Article(
            owner_id=self.omistaja_id, given_id="Author_Title", author="Author", title="Title", journal="Journal", year=1111))
        self.assertEqual(
            len(citation_repository.get_all_citations(self.omistaja_id)), 1)

    def test_create_new_other_citation(self):
        citation_repository.create_new_other_citation(OtherCitation(
            owner_id=self.omistaja_id, given_id="Author_Title", author="Author", title="Title", type="Type", other="Other", year=1111))
        self.assertEqual(
            len(citation_repository.get_all_citations(self.omistaja_id)), 1)

    def test_delete_book_citation(self):
        poistettava = citation_repository.create_new_book_citation(
            Book(owner_id=self.omistaja_id, given_id="Stephen_Hawking_A_Brief_History_Of_Time", author="Stephen Hawking", editor="Unknown", title="A Brief History of Time", publisher="Unknown", year=1988))
        citation_repository.delete_citation(
            poistettava.given_id, self.omistaja_id)

        self.assertEqual(
            len(citation_repository.get_all_citations(self.omistaja_id)), 0)

    def test_delete_book_citation_a_second_time(self):
        poistettava = citation_repository.create_new_book_citation(
            Book(owner_id=self.omistaja_id, given_id="Stephen_Hawking_A_Brief_History_Of_Time", author="Stephen Hawking", editor="Unknown", title="A Brief History of Time", publisher="Unknown", year=1988))
        citation_repository.delete_citation(
            poistettava.given_id, self.omistaja_id)
        self.assertEqual(
            len(citation_repository.get_all_citations(self.omistaja_id)), 0)

    def test_delete_one_book_citation_of_two(self):
        poistettava = citation_repository.create_new_book_citation(
            Book(owner_id=self.omistaja_id, given_id="Stephen_Hawking_A_Brief_History_Of_Time", author="Stephen Hawking", editor="Unknown", title="A Brief History of Time", publisher="Unknown", year=1988))
        citation_repository.create_new_book_citation(
            Book(owner_id=self.omistaja_id, given_id="Author_Two_Still_Unknown", author="Author Two", editor="Still Unknown", title="Title Two", publisher="Dunno", year=1111))
        citation_repository.delete_citation(
            poistettava.given_id, self.omistaja_id)
        self.assertEqual(
            len(citation_repository.get_all_citations(self.omistaja_id)), 1)
