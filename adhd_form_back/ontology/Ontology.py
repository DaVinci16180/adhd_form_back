from owlready2 import *
from .helpers import *
from .sparql import *


def load_ontology():
    if open_ontology.ontology is None:
        try:
            open_ontology.ontology = get_ontology('adhd_form_back/ontology/adhd-ontology.owx').load()
            print('Ontology loaded in background')
        except OwlReadyOntologyParsingError as e:
            print('Failed to load ontology')


@static_vars(ontology=None)
def open_ontology():
    if open_ontology.ontology is None:
        open_ontology.ontology = get_ontology('adhd_form_back/ontology/adhd-ontology.rdf').load()
        print('Ontology loaded on demand')

    return open_ontology.ontology


def reason():
    onto = open_ontology()

    with onto:
        sync_reasoner()


def mock():
    onto = open_ontology()

    patient = onto.Patient()
    patient.hasName = ['Joaquim Bezerra']
    patient.hasDocument = ['123.456.789-00']
    # patient.hasDateOfBirth = data['dateOfBirth']
    patient.hasBirthSex = map_birth_sex(onto)['M']

    condition = onto.NeurologicallyBasedCondition()

    mock_data = {
        'A1a': 5,
        'A1b': 5,
        'A1c': 5,
        'A1d': 5,
        'A1e': 5,
        'A1f': 5,
        'A1g': 5,
        'A1h': 5,
        'A1i': 5,
        'A2a': 1,
        'A2b': 1,
        'A2c': 1,
        'A2d': 1,
        'A2e': 1,
        'A2f': 1,
        'A2g': 1,
        'A2h': 1,
        'A2i': 1,
    }

    criterion_A = build_criterion_a(onto, mock_data)
    criterion_A.inheresIn = [condition]

    criterion_B = onto.CriterionB()
    criterion_B.inheresIn = [condition]

    criterion_C = onto.CriterionC()
    criterion_C.inheresIn = [condition]

    criterion_D = onto.CriterionD()
    criterion_D.inheresIn = [condition]

    criterion_E = onto.CriterionE()
    criterion_E.inheresIn = [condition]

    doctor = get_doctor(onto)
    report = onto.MedicalReport()

    report.mediates = [patient, doctor, condition]
    patient.suffersFrom = [condition]

    reason()


def register_form(data):
    onto = open_ontology()

    patient = onto.Patient()
    patient.hasName = [data['name']]
    patient.hasDocument = [data['document']]
    # patient.hasDateOfBirth = data['dateOfBirth']
    patient.hasBirthSex = map_birth_sex(onto)[data['birthSex']]

    condition = onto.NeurologicallyBasedCondition()

    criterion_A = build_criterion_a(onto, data)
    criterion_A.inheresIn = [condition]

    if data['criterionB']:
        criterion_B = onto.CriterionB()
        criterion_B.inheresIn = [condition]

    if data['criterionC']:
        criterion_C = onto.CriterionC()
        criterion_C.inheresIn = [condition]

    if data['criterionD']:
        criterion_D = onto.CriterionD()
        criterion_D.inheresIn = [condition]

    if data['criterionE']:
        criterion_E = onto.CriterionE()
        criterion_E.inheresIn = [condition]

    doctor = get_doctor(onto)
    report = onto.MedicalReport()

    report.mediates = [patient, doctor, condition]

    reason()


def fetch_patient_list():
    onto = open_ontology()

    patients = onto.search(type=onto.Patient, hasName='*')
    result = []

    for patient in patients:
        result.append({
            'name': patient.hasName[0],
            'iri': patient.iri,
        })

    return result


def create_report(data):
    onto = open_ontology()

    patient = onto.search_one(iri=data['iri'])
    report = onto.search_one(type=onto.MedicalReport, mediates=patient)
    condition = list(filter(lambda x: onto.NeurologicallyBasedCondition in x.is_a or onto.ADHD in x.is_a, report.mediates))[0]

    result = {
        'name': patient.hasName[0],
        'document': patient.hasDocument[0],
        'birthSex': 'Masculino' if patient.hasBirthSex is onto.Male else 'Feminino',
    }

    if onto.ADHD not in condition.is_a:
        result['condition'] = 'Outra condição'
        return result

    result['condition'] = 'TDAH'
    inverse = list(condition.get_inverse_properties())

    a1 = list(filter(lambda x: any(row == onto.CriterionA1 for row in x[0].is_a), inverse))
    a2 = list(filter(lambda x: any(row == onto.CriterionA2 for row in x[0].is_a), inverse))

    inverse = list(a1[0][0].get_inverse_properties() if a1 else [])
    inverse.extend(list(a2[0][0].get_inverse_properties() if a2 else []))

    average = 0
    for row in inverse:
        average += row[0].hasSeverity.hasValue

    average /= len(inverse)

    score = 1 if average >= 5 else 0
    if a1 and a2:
        result['type'] = 'Combinado'
        score += 1 if len(inverse) > 14 else 0
    elif a1:
        result['type'] = 'Predominantemente Hiperativo'
        score += 1 if len(inverse) > 7 else 0
    elif a2:
        result['type'] = 'Predominantemente Hiperativo'
        score += 1 if len(inverse) > 7 else 0

    if score == 0:
        result['severity'] = 'Leve'
    elif score == 1:
        result['severity'] = 'Médio'
    elif score == 2:
        result['severity'] = 'Grave'

    return result
