from app import db
from models.citation import Citation


class CitationRepository:
    def create_new_citation(self, citation: Citation):
        db.session.add(citation)
        db.session.commit()

        return citation

    def get_all_citations(self, user_id):
        return Citation.query.filter_by(owner_id=user_id)


citation_repository = CitationRepository()
