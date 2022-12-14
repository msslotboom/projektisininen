import unittest
from unittest.mock import Mock, ANY
from services.citation_services import CitationService, UserInputError
from services.user_services import UserService
from repositories.citation_repository import CitationRepository
from repositories.user_repository import UserRepository
from models.user import User


class TestCitationService(unittest.TestCase):
    def setUp(self):
        self.citation_repository_mock = Mock()
        self.citation_service_mock = CitationService(
            self.citation_repository_mock)
        self.citation_repository = CitationRepository()
        self.citation_service = CitationService(self.citation_repository)
        self.user_repo = UserRepository()
        self.user_services = UserService(self.user_repo)

    def test_validate_citation_with_no_author(self):
        try:
            self.citation_service_mock.create_book_citation(
                1, "Authors1999", "", "Title", "Editor", "Publisher", 1999)
        except:
            UserInputError("Viitteestä puuttuu tietoja")
        self.citation_repository_mock.create_new_book_citation.assert_not_called()

    def test_validate_citation_with_no_title(self):
        try:
            self.citation_service_mock.create_book_citation(
                1, "Authors1999", "Authors", "", "Editor", "Publisher", 1999)
        except:
            UserInputError("Viitteestä puuttuu tietoja")

        self.citation_repository_mock.create_new_book_citation.assert_not_called()

    def test_validate_citation_with_no_year(self):
        try:
            self.citation_service_mock.create_book_citation(
                1, "Authors1999", "", "Title", "Editor", "Publisher", "")
        except:
            UserInputError("Viitteestä puuttuu tietoja")

        self.citation_repository_mock.create_new_book_citation.assert_not_called()

    def test_generate_given_id(self):
        self.assertEqual(self.citation_service_mock.generate_given_id(
            "Author1 Author2", "1999"), "Author1_Author21999")

    def test_check_duplicate_given_id(self):
        # Pitää luoda UserRepository, UserServices ja sitten käyttäjä tai muuten tulee foreign key erroria
        # Lisäksi tätä ei voi testata mock repolla koska koska se palauttaa aina True
        self.user_services.create_user("Mikko", "Salasana1", "Salasana1")
        user_id = self.user_repo.get_id("Mikko")
        self.assertEqual(
            self.citation_service.check_duplicate_given_id("Unused_ID", user_id), False)
        self.citation_service.create_book_citation(
            user_id, "Used_ID", "Author", "Title", "Editor", "Publisher", 1999)
        try:
            self.citation_service.create_book_citation(
                user_id, "Used_ID", "Author", "Title", "Editor", "Publisher", 1999)
        except:
            UserInputError("Annettu ID on jo käytössä")

    def test_get_citations(self):
        self.user_services.create_user("Eemeli", "Salasana1", "Salasana1")
        user_id = self.user_repo.get_id("Eemeli")
        self.citation_service.create_article_citation(user_id, "", "Author", "Title", "Journal", 1969)
        self.citation_service.create_book_citation(user_id, "", "Book Author", "Book Title", "Book Editor", "Book Publisher", 2000)
        self.citation_service.create_other_citation(user_id, "", "Other Author", "Other Title", "Type", "Other", 1999)
        self.assertEqual(len(self.citation_service.get_citations(user_id)), 3)
        self.assertEqual(len(self.citation_service.get_article_citations(user_id)), 1)
        self.assertEqual(len(self.citation_service.get_book_citations(user_id)), 1)
        self.assertEqual(len(self.citation_service.get_other_citations(user_id)), 1)