from owlready2 import *


def get_medical_condition_by_patient(patient):
    query = f"""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX gufo: <http://purl.org/nemo/gufo#>
        PREFIX : <http://adhd.com#>
        
        SELECT DISTINCT ?condition
        WHERE {'{'}
            ?report rdf:type :MedicalReport;
                    gufo:mediates <{patient}>.
                    gufo:mediates ?condition;
            
            ?condition rdf:type :NeurologicallyBasedCondition;
        {'}'}
    """
    return default_world.sparql(query)
