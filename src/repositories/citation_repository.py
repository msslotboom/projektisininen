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

    def get_all_article_citations(self, user_id):
        return Article.query.filter_by(owner_id=user_id)

    def get_all_book_citations(self, user_id):
        return Book.query.filter_by(owner_id=user_id)

    def get_all_other_citations(self, user_id):
        return OtherCitation.query.filter_by(owner_id=user_id)

    def get_all_citations(self, user_id):

        all_citations = []
        all_citations.append(Article.query.filter_by(owner_id=user_id))
        all_citations.append(OtherCitation.query.filter_by(owner_id=user_id))
        all_citations.append(Book.query.filter_by(owner_id=user_id))
        
        return all_citations
    
    def get_all_citation_table_names(self):
        all_table_names = []
        all_table_names.append(Article.__table__.columns.keys())
        all_table_names.append(Book.__table__.columns.keys())
        all_table_names.append(OtherCitation.__table__.columns.keys())
        return all_table_names
    
    def delete_citation(self, given_id, owner_id):
        for book in self.get_all_book_citations(owner_id):
            if book.given_id == given_id:
                db.session.delete(book)
                db.session.commit()

        for article in self.get_all_article_citations(owner_id):
            if article.given_id == given_id:
                db.session.delete(article)
                db.session.commit()

        for other in self.get_all_other_citations(owner_id):
            if other.given_id == given_id:
                db.session.delete(other)
                db.session.commit()

    def delete_all_citations(self):
        books = Book.query.delete()
        articles = Article.query.delete()
        other_citations = OtherCitation.query.delete()
        db.session.commit()

        return books + articles + other_citations
    
    def get_citation(self, citation_id):
        #return Citation.query.filter_by(id=citation_id).first()
        pass

    def find_by_given_id(self, given_id, owner_id):
        id = Article.query.filter_by(given_id=given_id, owner_id=owner_id).first()
        id = Book.query.filter_by(given_id=given_id, owner_id=owner_id).first()
        id = OtherCitation.query.filter_by(given_id=given_id, owner_id=owner_id).first()
        return id




citation_repository = CitationRepository()
