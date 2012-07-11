import hangman_solver

def test_next_letter(test_solver):
    test_sets = ['']*2
    test_sets[0] = set(['element', 'letters', 'acrobat'])
    test_sets[1] = set(['sapped', 'padded', 'warped'])
    answers = [test_solver.get_next_letter(x) for x in test_sets]
    assert answers[0] == 't', 'get_next_letter returned ' + str(answers[0])
    assert answers[1] in ['a', 'd', 'e', 'p']
    return 'get_next_letter() passed'

def main():
    path = r'./dictionary.txt'
    test_solver = hangman_solver.hangman_solver(path)
    print test_next_letter(test_solver)
    
if __name__ == '__main__':
    main()
