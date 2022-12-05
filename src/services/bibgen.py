from services.citation_services import CitationService

class Bibgen:
    def __init__(self, _citations=CitationService()):
        self._citations = _citations
        

    def generate_bib_file(self, owner_id):
        with open ('src/templates/download.html', 'w') as gen:
            for citation in self._citations.get_citations(owner_id):
                gen.write(f' author:  {citation[0]}\n title:  {citation[1]}\n year:  {citation[2]}\n\n')
                
        


bibliography_generator = Bibgen()