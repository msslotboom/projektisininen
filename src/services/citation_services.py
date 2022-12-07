from models.citation import Citation
from repositories.citation_repository import citation_repository


class UserInputError(Exception):
    pass


class CitationService:
    def __init__(self, citation_repo=citation_repository):
        self._citation_repo = citation_repo

    def validate_citation(self, authors, title, year, given_id):
        if len(authors)<1 or len(title)<1 or not year or not given_id:
            raise UserInputError("Viitteestä puuttuu tietoja")
        elif len(authors) > 1000 or len(title) > 1000 or year > 2030:
            raise UserInputError("Viite on virheellinen")
        elif self.check_duplicate_given_id(given_id):
            raise UserInputError("Annettu ID on jo käytössä")

    def check_duplicate_given_id(self, given_id):
        id = self._citation_repo.find_by_given_id(given_id)
        if (id is not None):
            return True
        else:
            return False

    def create_citation(self, owner_id, authors, title, year, given_id):
        self.validate_citation(authors, title, year, given_id)

        return self._citation_repo.create_new_citation(Citation(owner_id=owner_id, authors=authors, title=title, year=year, given_id=given_id))
    
    def edit_citation(self, citation_id, authors, title, year, given_id):
        self.validate_citation(authors, title, year, given_id)
        self._citation_repo.edit_citation(citation_id, authors, title, year, given_id)

    def get_citations(self, owner_id):
        citations = []
        for citation in self._citation_repo.get_all_citations(owner_id):
            citations.append((citation.authors, citation.title, citation.year, citation.given_id, citation.id))
        
        return citations

    def get_citations_column_names(self):
        column_names = []
        for name in self._citation_repo.get_all_citation_table_names():
            column_names.append(name)
        
        return column_names
    
    def get_content_by_id(self, citation_id):
        return self._citation_repo.get_citation(citation_id)

    def delete_citation(self, citation_id):
        self._citation_repo.delete_citation(citation_id)

    def delete_all_citations(self):
        return self._citation_repo.delete_all_citations()

citation_service = CitationService()
