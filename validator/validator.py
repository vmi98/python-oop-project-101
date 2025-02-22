class Validator:
    def string(self):
        return StringValidator()
    
    def number(self):
        return NumberValidator()


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
        if number is None:
            return not self.rules['required']
    
        if not isinstance(number, int):
            return False
        
        if self.rules['required'] and not number and number != 0:
            return False
            
        if self.rules['positive'] and number < 0:
            return False
            
        if self.rules['range'] and number not in self.rules['range']:
            return False 

        return True

    
    

