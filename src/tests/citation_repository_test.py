import unittest
from repositories.user_repository import user_repository
from models.user import User
from repositories.citation_repository import citation_repository
from models.citation import Citation

class TestCitationRepository(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        citation_repository.delete_all_citations()
        user_repository.delete_all_users()
        user_repository.create_new_user(User(username="Jaakko", password="salasana1"))
        
    #HUOM Poistettavan viitteen ID on eri vaikka edellinen poistettu!
    
    def test_delete_citaton(self):
        omistaja_id = 1
        citation_repository.create_new_citation(Citation(
            owner_id=omistaja_id, authors="Einstein", title="kirja", year=1905))  

        Einstein_id = 1
        citation_repository.delete_citation(Einstein_id)

        citations = citation_repository.get_all_citations(omistaja_id).count()
        self.assertEqual(citations, 0)

    def test_delete_citaton_a_second_time(self):
        omistaja_id = 1
        citation_repository.create_new_citation(Citation(
            owner_id=omistaja_id, authors="Einstein", title="kirja", year=1905))  

        Einstein_id = 2
        citation_repository.delete_citation(Einstein_id)

        citations = citation_repository.get_all_citations(omistaja_id).count()
        self.assertEqual(citations, 0)
    
    def test_delete_one_citaton_of_two(self):
        omistaja_id = 1
        citation_repository.create_new_citation(Citation(owner_id=omistaja_id, 
        authors="Einstein", title="kirja", year=1905))  
        citation_repository.create_new_citation(Citation(owner_id=omistaja_id, 
        authors="Hawking", title="parempi kirja", year=2002))  

        Einstein_id = 3
        citation_repository.delete_citation(Einstein_id)

        citations = citation_repository.get_all_citations(omistaja_id).count()
        self.assertEqual(citations, 1)
