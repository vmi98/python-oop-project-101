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
    assert schema3.is_valid(0)
    schema3.required()
    assert schema3.is_valid(0)
    assert not schema3.is_valid(None)  


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