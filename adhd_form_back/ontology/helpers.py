def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func

    return decorate


def map_severity(ontology):
    return {
        1: ontology.Severity1,
        2: ontology.Severity2,
        3: ontology.Severity3,
        4: ontology.Severity4,
        5: ontology.Severity5,
        6: ontology.Severity6,
        7: ontology.Severity7,
    }


def map_birth_sex(ontology):
    return {
        'M': ontology.Male,
        'F': ontology.Female,
    }


def build_criterion_a(ontology, data):
    criterion_A = ontology.CriterionA()

    if data['A1a'] > 2:
        criterion_A1a = ontology.CriterionA1a()
        criterion_A1a.hasSeverity = map_severity(ontology)[data['A1a']]
        criterion_A1a.inheresIn = [criterion_A]

    if data['A1b'] > 2:
        criterion_A1b = ontology.CriterionA1b()
        criterion_A1b.hasSeverity = map_severity(ontology)[data['A1b']]
        criterion_A1b.inheresIn = [criterion_A]

    if data['A1c'] > 2:
        criterion_A1c = ontology.CriterionA1c()
        criterion_A1c.hasSeverity = map_severity(ontology)[data['A1c']]
        criterion_A1c.inheresIn = [criterion_A]

    if data['A1d'] > 2:
        criterion_A1d = ontology.CriterionA1d()
        criterion_A1d.hasSeverity = map_severity(ontology)[data['A1d']]
        criterion_A1d.inheresIn = [criterion_A]

    if data['A1e'] > 2:
        criterion_A1e = ontology.CriterionA1e()
        criterion_A1e.hasSeverity = map_severity(ontology)[data['A1e']]
        criterion_A1e.inheresIn = [criterion_A]

    if data['A1f'] > 2:
        criterion_A1f = ontology.CriterionA1f()
        criterion_A1f.hasSeverity = map_severity(ontology)[data['A1f']]
        criterion_A1f.inheresIn = [criterion_A]

    if data['A1g'] > 2:
        criterion_A1g = ontology.CriterionA1g()
        criterion_A1g.hasSeverity = map_severity(ontology)[data['A1g']]
        criterion_A1g.inheresIn = [criterion_A]

    if data['A1h'] > 2:
        criterion_A1h = ontology.CriterionA1h()
        criterion_A1h.hasSeverity = map_severity(ontology)[data['A1h']]
        criterion_A1h.inheresIn = [criterion_A]

    if data['A1i'] > 2:
        criterion_A1i = ontology.CriterionA1i()
        criterion_A1i.hasSeverity = map_severity(ontology)[data['A1i']]
        criterion_A1i.inheresIn = [criterion_A]

    if data['A2a'] > 2:
        criterion_A2a = ontology.CriterionA2a()
        criterion_A2a.hasSeverity = map_severity(ontology)[data['A2a']]
        criterion_A2a.inheresIn = [criterion_A]

    if data['A2b'] > 2:
        criterion_A2b = ontology.CriterionA2b()
        criterion_A2b.hasSeverity = map_severity(ontology)[data['A2b']]
        criterion_A2b.inheresIn = [criterion_A]

    if data['A2c'] > 2:
        criterion_A2c = ontology.CriterionA2c()
        criterion_A2c.hasSeverity = map_severity(ontology)[data['A2c']]
        criterion_A2c.inheresIn = [criterion_A]

    if data['A2d'] > 2:
        criterion_A2d = ontology.CriterionA2d()
        criterion_A2d.hasSeverity = map_severity(ontology)[data['A2d']]
        criterion_A2d.inheresIn = [criterion_A]

    if data['A2e'] > 2:
        criterion_A2e = ontology.CriterionA2e()
        criterion_A2e.hasSeverity = map_severity(ontology)[data['A2e']]
        criterion_A2e.inheresIn = [criterion_A]

    if data['A2f'] > 2:
        criterion_A2f = ontology.CriterionA2f()
        criterion_A2f.hasSeverity = map_severity(ontology)[data['A2f']]
        criterion_A2f.inheresIn = [criterion_A]

    if data['A2g'] > 2:
        criterion_A2g = ontology.CriterionA2g()
        criterion_A2g.hasSeverity = map_severity(ontology)[data['A2g']]
        criterion_A2g.inheresIn = [criterion_A]

    if data['A2h'] > 2:
        criterion_A2h = ontology.CriterionA2h()
        criterion_A2h.hasSeverity = map_severity(ontology)[data['A2h']]
        criterion_A2h.inheresIn = [criterion_A]

    if data['A2i'] > 2:
        criterion_A2i = ontology.CriterionA2i()
        criterion_A2i.hasSeverity = map_severity(ontology)[data['A2i']]
        criterion_A2i.inheresIn = [criterion_A]

    return criterion_A


def get_doctor(ontology):
    doctors = ontology.search(type=ontology.Doctor)

    if len(doctors) == 0:
        doctor = ontology.Doctor()
        doctor.hasName = ['William Praxedes']

        return doctor

    return doctors[0]
