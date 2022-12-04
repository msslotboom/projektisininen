import unittest
from unittest.mock import Mock, ANY
from services.citation_services import CitationService, UserInputError

class TestCitationService(unittest.TestCase):
    def setUp(self):
        self.citation_repository_mock = Mock()
        self.citation_service = CitationService(self.citation_repository_mock)

