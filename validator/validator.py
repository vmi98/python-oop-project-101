class Validator:
    def string(self):
        return StringValidator()
    
class StringValidator:
    def __init__(self):
        self.rules = {'required': False, 'min_len': None, 'contains' : None}

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
        if not isinstance(text, str):
            return False
        
        if self.rules['required']:
            if not text:
                return False
            
        if self.rules['min_len']:
            if len(text) >= self.rules['min_len']:
                return False
            
        if self.rules['contains']:
            if self.rules['contains'] not in text:
                return False 

        return True
