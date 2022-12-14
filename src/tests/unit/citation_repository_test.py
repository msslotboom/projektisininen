import unittest

from models.book import Book
from models.user import User
from repositories.citation_repository import citation_repository
from repositories.user_repository import user_repository


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

    def test_edit_citation(self):
        omistaja_id = 1
        viite = citation_repository.create_new_citation(Citation(owner_id=omistaja_id, 
        authors="Einstein", title="kirja", year=1905, given_id = 1))  
        
        viite_id = viite.id
        u_viite = citation_repository.edit_citation(viite_id, "Hawking", "parempi kirja", 2002, 2)
        self.assertEqual(u_viite.authors, "Hawking")
        self.assertEqual(u_viite.title, "parempi kirja")
        self.assertEqual(u_viite.year, 2002)
        self.assertEqual(u_viite.given_id, 2)
    
    def test_edit_other_citation(self):
        viite = citation_repository.create_new_other_citation(OtherCitation(
            owner_id=1, given_id=1, author="author", title="title", type="type", other="other", year=2021
        ))
        uusi_viite = citation_repository.edit_other_citation(
            citation_id=viite.id, given_id=2, author="author2", title="title2", type="type2", other="other2", year=2022
        )
        self.assertEqual(uusi_viite.author, "author2")
        self.assertNotEqual(uusi_viite.title, "title")
    def test_delete_one_book_citation_of_two(self):
        poistettava = citation_repository.create_new_book_citation(
            Book(owner_id=self.omistaja_id, given_id=1, author="Stephen Hawking", title="A Brief History of Time", year=1988))
        citation_repository.create_new_book_citation(
            Book(owner_id=self.omistaja_id, given_id=2, author="Richard Feynman", title="The Feynman Lectures on Physics", year=1963))

        citation_repository.delete_citation(poistettava.id, "book")

        citations = citation_repository.get_all_citations(
            self.omistaja_id).count()
        self.assertEqual(citations, 1)
