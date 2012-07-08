with open(r'./dictionary.txt', 'r') as f:
    words = [strip(word) for word in f]

print words