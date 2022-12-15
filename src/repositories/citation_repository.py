from app import db
from models.article import Article
from models.book import Book
from models.othercitation import OtherCitation


class CitationRepository:
    def create_new_book_citation(self, book: Book):
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

    def edit_other_citation(self, citation_id, author, title, year, other, type):
        OtherCitation.query.filter_by(id=citation_id).\
            update({'author': author})
        OtherCitation.query.filter_by(id=citation_id).\
            update({'title': title})
        OtherCitation.query.filter_by(id=citation_id).\
            update({'year': year})
        OtherCitation.query.filter_by(id=citation_id).\
            update({'type': type})
        OtherCitation.query.filter_by(id=citation_id).\
            update({'other': other})
        db.session.commit()

    def edit_book_citation(self, citation_id, author, title, editor, publisher, year):
        Book.query.filter_by(id=citation_id).\
            update({'author': author})
        Book.query.filter_by(id=citation_id).\
            update({'title': title})
        Book.query.filter_by(id=citation_id).\
            update({'year': year})
        Book.query.filter_by(id=citation_id).\
            update({'editor': editor})
        Book.query.filter_by(id=citation_id).\
            update({'publisher': publisher})
        db.session.commit()

    def edit_article_citation(self, citation_id, author, title, journal, year):
        Article.query.filter_by(id=citation_id).\
            update({'author': author})
        Article.query.filter_by(id=citation_id).\
            update({'title': title})
        Article.query.filter_by(id=citation_id).\
            update({'year': year})
        Article.query.filter_by(id=citation_id).\
            update({'journal': journal})
        db.session.commit()

    def get_all_article_citations(self, user_id):
        return Article.query.filter_by(owner_id=user_id)

    def get_all_book_citations(self, user_id):
        return Book.query.filter_by(owner_id=user_id)

    def get_all_other_citations(self, user_id):
        return OtherCitation.query.filter_by(owner_id=user_id)

    def get_all_citations(self, user_id):

        all_citations = []

        for book in Book.query.filter_by(owner_id=user_id):
            all_citations.append(book)

        for article in Article.query.filter_by(owner_id=user_id):
            all_citations.append(article)

        for other in OtherCitation.query.filter_by(owner_id=user_id):
            all_citations.append(other)

        return all_citations

    def get_all_citation_table_names(self):
        all_table_names = []
        all_table_names.append(Article.__table__.columns.keys())
        all_table_names.append(Book.__table__.columns.keys())
        all_table_names.append(OtherCitation.__table__.columns.keys())
        return all_table_names

    def delete_citation(self, given_id, owner_id):
        for citation in self.get_all_citations(owner_id):
            if citation.given_id == given_id:
                db.session.delete(citation)
                db.session.commit()

    def delete_all_citations(self):
        books = Book.query.delete()
        articles = Article.query.delete()
        other_citations = OtherCitation.query.delete()
        db.session.commit()

        return books + articles + other_citations

    def get_content_by_given_id(self, given_id, owner_id):
        for citation in self.get_all_citations(owner_id):
            if str(citation.given_id) == str(given_id):
                return citation

    def find_by_given_id(self, given_id, owner_id):
        id = Article.query.filter_by(
            given_id=given_id, owner_id=owner_id).first()
        if (id is not None):
            return id
        id = Book.query.filter_by(given_id=given_id, owner_id=owner_id).first()
        if (id is not None):
            return id
        id = OtherCitation.query.filter_by(
            given_id=given_id, owner_id=owner_id).first()
        return id


citation_repository = CitationRepository()
