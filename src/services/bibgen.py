from services.citation_services import CitationService
from models.article import Article
from models.book import Book
from os import path

class Bibgen:
    def __init__(self, _citations=CitationService()):
        self._citations = _citations

        

    def generate_bib_text(self, owner_id):
        citation_list = self._citations.get_citations(owner_id)
        
        converted_columns = self.convert_to_bib_variables(citation_list)
        
        reordered_citation_list = self.reorder_citation_list_for_bib(citation_list)

        bib_as_text = ''
        
        for item in range(len(citation_list)):
            for column in range(len(reordered_citation_list[item])):
                if column == 0:
                    bib_as_text += f'@{self._citations.get_citation_name(item)}' + '{' + f'{reordered_citation_list[item][column]},\n'
                elif column + 1 == len(reordered_citation_list[item]):
                    bib_as_text += f'{converted_columns[item][column]} = ' + "{" + f'{reordered_citation_list[item][column]}' + "}\n}"
                else:
                    bib_as_text += f'{converted_columns[item][column]} = ' + "{" + f'{reordered_citation_list[item][column]}' + "},\n"

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
            temporary_list = []
            for attr in item.__table__.columns.keys():
                if not (attr == 'id') and not (attr == 'owner_id'):
                    if attr == 'given_id':
                        temporary_list.insert(0, attr)
                        
                    elif attr == 'authors':
                        temporary_list.append("author")
                        
                    else:
                        temporary_list.append(attr)
                        
            converted_columns.append(temporary_list)

        return converted_columns

    def reorder_citation_list_for_bib(self, list):
        reordered_list = []
        for item in list:
            if isinstance(item, Book):
                reordered_list.append(self._citations.get_book_citation_values(item))
            elif isinstance(item, Article):
                reordered_list.append(self._citations.get_article_citation_values(item))
            else:
                reordered_list.append(self._citations.get_other_citation_values(item))
        
        return reordered_list



bibliography_generator = Bibgen()