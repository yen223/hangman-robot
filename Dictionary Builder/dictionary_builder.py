import re

ascii_pattern = re.compile('[^A-Za-z]')

'''with open(r'./dictionary_raw.txt', 'r') as f:
    words = [word.strip() for word in f if ascii_pattern.search(word.strip()) == None]

with open(r'./dictionary.txt', 'w') as f2:
    for word in words:
        f2.write(word + '\n')
        print word'''

word_set = set()
with open(r'./dictionary_paths.txt', 'r') as f:
    for path in f:
        full_path = r'./scowl-7.1/final/' + path.strip()
        with open(full_path, 'r') as f2:
            for word in f2:
                if ascii_pattern.search(word.strip()) == None:
                    word_set.add(word.strip())
word_list = list(word_set)
word_list.sort()

with open (r'../dictionary.txt', 'w') as dict_file:
    for word in word_list:
        dict_file.write(word + '\n')
        print word