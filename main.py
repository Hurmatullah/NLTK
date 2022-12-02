from nltk import book
import matplotlib.pyplot as plt

# Printing the lenght of the vocabulary
# print("Length of vocabulary", len(book.text1))

# # Sorting our text in NLTK using python
# print("Sorting the text", sorted(set(book.text1)))

# Showing the how much distinct terms we have
# print("Distinct terms in our vocabulary", len(set(book.text1)) / len(book.text1))

# Counting the terms that occured in our specified text
# print("Occurance number of a term:", book.text1.count('Moby'))

# Calculation for more texts
# def lexical_diversity(text):
#     return len(set(text)) / len(text)
#
# def percentage(count, total):
#     return 100 * count / total

# Creating a list in NLTK
# sents1 = ['call', "me", "Ishmael"]
# print(sents1[0])

# Indexing our list using python
# sents1 = book.text1.index('and')
# print(sents1)

#Joining two string using python
# joinTexts = ['hey', 'hurmat']
# print(' '.join(joinTexts))

# Showing most frequent terms in text1
# fds = book.FreqDist(book.text1)
# most_common = fds.most_common(50)
# print(most_common)

# printing the number of sample in our sample using N()
# Fdist = book.FreqDist(book.text1)
# print(Fdist.N())

#Print the number of text that came in our sample
# fdist = book.FreqDist(book.text1)
# print("Count the number of this term in our sample", fdist.freq('monstrous'))

#Print the number of text that came in our sample by another way
# fdist = book.FreqDist(book.text1)
# print("Count the text in our sample using this method: ", fdist['monstrous'])

#Sorting the samples from the most frequent term up to unfrequent
# fdist = book.FreqDist(book.text1)
# print((fdist.keys()))

# fdist = book.FreqDist(book.text1)
# for samples in fdist:
#     print(samples)

# Print data with tabulate form
# fdist = book.FreqDist(book.text1)
# print(fdist.tabulate())

# Ploting our sample using matplotlib
# fdist = book.FreqDist(book.text1)
# fdist.plot()

# Printing the length of our sample and print the length of that
# hey = len([set(word.lower()) for word in book.text1])
# print(hey)

#printing the list of terms that is non alfa in our sample
# noneAlfaTerms = len([set(word.lower()) for word in book.text1 if word.isalpha()])
# print(noneAlfaTerms)

#Adding the condition for our code to check whether is title or lower or upper
# texts = book.text1
# for text in texts:
#     if text.islower():
#         print("This text is lower")
#     elif text.istitle():
#         print("This text is title")
#     elif text.isupper():
#         print("This text is upper")
#     else:
#         print("This is punctuation")

from nltk.corpus import gutenberg
print(gutenberg.fileids())
































