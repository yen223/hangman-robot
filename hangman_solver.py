from collections import Counter

class hangman_solver:
    all_words = dict() #Sorted by length
    min_len = 3
    max_len = 3
    wrong_letters = set() #Set of letters that are not in the word
    pattern = []
    game_over = False
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    lives = 11

    def __init__(self, dict_path):
        raw_word_list = []
        with open(dict_path, 'r') as f:
            for word in f:
                if len(word) >= self.min_len:
                    raw_word_list.append(word.strip())
                    if len(word) > self.max_len:
                        self.max_len = len(word)
        print raw_word_list
        print 'Max length is', self.max_len
        for x in range(self.min_len, self.max_len + 1):
            words = set([word.lower() for word in raw_word_list if len(word) == x])
            self.all_words[x] = words

    def begin_solving(self, length):
        self.word_set = self.all_words[length] 
        self.pattern = [''] * length
        while (not self.game_over):
            next_letter = self.get_next_letter()
            print 'Guessed letter:',next_letter
            raw_input()

    def get_next_letter(self):
        '''
        Builds the table of letter frequency to letter in possible words.
        Possible words are words that
            - don't contain wrong letters
            - match the currently know pattern
        Letter frequency refers to how many possible words contain the letter.
        E.g. 
        Possible words = 'element', 'letters', 'acrobat'
        freq('l') = 2
        freq('e') = 3
        freq('z') = 0

        Returns letter with highest frequency
        '''
        self.find_possible_words()
        print self.word_set

    def find_possible_words(self):
        '''
        Find all remaining possible words, by filtering out words which
            - don't match the currently known pattern
            - contain a wrong letter

        Returns list of words.
        '''
        q = set()
        for word in self.word_set:
            for index, x in enumerate(word):
                if x in self.wrong_letters: break
                if self.pattern[index] != '' and self.pattern[index] != x: break
            else:
                q.add(word)

        self.word_set = q
def main():
    path = r'./dictionary.txt'
    solver = hangman_solver(path)

    length = int(raw_input('How many letters does the word have?\n'))
    solver.begin_solving(length)

if __name__ == "__main__":
    import cProfile
    cProfile.run("main()")