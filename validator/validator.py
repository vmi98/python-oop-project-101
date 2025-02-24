from abc import ABC, abstractmethod


class BaseValidator(ABC):
    @abstractmethod
    def is_valid(self, value):
        pass

    @abstractmethod
    def test(self, validator_name, *args):
        pass


class Validator:
    def __init__(self):
        self.validators = {}

    def string(self) -> BaseValidator:
        return StringValidator(self)
    
    def number(self) -> BaseValidator:
        return NumberValidator(self)
    
    def list(self) -> BaseValidator:
        return ListValidator(self)
    
    def dict(self) -> BaseValidator:
        return DictValidator(self)
    
    def add_validator(self, type, name, fn):
        if type not in self.validators:
            self.validators[type] = {}
        self.validators[type][name] = fn
        return self


class StringValidator(BaseValidator):
    def __init__(self, validator):
        self.validator = validator 
        self.rules = {'required': False, 'min_len': None, 'contains': None,
        'customized': {}}

    def test(self, validator_name, *args):
        self.rules['customized'][validator_name] = args
        return self
    
    def required(self):
        self.rules['required'] = True
        return self

    def min_len(self, num):
        self.rules['min_len'] = num
        return self

    def contains(self, text):
        self.rules['contains'] = text
        return self

    def is_valid(self, text):
        if text is None:
            return not self.rules['required']
    
        if not isinstance(text, str):
            return False
        
        if self.rules['required'] and not text:
            return False
            
        if self.rules['min_len'] and len(text) < self.rules['min_len']:
            return False
            
        if self.rules['contains'] and self.rules['contains'] not in text:
            return False 
        
        if self.rules['customized']:
            for validator_name, args in self.rules['customized'].items():
                validator_fn = self.validator.validators.get('string', {}).get(validator_name)
                if not validator_fn(text, *args):
                    return False
        
        return True
    

class NumberValidator(BaseValidator):
    def __init__(self, validator):
        self.validator = validator 
        self.rules = {'required': False, 'positive': False, 'range': None, 'customized': {}}

    def test(self, validator_name, *args):
        self.rules['customized'][validator_name] = args
        return self

    def required(self):
        self.rules['required'] = True
        return self
    
    def positive(self):
        self.rules['positive'] = True
        return self
    
    def range(self, start, end):
        self.rules['range'] = [start, end]

    def is_valid(self, number):
        if number is None and not isinstance(number, int):
            return not self.rules['required']
    
        if not isinstance(number, int):
            return False
            
        if self.rules['positive'] and number <= 0:
            return False
            
        if self.rules['range']:
            if not (self.rules['range'][0] <= number <= self.rules['range'][1]):
                return False
        
        if self.rules['customized']:
            for validator_name, args in self.rules['customized'].items():
                validator_fn = self.validator.validators.get('number', {}).get(validator_name)
                if not validator_fn(number, *args):
                    return False
                
        return True


class ListValidator(BaseValidator):
    def __init__(self, validator):
        self.validator = validator
        self.rules = {'required': False, 'sizeof': None, 'customized': {}}

    def test(self, validator_name, *args):
        self.rules['customized'][validator_name] = args
        return self

    def required(self):
        self.rules['required'] = True
        return self
    
    def sizeof(self, sizeof):
        self.rules['sizeof'] = sizeof
        return self
    
    def is_valid(self, items):
        if items is None and not isinstance(items, list):
            return not self.rules['required']
    
        if not isinstance(items, list):
            return False
            
        if self.rules['sizeof'] and len(items) != self.rules['sizeof']:
            return False 

        if self.rules['customized']:
            for validator_name, args in self.rules['customized'].items():
                validator_fn = self.validator.validators.get('list', {}).get(validator_name)
                if not validator_fn(items, *args):
                    return False
        
        return True
    

class DictValidator(BaseValidator):
    def __init__(self, validator):
        self.validator = validator 
        self.rules = {}

    def test(self, validator_name, *args):
        self.rules['customized'][validator_name] = args
        return self

    def shape(self, rules):
        self.rules = rules
        return self

    def is_valid(self, val_data):
        for k in val_data.keys():
            schema = self.rules[k] 
            if not schema.is_valid(val_data[k]):
                return False
            
        if self.rules.get('customized'):
            for validator_name, args in self.rules['customized'].items():
                validator_fn = self.validator.validators.get('dict', {}).get(validator_name)
                if not validator_fn(val_data, *args):
                    return False
        return True



