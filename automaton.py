#automaton.py

class Automaton:
    def __init__(self):
        with open("pda_representation.txt", 'r') as file:
            lines = file.readlines()
            self.states = lines[0].strip().split(' ')
            self.alphabet = lines[1].strip().split(' ')
            self.stack_alphabet = lines[2].strip().split(' ')
            self.start_state = lines[3].strip()
            self.accept_states = lines[4].strip().split(' ')
            self.transitions = {}
            self.stack_actions = {}
            for line in lines[5:]:
                state, read_symbol, stack_action, next_state = line.strip().split(' ')
                stack_pop = stack_action[0]
                stack_push = stack_action[-1]
                self.transitions[(state, read_symbol)] = next_state
                self.stack_actions[(state, read_symbol)] = (stack_pop, stack_push)

    def check(self, string):
        stack = []
        current_state = self.start_state
        transition_list = []
        symbols = list(string)
        while symbols:
            if (current_state, symbols[0]) in self.transitions:
                stack_pop, stack_push = self.stack_actions[(current_state, symbols[0])]
                if stack_pop != 'l':
                    try:
                        temp = stack.pop()
                        if temp != stack_pop:
                            return False
                    except:
                        return False
                if stack_push != 'l':
                    stack.append(stack_push)
                transition_list.append((current_state, symbols[0], self.transitions[(current_state, symbols[0])]))
                current_state = self.transitions[(current_state, symbols[0])]
                symbols.pop(0)
            elif (current_state, 'l') in self.transitions:
                stack_pop, stack_push = self.stack_actions[(current_state, 'l')]
                if stack_pop != 'l':
                    try:
                        temp = stack.pop()
                        if temp != stack_pop:
                            return False
                    except:
                        return False
                if stack_push != 'l':
                    stack.append(stack_push)
                transition_list.append((current_state, 'λ', self.transitions[(current_state, 'l')]))
                current_state = self.transitions[(current_state, 'l')]
            else:
                return False
        if current_state in self.accept_states and not stack: # need an empty stack and end in an accepting state
            return transition_list
        return False
    
    def test_string(self, string):
        print(f'testing accept(A, "{string}")...')
        result = self.check(string)
        if result:
            print('accept')
            for transition in result:
                print(f'{transition[0]} {transition[1]} {transition[2]}')
        else:
            print('reject')
        print()