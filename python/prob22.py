#!/usr/bin/env python
# What is the total of all the name scores in the file?

def alphabet_pos(n):
    return {
            'a': 1,
            'b': 2,
            'c': 3,
            'd': 4,
            'e': 5,
            'f': 6,
            'g': 7,
            'h': 8,
            'i': 9,
            'j': 10,
            'k': 11,
            'l': 12,
            'm': 13,
            'n': 14,
            'o': 15,
            'p': 16,
            'q': 17,
            'r': 18,
            's': 19,
            't': 20,
            'u': 21,
            'v': 22,
            'w': 23,
            'x': 24,
            'y': 25,
            'z': 26
            }[n]

def alpha_sort(words):
    sorted_words = sorted(words)

    return sorted_words

def word_score(word):
    score = 0
    for letter in word:
        score += alphabet_pos(letter.lower())

    return score

def main():
    names_file = open("names.txt", 'r')
    names = names_file.read()
    names_file.close()
    names = names.replace('"', '')
    names = names.split(',')
    names = alpha_sort(names)
    scores = []
    i = 0
    score = None
    while i < len(names):
        score = (i + 1) * word_score(names[i])
        scores.append(score)
        i += 1

    print(sum(scores))

main()
