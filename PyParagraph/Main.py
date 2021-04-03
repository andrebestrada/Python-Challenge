# Approximate word count
# Approximate sentence count
# Approximate letter count (per word)
# Average sentence length (in words)

import os
import csv
import re

Text=os.path.join("Resources","Data_paragraph_1.txt")
number_of_lines = 0
number_of_words = 0
number_of_sentence = 0


#    for cnt, line in enumerate(fp):
#        print("Line {}: {}".format(cnt, line))
with open(Text) as Paragraph:
    for line in Paragraph:
        line = line.strip("\n")

        words = line.split()
        print(words)
        number_of_words += len(words)
        print("----------------------------------------")
        
        sentence=line.split('.')
        sentence=list(filter(None, sentence))
        # print(sentence)
        number_of_sentence += len(sentence)
        

print("Paragraph Analysis")
print("-----------------")
print(f'Approximate Word Count: {number_of_words}')
print(f'Approximate Sentence Count: {number_of_sentence}')
# print(f'Average Letter Count: {}')
# print(f'Average Sentence Length:{}')

# Paragraph Analysis
# -----------------
# Approximate Word Count: 122
# Approximate Sentence Count: 5
# Average Letter Count: 4.6
# Average Sentence Length: 24.0
