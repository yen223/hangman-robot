import hangman_solver

def test_next_letter(test_solver):
    test_set_1 = set(['element', 'letters', 'acrobat'])
    test_set_2 = set(['sapped', 'padded', 'warped'])
    assert test_solver.get_next_letter(test_set_1) == 't'
    assert test_solver.get_next_letter(test_set_2) in ['a', 'd', 'e', 'p']
    return 'get_next_letter() passed'

def main():
    path = r'./dictionary.txt'
    test_solver = hangman_solver.hangman_solver(path)
    print test_next_letter(test_solver)

if __name__ == '__main__':
    main()