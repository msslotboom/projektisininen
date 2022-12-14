from app import db
from models.article import Article
from models.book import Book
from models.othercitation import OtherCitation


class CitationRepository:
    def create_new_book_citation(self, book:Book):
        db.session.add(book)
        db.session.commit()

        return book

    def create_new_article_citation(self, article: Article):
        db.session.add(article)
        db.session.commit()

        return article

    def create_new_other_citation(self, other_citation: OtherCitation):
        db.session.add(other_citation)
        db.session.commit()

        return other_citation
    
    def edit_citation(self, citation_id, authors, title, year, given_id):
        # Citation.query.filter_by(id=citation_id).\
        #     update({'authors':authors})
        # Citation.query.filter_by(id=citation_id).\
        #     update({'title':title})
        # Citation.query.filter_by(id=citation_id).\
        #     update({'year':year})
        # Citation.query.filter_by(id=citation_id).\
        #     update({'given_id':given_id})
        # db.session.commit()
        # return self.get_citation(citation_id)
        pass

    def get_all_citations(self, user_id):
        # return Citation.query.filter_by(owner_id=user_id)
        pass
    
    def get_all_citation_table_names(self):
        # return Citation.__table__.columns.keys()
        pass
    
    def delete_citation(self, citation_id, type):
        if type == "article":
            article_obj = Article.query.filter_by(id=citation_id).first()
            db.session.delete(article_obj)
            db.session.commit()

        elif type == "book":
            book_obj = Book.query.filter_by(id=citation_id).first()
            db.session.delete(book_obj)
            db.session.commit()

        elif type == "other":
            other_obj = OtherCitation.query.filter_by(id=citation_id).first()
            db.session.delete(other_obj)
            db.session.commit()


    def delete_all_citations(self):
        books = Book.query.delete()
        articles = Article.query.delete()
        other_citations = OtherCitation.query.delete()
        db.session.commit()

        return books + articles + other_citations
    
    def get_citation(self, citation_id):
        return Citation.query.filter_by(id=citation_id).first()

    def find_by_given_id(self, given_id):
        #id = Citation.query.filter_by(given_id=given_id).first()
        #return id
        pass



citation_repository = CitationRepository()
