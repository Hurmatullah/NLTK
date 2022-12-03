# from nltk.corpus import gutenberg
#
# for fileids in gutenberg.fileids():
#     numChars = len(gutenberg.raw(fileids))
#     numWords = len(gutenberg.words(fileids))
#     numSents = len(gutenberg.sents(fileids))
#     numVocab = len(set(w.lower() for w in gutenberg.words(fileids)))
#
#     print(round(numChars / numWords), round(numWords / numSents), round(numWords / numVocab), fileids)


from nltk.corpus import brown

listGeneres = [(genre, word) for genre in ['news', 'romance'] for word in brown.words(categories=genre)]




































