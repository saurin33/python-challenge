import os
import string

paragraph_txt = os.path.join(
    "/Users/saurin/Desktop/Resources", "paragraph_1.txt")
word_list = []
word_count = 0
sentence_count = 0
sentence_list = []
sentence_length = 0
letter_list = []
letter_count = 0

with open(paragraph_txt, "r")as file:
    for line in file:
        words = line.split()
        word_list.append(words)
        word_count += len(words)

        sentence = line.split('.')
        sentence_list.append(sentence)
        sentence_count += len(sentence)
        sentence_length = round(word_count/sentence_count)

    print("Paragraph Analysis")
    print("--------------------------")
    print(f"Approximate Word Count: {word_count}")
    print(f"Approximate Sentence Count: {sentence_count}")
    print(f"Average Sentence Length: {sentence_length}")

    letter_count = [len(w) for w in words]
    total_letters = sum(letter_count)

    letter_count = total_letters/word_count
    average_letter_count = round(letter_count, 1)

    print(f"Average Letter Count: {average_letter_count}")
