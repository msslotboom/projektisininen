from services.citation_services import CitationService
from os import path

class Bibgen:
    def __init__(self, _citations=CitationService()):
        self._citations = _citations

        

    def generate_bib_text(self, owner_id):
        citation_columns = self._citations.get_citations_column_names()
        converted_columns = self.convert_to_bib_variables(citation_columns)
        citation_list = self._citations.get_citations(owner_id)
        bib_as_text = ''
        for item in range(len(citation_list)):
            for column in range(len(converted_columns)):
                if column == 0:
                    bib_as_text += "@----{" + f'{citation_list[item][column]},\n'
                elif column + 1 == len(converted_columns):
                    bib_as_text += f'{converted_columns[column]} = ' + "{" + f'{citation_list[item][column]}' + "}\n}"
                else:
                    bib_as_text += f'{converted_columns[column]} = ' + "{" + f'{citation_list[item][column]}' + "},\n"

            bib_as_text += '\n'
                

        return bib_as_text
                
    def generate_bib_file(self, text):
        this_directory = path.dirname(__file__)
        download_html_path = path.join(this_directory, "..", "templates", "download.html")
        with open(download_html_path, 'w') as gen:
            gen.write(text)

    def convert_to_bib_variables(self, columns):
        converted_columns = []
        for item in columns:
            if not (item == 'id') and not (item == 'owner_id'):
                if item == 'given_id':
                    converted_columns.insert(0, item)
                elif item == 'authors':
                    converted_columns.append("author")
                else:
                    converted_columns.append(item)

        return converted_columns


        


bibliography_generator = Bibgen()