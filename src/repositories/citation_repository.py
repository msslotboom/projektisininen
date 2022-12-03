from app import db
from models.citation import Citation


class CitationRepository:
    def create_new_citation(self, citation: Citation):
        db.session.add(citation)
        db.session.commit()

        return citation

    def get_all_citations(self, user_id):
        return Citation.query.filter_by(owner_id=user_id)
    
    def delete_citation(self, citation_id):
        citation_obj = Citation.query.filter_by(id=citation_id).one()

        db.session.delete(citation_obj)
        db.session.commit()


citation_repository = CitationRepository()
