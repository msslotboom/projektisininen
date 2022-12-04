from models.citation import Citation
from repositories.citation_repository import citation_repository


class UserInputError(Exception):
    pass


class CitationService:
    def __init__(self, citation_repo=citation_repository):
        self._citation_repo = citation_repo

    def validate_citation(self, authors, title, year):
        if len(authors)<1 or len(title)<1 or not year:
            raise UserInputError("Viitteestä puuttuu tietoja")
        elif len(authors) > 1000 or len(title) > 1000 or year > 2030:
            raise UserInputError("Viite on virheellinen")

    def create_citation(self, owner_id, authors, title, year):
        self.validate_citation(authors, title, year)

        return self._citation_repo.create_new_citation(Citation(owner_id=owner_id, authors=authors, title=title, year=year))
    
    def edit_citation(self, citation_id, authors, title, year):
        self.validate_citation(authors, title, year)
        self._citation_repo.edit_citation(citation_id, authors, title, year)


    def get_citations(self, owner_id):
        citations = []
        for citation in self._citation_repo.get_all_citations(owner_id):
            citations.append((citation.authors, citation.title, citation.year, citation.id))
        
        return citations
    
    def get_content_by_id(self, citation_id):
        return self._citation_repo.get_citation(citation_id)

    def delete_citation(self, citation_id):
        self._citation_repo.delete_citation(citation_id)

    def delete_all_citations(self):
        return self._citation_repo.delete_all_citations()

citation_service = CitationService()
