class hangman_checker:
    solution = ''
    def __init__(self, solution):
        self.solution = solution
        
    def check_result(self, letter):
        '''
        Returns the new pattern based on 