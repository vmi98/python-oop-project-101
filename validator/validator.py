class Validator:
    def string(self):
        return StringValidator()
    
    def number(self):
        return NumberValidator()
    
    def list(self):
        return ListValidator()
    
    def dict(self):
        return DictValidator()


class StringValidator:
    def __init__(self):
        self.rules = {'required': False, 'min_len': None, 'contains': None}

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

        return True


class NumberValidator:
    def __init__(self):
        self.rules = {'required': False, 'positive': False, 'range': None}

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
            
        if self.rules['positive'] and number < 0:
            return False
            
        if self.rules['range'] and number not in self.rules['range']:
            return False 

        return True


class ListValidator:
    def __init__(self):
        self.rules = {'required': False, 'sizeof': None}

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

        return True
    

class DictValidator:
    def __init__(self):
        self.rules = {}

    def shape(self, rules):
        self.rules = rules

    def is_valid(self, val_data):
        for k in val_data.keys():
            schema = self.rules[k] 
            if not schema.is_valid(val_data[k]):
                return False
        return True



