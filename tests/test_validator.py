from validator.validator import Validator


def test_none_value():
    v = Validator()
    schema = v.string()
    assert schema.is_valid('') 
    assert schema.is_valid(None)

    schema2 = v.string()
    schema2.required()
    assert not schema2.is_valid('') 
    assert not schema2.is_valid(None)
    assert schema2.is_valid('what does the fox say')

    schema3 = v.number()
    assert schema3.is_valid(None)
    schema3.required()
    assert not schema3.is_valid(None) 
    assert schema3.is_valid(0)  

    schema4 = v.list()
    assert schema4.is_valid(None)
    schema4.required()
    assert not schema4.is_valid(None)


def test_min_len():
    v = Validator()
    assert not v.string().min_len(10).is_valid('Hexlet')
    assert v.string().min_len(6).is_valid('Hexlet')


def test_contains():
    v = Validator()
    assert v.string().contains('what').is_valid('what does the fox say') 
    assert not v.string().contains('whatthe').is_valid('what does the fox say')


def test_priority():
    v = Validator()
    assert v.string().min_len(10).min_len(4).is_valid('Hexlet')


def test_positive():
    v = Validator()
    assert v.number().positive().is_valid(10)
    assert not v.number().positive().is_valid(-7)


def test_range():
    v = Validator()
    schema = v.number()
    schema.range(-5, 5)
    assert not schema.is_valid(-7) 
    assert schema.is_valid(5)


def test_size_of():
    v = Validator()
    schema = v.list()
    schema.sizeof(2)
    assert not schema.is_valid(['hexlet'])
    assert schema.is_valid(['hexlet', 'code-basics'])


def test_shape():
    v = Validator()
    schema = v.dict()

    schema.shape({
    'name': v.string().required(),
    'age': v.number().positive(),
    })

    assert schema.is_valid({'name': 'kolya', 'age': 100}) 
    assert schema.is_valid({'name': 'maya', 'age': None}) 
    assert not schema.is_valid({'name': '', 'age': None})  
    assert not schema.is_valid({'name': 'ada', 'age': -5})  