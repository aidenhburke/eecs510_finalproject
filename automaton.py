#automaton.py

class Automaton:
    def __init__(self):
        self.stack = []
        self.alphabet = set('()+-*/0123456789') 
        
    def _clear_stack(self):
        while self.stack:
            self.stack.pop()
    
    def _push(self, char):
        self.stack.append(char)
    
    def _pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return None
    
    def validate_string(self, string):
        self._clear_stack()

        
