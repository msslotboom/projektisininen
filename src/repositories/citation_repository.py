from entities.citation import Citation
import psycopg2
import os

#ympäristömuuttujat tähän

class CitationRepository:
    def __init__(self):
        self._citations = []

    def create_new_citation(self, owner_id):
        pass

    '''
    Viitteiden haku tähän
    '''