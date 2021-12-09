# Program: Text File Word Counter
# Purpose: This program creates a dictionary from the words in a text file and counts the number of times the words show up.
# Developer: Patrick Weatherford
# Week 2 - Assignment 7.1
# DSC 510 T301 - Intro to Programming
# Bellevue University - Professor Michael Eller

from operator import itemgetter

nl = '\n'
tab = '\t'
dash = '-'


# add word to dictionary
def add_word(word, dic):
    if word not in dic:
        dic[word] = 1  # if word not already in dictionary add it and set the value to 1
    else:
        dic[word] = dic[word] + 1  # if word already in dictionary set the value to itself plus 1


# process .txt file line and remove unwanted words & characters
def process_line(line, dic):
    line = line.lower()  # set all words to lower case
    for word in line.split():
        if word.isnumeric():  # if word is nothing but numbers, skip
            continue
        elif word.isalpha():  # if word is nothing but word characters, call the add_word function
            add_word(word, dic)
        else:
            for char in word:  # loop through characters in the string and remove unwanted characters & words
                is_word = True  # based on the characters found, if this is false then the word will not be added
                if char.isnumeric():  # if character in word is a number then not a word. Set is_word to False and break loop.
                    is_word = False
                    break
                elif not char.isalnum():  # if character is not a word character or number then replace the character in the word with blank string.
                    word = word.replace(char, '')
                else:
                    continue
            if is_word is True and word != '':
                add_word(word, dic)
            else:
                continue


def pretty_print(dic):
    print(f'{nl}Length of the dictionary: {len(dic)}{nl}')
    # sort by frequency then by word
    sort_dic = sorted(dic.items(), key=itemgetter(0))  # first pass sorts on word
    sort_dic2 = sorted(sort_dic, key=itemgetter(1), reverse=True)  # second pass sorts by frequency
    print("{:<15}{:<10}".format('WORD', 'FREQUENCY'))  # formatted header
    print(f'{dash*25}')  # line under header
    for i in sort_dic2:
        print("{:<15}{:<10}".format(i[0], i[1]))  # formatted values


def main():
    dic = {}
    with open('gettysburg', 'r') as read_file:  # open file
        for line in read_file:
            process_line(line, dic)
    print(pretty_print(dic))


if __name__ == '__main__':
    main()
