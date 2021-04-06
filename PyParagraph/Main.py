# Approximate word count
# Approximate sentence count
# Approximate letter count (per word)
# Average sentence length (in words)

import os
import csv
import re

Text=os.path.join("Resources","Data_paragraph_1.txt")
# Text=os.path.join("Resources","Data_paragraph_2.txt")

letter_Count = 0
word_count = 0
sentence_count = 0

with open(Text, 'r') as Paragraph:   
        
    lines = Paragraph.read()

    sentences = re.split("(?<=[.!?]) +", lines)

    # For the second text, sentences must be separated by 2 lines
    # sentences = re.split('\n\n', lines)
    
    words = re.split(r' ', lines)                    
    print(sentences)
    for word in words:
        letter_Count = letter_Count + len(word)

    word_count=len(words)
    sentence_count=len(sentences)
    avg_letter=round(letter_Count/len(words),2)
    avg_word=round(len(words)/len(sentences),2)
    
    print("Paragraph Analysis")
    print("-----------------")
    print("Approximate Word Count:: "+str(word_count))
    print("Approximate Sentence Count: "+str(sentence_count))
    print("Average Letter Count: "+ str(avg_letter))
    print("Average Sentence Length: "+ str(avg_word))

# Paragraph Analysis
# -----------------
# Approximate Word Count: 122
# Approximate Sentence Count: 5
# Average Letter Count: 4.6
# Average Sentence Length: 24.0
