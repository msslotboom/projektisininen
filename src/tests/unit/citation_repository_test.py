import unittest

from models.book import Book
from models.user import User
from models.othercitation import OtherCitation
from models.article import Article
from repositories.citation_repository import citation_repository
from repositories.user_repository import user_repository
from services.user_services import UserService


class TestCitationRepository(unittest.TestCase):

    def setUp(self):
        citation_repository.delete_all_citations()
        user_repository.delete_all_users()
        user_service = UserService(user_repository)
        user_service.create_user("Jaakko", "Salasana1", "Salasana1")
        self.omistaja_id = user_repository.get_id("Jaakko")

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

    def test_edit_other_citation(self):
        viite = citation_repository.create_new_other_citation(OtherCitation(owner_id=self.omistaja_id, given_id=1,
                                                                            author="author", title="title", type="type", other="other", year=2021))
        citation_repository.edit_other_citation(
            citation_id=viite.id, given_id=2, author="author2", title="title2", type="type2", other="other2", year=2022)

        self.assertEqual(viite.author, "author2")
        self.assertEqual(viite.title, "title2")
        self.assertEqual(viite.type, "type2")
        self.assertEqual(viite.other, "other2")
        self.assertEqual(viite.year, 2022)

    def test_edit_book_and_article(self):
        kirja = citation_repository.create_new_book_citation(Book(
            owner_id=self.omistaja_id, given_id="kirja", author="author", title="title", editor="editor", publisher="publisher", year=2022
        ))
        artikkeli = citation_repository.create_new_article_citation(Article(
            owner_id=self.omistaja_id, given_id="artikkeli", author="author", title="title", journal="journal", year=2022
        ))

        citation_repository.edit_book_citation(
            citation_id=kirja.id, given_id="kirja", author="author", title="title", editor="editor2", publisher="publisher2", year=2022
        )
        citation_repository.edit_article_citation(
            citation_id=artikkeli.id, given_id="artikkeli", author="author", title="title", journal="journal2", year=2022)

        self.assertEqual(artikkeli.journal, "journal2")
        self.assertEqual(kirja.editor, "editor2")
        self.assertEqual(kirja.publisher, "publisher2")
