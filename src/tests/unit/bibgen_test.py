import unittest
from unittest.mock import Mock
from services.bibgen import Bibgen
from services.citation_services import CitationService

class TestBibgen(unittest.TestCase):
    def setUp(self):
        self.citation_repository_mock = Mock()
        self.citation_service = CitationService(self.citation_repository_mock)
        self.bibgen = Bibgen()

    def test_generate_empty_text_from_empty_repository(self):
        result = self.bibgen.generate_bib_text(1)
        self.assertEqual("", result)

    def test_converting_from_database_results_to_appropriate_variables(self):
        self.citation_service.create_book_citation(1, 1, 'Einstein', 'Relativity: The Special and the General Theory', 'None', 'Holt', 1921)

        test_result = self.bibgen.convert_to_bib_variables(self.citation_service.get_citations_column_names())
        real_result = ['given_id', 'author', 'editor', 'title', 'publisher', 'year']

        self.assertEqual(real_result, test_result)

    def test_reordering_citation_list_for_bibgen(self):
        self.citation_service.create_book_citation(1, 1, 'Einstein', 'Relativity: The Special and the General Theory', 'None', 'Holt', 1921)

        test_result = self.bibgen.reorder_citation_list_for_bib(self.citation_service.get_citations(1))
        real_result = [1, 'Einstein', 'Relativity: The Special and the General Theory', 'None', 'Holt', 1921]

        self.assertEqual(real_result, test_result)

