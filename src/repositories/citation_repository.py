from app import db
from models.citation import Citation


class CitationRepository:
    def create_new_citation(self, citation: Citation):
        db.session.add(citation)
        db.session.commit()

        return citation
    
    def edit_citation(self, citation_id, authors, title, year, given_id):
        Citation.query.filter_by(id=citation_id).\
            update({'authors':authors})
        Citation.query.filter_by(id=citation_id).\
            update({'title':title})
        Citation.query.filter_by(id=citation_id).\
            update({'year':year})
        Citation.query.filter_by(id=citation_id).\
            update({'given_id':given_id})
        db.session.commit()
        return self.get_citation(citation_id)

    def get_all_citations(self, user_id):
        return Citation.query.filter_by(owner_id=user_id)
    
    def delete_citation(self, citation_id):
        citation_obj = Citation.query.filter_by(id=citation_id).one()

        db.session.delete(citation_obj)
        db.session.commit()

    def delete_all_citations(self):
        return_value = Citation.query.delete()
        db.session.commit()

        return return_value
    
    def get_citation(self, citation_id):
        return Citation.query.filter_by(id=citation_id).first()



citation_repository = CitationRepository()
