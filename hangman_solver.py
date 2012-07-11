from collections import Counter
from random import choice
class hangman_solver:
    all_words = dict() #Sorted by length
    min_len = 3
    max_len = 3
    used_letters = set() #Set of letters that are not in the word
    pattern = []
    game_over = False
    alphabet = set('abcdefghijklmnopqrstuvwxyz')

    def __init__(self, dict_path):
        raw_word_list = []
        with open(dict_path, 'r') as f:
            for word in f:
                if len(word) >= self.min_len:
                    raw_word_list.append(word.strip())
                    if len(word) > self.max_len:
                        self.max_len = len(word)
        # print raw_word_list
        print 'Max length is', self.max_len
        for x in range(self.min_len, self.max_len + 1):
            words = set([word.lower() for word in raw_word_list if len(word) == x])
            self.all_words[x] = words

    def begin_solving(self, length):
        self.word_set = self.all_words[length] 
        self.pattern = '_' * length
        while (1):
            self.word_set = self.find_possible_words(self.pattern, self.used_letters, self.word_set)
            next_letter = self.get_next_letter(self.word_set, self.used_letters)
            print 'Guessed letter:',next_letter
            self.used_letters.add(next_letter)
            #raw_input()
            yield self.pattern, next_letter
            self.pattern = (yield)
            print 'New pattern =', self.pattern

    def get_next_letter(self, word_set, used_letters):
        '''
        Builds the table of letter frequency to letter given a set of words.
        Letter frequency refers to how many possible words contain the letter.
        E.g. 
        Possible words = 'element', 
                         'letters', 
                         'acrobat'
        freq('l') = 2
        freq('t') = 3
        freq('z') = 0

        Returns letter with highest frequency
        '''
        if len(word_set) == 0:
            unused_letters = list(set(self.alphabet).difference(used_letters))
            ret = choice(unused_letters)
        else:
            letter_count = Counter()
            for word in word_set:
                letter_count += Counter(set(word))
            # c = letter_count.most_common()
            result = 0
            ret = ''
            for key,value in letter_count.iteritems():
                if value > result and key not in used_letters:
                    result = value
                    ret = key
                #print key,':',value
        return ret
        # return c[0][0]
        

    def find_possible_words(self, pattern, used_letters, word_set):
        '''
        Find all remaining possible words, by filtering out words which
            - don't match the currently known pattern
            - contain a wrong letter

        Returns set of words.
        '''
        q = set()
        #print word_set
        print 'Finding words...'
        for word in word_set:
            for index, x in enumerate(word):
                if x in used_letters and x not in pattern: break
                if pattern[index] != '_' and pattern[index] != x: break
            else:
                print word
                q.add(word)

        return q

def main():
    path = r'./dictionary.txt'
    solver = hangman_solver(path)

    length = int(raw_input('How many letters does the word have?\n'))
    solver.begin_solving(length)

if __name__ == "__main__":
    import cProfile
    cProfile.run("main()")
