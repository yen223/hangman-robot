'''
This is the entry-point to the Hangman game.
'''
from hangman_solver import hangman_solver as solver

# def __init__(self, solution):
#    self.solution = solution
#    self.lives = 11

def check_result(pattern, letter, solution):
    '''
    Returns the new pattern based on the given letter.
    '''
    new_pattern = []
    if letter not in solution:
        return pattern, -1
    else:
        life = 0
        for index, x in enumerate(solution):
            if x == letter:
                new_pattern.append(x)
            else:
                new_pattern.append(pattern[index])

    return ''.join(new_pattern), life


def main():
    lives = 11
    solution = raw_input('Please enter random word:')
    solver_obj = solver(r'./dictionary.txt')
    s = solver_obj.begin_solving(len(solution))
    pattern, next_letter = s.next()
    while (1):
        new_pattern, life = check_result(pattern, next_letter, solution)
        lives += life
        print 'Result:', new_pattern
        if '_' not in new_pattern:
            print "You have guessed the word!"
            break
        if lives < 0:
            print 'No more lives left!'
            break
        else:
            print lives,"lives left"
        raw_input()
        s.next()
        pattern, next_letter = s.send(new_pattern)
    s.close()

    

if __name__ == "__main__":
    main()
