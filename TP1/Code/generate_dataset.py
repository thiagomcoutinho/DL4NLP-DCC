import gensim
from gensim.parsing.preprocessing import remove_stopwords
from gensim.parsing.preprocessing import strip_short
from random import randrange
from math import floor

corpus = []
with open('text8') as f:
    for line in f:
        for word in line.split():
            corpus.append(word)

print(len(corpus))
short_corpus = []
for word in corpus:
    remove_short = strip_short(word, minsize=3)
    if len(remove_short) > 0:
        short_corpus.append(remove_short)
print(len(short_corpus))
corpus = []

stop_corpus = []
for word in short_corpus:
    remove_stop = remove_stopwords(word)
    if len(remove_stop) > 0:
        stop_corpus.append(remove_stop)

short_corpus = []
print(len(stop_corpus))

new_corpus = []
for word in stop_corpus:
    if word in 'one' or word in 'two' or word in 'three' or word in 'four'\
    or word in 'five' or word in 'six' or word in 'seven' or word in 'eight' or word in 'nine' or word in 'zero':
        continue
    else:
        new_corpus.append(word)

stop_corpus = []
print(len(new_corpus))

def write_file(corpus, size):
    count = 0

    with open(f"output_{size}.txt", "w") as text_file:
        for word in new_corpus:
            text_file.write(f'{word} ')
            count = count + 1

    print(f"DONE! Written {count} words to 'output_{size}.txt'")

backup = new_corpus.copy()
original_size = len(new_corpus)

write_file(new_corpus, 100)

new_corpus = backup.copy()
index_75 = floor(0.25*original_size)
del new_corpus[0:index_75]
write_file(new_corpus, 75)

new_corpus = backup.copy()
index_50 = floor(0.5*original_size)
del new_corpus[0:index_50]
write_file(new_corpus, 50)

new_corpus = backup.copy()
index_25 = floor(0.75*original_size)
del new_corpus[0:index_25]
write_file(new_corpus, 25)