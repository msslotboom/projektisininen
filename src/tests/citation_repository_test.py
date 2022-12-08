import unittest
from repositories.citation_repository import citation_repository
from repositories.user_repository import user_repository
from models.citation import Citation
from models.user import User

class TestCitationRepository(unittest.TestCase):
    def setUp(self):
        citation_repository.delete_all_citations()
        user_repository.create_new_user(User(username="Jaakko", password="salasana1"))
        citations = citation_repository.get_all_citations()

    def test_create_citation_with_valid_fields(self):
        citation_repository.create_new_citation(Citation(id=1, owner_id=2, authors="Kirjoittaja", title="Titteli", year="2020"))
        citations = citation_repository.get_all_citations(1)

        self.assertEqual(len(citations), 1)
        self.assertEqual(citations[0][2], "Kirjoittaja")
        
