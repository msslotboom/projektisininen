from services.citation_services import CitationService
from os import path

class Bibgen:
    def __init__(self, _citations=CitationService()):
        self._citations = _citations

        

    def generate_bib_file(self, owner_id):
        this_directory = path.dirname(__file__)
        download_html_path = path.join(this_directory, "..", "templates", "download.html")
        with open (download_html_path, 'w') as gen:
            for citation in self._citations.get_citations(owner_id):
                gen.write(f' author:  {citation[0]}\n title:  {citation[1]}\n year:  {citation[2]}\n\n')
                
        


bibliography_generator = Bibgen()