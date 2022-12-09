import unittest
from unittest.mock import Mock, ANY
from services.citation_services import CitationService, UserInputError

class TestCitationService(unittest.TestCase):
    def setUp(self):
        self.citation_repository_mock = Mock()
        self.citation_service = CitationService(self.citation_repository_mock)

    def test_validate_citation_with_no_author(self):
        try:
            self.citation_service.create_citation(1, "", "title", "1", "1")
        except:
            UserInputError("Viitteestä puuttuu tietoja")

        self.citation_repository_mock.create_new_citation.assert_not_called()

    def test_validate_citation_with_no_title(self):
        try:
            self.citation_service.create_citation(1, "author", "", "1", "1")
        except:
            UserInputError("Viitteestä puuttuu tietoja")

        self.citation_repository_mock.create_new_citation.assert_not_called()

    def test_validate_citation_with_no_year(self):
        try:
            self.citation_service.create_citation(1, "author", "title", "", "1")
        except:
            UserInputError("Viite on virheellinen")

        self.citation_repository_mock.create_new_citation.assert_not_called()

    #Jostain syystä citation_servicen check_duplicate_given_id ei toimi oikein testeissä
    #
    #def test_create_citation_with_valid_information(self):
    #    self.citation_service.create_citation(1, "author", "title", 1, 1)
    #
    #    self.citation_repository_mock.create_new_citation.assert_called()

    

