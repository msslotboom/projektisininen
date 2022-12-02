from app import db
from models.citation import Citation


class CitationRepository:
    def create_new_citation(self, citation: Citation):
        db.session.add(citation)
        db.session.commit()

        return citation

    def get_all_citations(self, user_id):
        return Citation.query.filer_by(owner_id=user_id)

    def get_citations_from_db(self, owner_id):
        sql = """SELECT * FROM citations WHERE owner_id=:id
        """

        result = db.session.execute(sql, {"id":owner_id})
        citations = []
        for row in result.fetchall():
            citations.append(row)
        self._citations = citations
        return self._citations

citation_repository = CitationRepository()
