import unittest
from unittest.mock import Mock
from repositories.user_repository import UserRepository
from services.bibgen import Bibgen
from services.citation_services import CitationService
from repositories.citation_repository import CitationRepository
from services.user_services import UserService

class TestBibgen(unittest.TestCase):
    def setUp(self):
        self.citation_repository = CitationRepository()
        self.citation_service = CitationService(self.citation_repository)
        self.user_repo = UserRepository()
        self.user_services = UserService(self.user_repo)
        self.bibgen = Bibgen()

    def test_generate_empty_text_from_empty_repository(self):
        result = self.bibgen.generate_bib_text(0)
        print("heui")
        print(result)
        print("jaa")
        self.assertEqual("", result)

    #def test_converting_from_database_results_to_appropriate_variables(self):
    #    self.user_services.create_user("Antero", "Salasana1", "Salasana1")
    #    user_id = self.user_repo.get_id("Antero")
    #    self.citation_service.create_book_citation(user_id, "", 'Einstein', 'Relativity: The Special and the General Theory', 'None', 'Holt', 1921)
#
    #    test_result = self.bibgen.convert_to_bib_variables(self.citation_service.get_citations_column_names())
    #    real_result = ['given_id', 'author', 'editor', 'title', 'publisher', 'year']
#
    #    self.assertEqual(real_result, test_result)

    def test_reordering_citation_list_for_bibgen(self):
        self.user_services.create_user("Seppo", "Salasana1", "Salasana1")
        user_id = self.user_repo.get_id("Seppo")
        self.citation_service.create_book_citation(user_id, "ID", "Author", "Title", "None", "Dunno", 1111)

        test_result = self.bibgen.reorder_citation_list_for_bib(self.citation_service.get_citations(user_id))
        real_result = [("ID", "Author", "None", "Title", "Dunno", 1111)]
        self.assertEqual(real_result, test_result)

