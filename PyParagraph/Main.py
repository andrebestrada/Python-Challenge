# Approximate word count
# Approximate sentence count
# Approximate letter count (per word)
# Average sentence length (in words)

import os
import csv
import re

Text=os.path.join("Resources","Data_paragraph_1.txt")
Text=os.path.join("Resources","Data_paragraph_2.txt")
number_of_lines = 0
number_of_words = 0
number_of_sentence = 0
words_sum=0

word_dic={}
word_len=[]
sentence_len=[]
#    for cnt, line in enumerate(fp):
#        print("Line {}: {}".format(cnt, line))
with open(Text) as Paragraph:
    for line in Paragraph:
        line = line.strip("\n")

        words = line.split()
        for word in words:
            word_len.append(len(word))


        # print(words)
        # print(word_len)
        number_of_words += len(words)

        # print("\n")
        # print("\n")
        sentence=line.split('.')
        sentence=list(filter(None, sentence))
        # print(sentence)

        for words in sentence:
            oracion=words.split()
            sentence_len.append(len(oracion))
            words_sum+=len(oracion)

        # print(".................................")


        # print(sentence)
        number_of_sentence += len(sentence)
        

        letter_tot=sum(word_len)
        letter_avg=letter_tot/number_of_words


sentence_len=words_sum/len(sentence)
letter_avg=str(round(letter_avg,2))

print("Paragraph Analysis")
print("-------------------")
print(f'Approximate Word Count: {number_of_words}')
print(f'Approximate Sentence Count: {number_of_sentence}')
print(f'Average Letter Count: {letter_avg}')
print(f'Average Sentence Length: {sentence_len}')

# Paragraph Analysis
# -----------------
# Approximate Word Count: 122
# Approximate Sentence Count: 5
# Average Letter Count: 4.6
# Average Sentence Length: 24.0
