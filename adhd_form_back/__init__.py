from .ontology.Ontology import load_ontology, mock


def tasks():
    load_ontology()
    mock()


tasks()
