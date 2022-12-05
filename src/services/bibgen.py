from repositories.citation_repository import citation_repository

class Bibgen:
    def __init__(self, citations=citation_repository):
        self._citations = citations
        

    def generate_bib_file(self, owner_id):
        with open ('templates/download.html', 'w') as gen:
            for citation in self._citations.get_all_citations(owner_id):
                gen.write(f' author:  {citation.authors}\n title:  {citation.title}\n year:  {citation.year}\n\n')
                
        


bibliography_generator = Bibgen()