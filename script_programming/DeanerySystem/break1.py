from term import Term
class Break(Term):
    def __init__(self, term: Term):
        super().__init__(hour= term.hour, minute=term.minute, duration=term.duration)

    def __str__(self):
        return '---'
    
    def getTerm(self):
        return [(self.hour, self.minute), self.duration]

