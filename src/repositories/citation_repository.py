from entities.citation import Citation
from db import db 

class CitationRepository:
    def __init__(self):
        self._citations = []

    def create_new_citation(self, citation: Citation):
        sql = """INSERT INTO citations(owner_id, authors, title, year)
                VALUES (%s,%s,%s,%s)"""
        insert = (citation.owner_id, citation.authors, 
                    citation.title, citation.year)
        db.execute(sql, insert)

        self._citations.append()

    '''
    Viitteiden haku tähän
    '''

citation_repository = CitationRepository()