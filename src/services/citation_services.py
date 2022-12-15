from models.book import Book
from models.article import Article
from models.othercitation import OtherCitation
from repositories.citation_repository import citation_repository
import sys


class UserInputError(Exception):
    pass


class CitationService:
    def __init__(self, citation_repo=citation_repository):
        self._citation_repo = citation_repo

    def validate_citation(self, authors, title, year, given_id, owner_id):
        if len(authors) < 1 or len(title) < 1 or not year:
            raise UserInputError("Viitteestä puuttuu tietoja")
        elif len(authors) > 1000 or len(title) > 1000 or year > 2030:
            raise UserInputError("Viite on virheellinen")
        elif self.check_duplicate_given_id(given_id, owner_id):
            raise UserInputError("Annettu ID on jo käytössä")

    def generate_given_id(self, authors, year):
        return authors.split(",")[0].replace(" ", "_") + str(year)

    def check_duplicate_given_id(self, given_id, owner_id):
        return self._citation_repo.find_by_given_id(given_id, owner_id) is not None

    def create_book_citation(self, owner_id, given_id, author, title, editor, publisher, year):
        self.validate_citation(author, title, year, given_id, owner_id)
        return self._citation_repo.create_new_book_citation(Book(
            owner_id=owner_id, given_id=given_id, author=author, title=title, editor=editor, publisher=publisher, year=year
        ))

    def create_article_citation(self, owner_id, given_id, author, title, journal, year):
        self.validate_citation(author, title, year, given_id, owner_id)

        return self._citation_repo.create_new_book_citation(Article(
            owner_id=owner_id, given_id=given_id, author=author, title=title, journal=journal, year=year
        ))

    def create_other_citation(self, owner_id, given_id, author, title, type, note, year):
        self.validate_citation(author, title, year, given_id, owner_id)

        return self._citation_repo.create_new_other_citation(OtherCitation(
            owner_id=owner_id, given_id=given_id, author=author, title=title, type=type, note=note, year=year
        ))

    def edit_other_citation(self, citation_id, authors, title, type, note, year):
        self._citation_repo.edit_other_citation(
            citation_id=citation_id, author=authors,
            title=title, type=type, note=note, year=year)

    def edit_book_citation(self, citation_id, authors, title, editor, publisher, year):
        self._citation_repo.edit_book_citation(
            citation_id=citation_id, author=authors,
            title=title, publisher=publisher, editor=editor, year=year)

    def edit_article_citation(self, citation_id, authors, title, journal, year):
        self._citation_repo.edit_article_citation(
            citation_id=citation_id, author=authors,
            title=title, journal=journal, year=year)

    def get_article_citations(self, owner_id):
        article_citations = []
        for article_citation in self._citation_repo.get_all_article_citations(owner_id):
            article_citations.append(article_citation)
        return article_citations

    def get_book_citations(self, owner_id):
        book_citations = []
        for book_citation in self._citation_repo.get_all_book_citations(owner_id):
            book_citations.append(book_citation)
        return book_citations

    def get_other_citations(self, owner_id):
        other_citations = []
        for other_citation in self._citation_repo.get_all_other_citations(owner_id):
            other_citations.append(other_citation)
        return other_citations

    def get_book_citation_values(self, book):
        return (book.given_id, book.author, book.editor, book.title, book.publisher, book.year)

    def get_article_citation_values(self, article):
        return (article.given_id, article.author, article.title, article.journal, article.year)

    def get_other_citation_values(self, other):
        return (other.given_id, other.author, other.title, other.type, other.note, other.year)

    def get_citations(self, owner_id):
        citations = []
        citation_query_list = self._citation_repo.get_all_citations(owner_id)

        for citation in citation_query_list:
            citations.append(citation)

        return citations

    def get_citation_name(self, citation):
        if isinstance(citation, Article):
            return "article"
        elif isinstance(citation, Book):
            return "book"
        else:
            return "misc"

    def get_citations_column_names(self):
        column_names = []
        for name in self._citation_repo.get_all_citation_table_names():
            column_names.append(name)

        return column_names

    def get_content_by_id(self, given_id, owner_id):
        return self._citation_repo.get_content_by_given_id(given_id=given_id, owner_id=owner_id)

    def delete_citation(self, given_id, owner_id):
        self._citation_repo.delete_citation(given_id, owner_id)

    def delete_all_citations(self):
        self._citation_repo.delete_all_citations()


citation_service = CitationService()
