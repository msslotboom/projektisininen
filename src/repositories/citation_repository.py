from app import db
from models.citation import Citation
from models.book import Book
from models.article import Article
from models.othercitation import OtherCitation


class CitationRepository:
    def create_new_book_citation(self, book:Book):
        db.session.add(book)
        db.session.add(Citation(owner_id = book.owner_id, given_id= book.given_id, type="book"))
        db.session.commit()

        return book

    def create_new_article_citation(self, article: Article):
        db.session.add(article)
        db.session.add(Citation(owner_id = article.owner_id, given_id= article.given_id, type="book"))
        db.session.commit()

        return article

    def create_new_book_citation(self, other_citation: OtherCitation):
        db.session.add(other_citation)
        db.session.add(Citation(owner_id = other_citation.owner_id, given_id= other_citation.given_id, type="book"))
        db.session.commit()

        return other_citation
    
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

    def find_by_given_id(self, given_id):
        id = Citation.query.filter_by(given_id=given_id).first()
        return id



citation_repository = CitationRepository()
