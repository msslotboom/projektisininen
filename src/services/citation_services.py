from models.citation import Citation
from repositories.citation_repository import citation_repository


class UserInputError(Exception):
    pass


class CitationService:
    def __init__(self, citation_repo=citation_repository):
        self._citation_repo = citation_repo

    def validate_citation(self, authors, title, year):
        if not authors or not title or not year:
            raise UserInputError("Viitteestä puuttuu tietoja")

    def create_citation(self, owner_id, authors, title, year):
        self.validate_citation(authors, title, year)

        return self._citation_repo.create_new_citation(Citation(owner_id=owner_id, authors=authors, title=title, year=year))


citation_service = CitationService()
