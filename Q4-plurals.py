class PluralFiniteStateMachine:
    def __init__(self):
        self.state = 'Start'

    def transition(self, word):
        if self.state == 'Start' and word.endswith('y'):
            self.state = 'Singular'
            return word[:-1] + 'ies'
        elif self.state == 'Start' and word[-1] in ['s', 'x', 'z', 'ch', 'sh']:
            self.state = 'Singular'
            return word + 'es'
        elif self.state == 'Start':
            self.state = 'Singular'
            return word + 's'
        elif self.state == 'Singular':
            return word + 's'

fsm = PluralFiniteStateMachine()
print(fsm.transition('cat')) 
print(fsm.transition('box'))
print(fsm.transition('apple'))
print(fsm.transition('city'))  
