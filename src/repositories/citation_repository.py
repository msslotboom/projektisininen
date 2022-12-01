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

    def get_all_citations(self, user_id):
        sql = """SELECT * FROM citations WHERE owner_id=%s
        """
        db.execute(sql, user_id)
        citations = []
        for row in db.fetchall():
            citations.append(row)
        self._citations = citations
        return self._citations

citation_repository = CitationRepository()