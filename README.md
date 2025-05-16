## Data validator

The project is part of Hexlet course assignments. Data validator is a library that can be used to check the correctness of any data. The project is based on the yup library.

### Hexlet tests and linter status:
[![Actions Status](https://github.com/vmi98/python-oop-project-101/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/vmi98/python-oop-project-101/actions)

## Features

String validator:
- required – non-empty value (not None) and any non-empty string
- min_len – string is equal to or longer than the specified number
- contains – string contains a certain substring.

Number validator:
- required – non-empty value (not None) and any number including zero
- positive – positive number
- range – range in which numbers must fall including boundaries.

List validator:
- required – the list data type is required
- sizeof – the array length is equal to the specified one.

Dictionary validator: check data by keys.

Add custom valdator

## Tech Stack

- Python
- Ruff (linting)
- pytest (testing)
- uv (package management)

## Installation
```
git clone https://github.com/vmi98/python-oop-project-101.git
cd python-oop-project-101

make install
```

## Run tests
```
make test
```

## Usage
```
# Create validator
v = Validator()

# Specify the type of data to be checked (string, number, list, dict) 
# Create validation schema
# Check using is_valid() method

schema = v.number()
schema.positive().is_valid(10) # True
```

```
# Example for dict

v = Validator()

schema = v.dict()

schema.shape({
    'name': v.string().required(),
    'age': v.number().positive(),
})

schema.is_valid({'name': 'kolya', 'age': 100})  # True
schema.is_valid({'name': 'maya', 'age': None})  # True
schema.is_valid({'name': '', 'age': None})  # False
schema.is_valid({'name': 'ada', 'age': -5})  # False
```

```
# Example of adding custom valdator
v = Validator()

fn = lambda value, start: value.startswith(start)
# Method of adding new validator
# add_validator(type, name, fn)
v.add_validator('string', 'startWith', fn)

# New validators with test() method
schema = v.string().test('startWith', 'H')
schema.is_valid('exlet') # False
schema.is_valid('Hexlet') # True

fn = lambda value, min: value >= min
v.add_validator('number', 'min', fn)

schema = v.number().test('min', 5)
schema.is_valid(4) # False
schema.is_valid(6) # True
```
