# Program: Text File Word Counter
# Purpose: This program creates a dictionary from the words in a text file and counts the number of times the words show up.
# Developer: Patrick Weatherford
# Week 2 - Assignment 8.1
# DSC 510 T301 - Intro to Programming
# Bellevue University - Professor Michael Eller

# CHANGE LOG:
# Change#:1
# Change(s) Made: added process_file function which outputs results into text file result_file.txt
# Date of Change: 7/15/2021
# Author: Patrick Weatherford
# Change approved by: Professor Michael Eller
# Date moved to production: 7/15/2021


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
    is_word = True  # variable used in looping through characters for each word below
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
                    word = word.replace(char, '')  # replace invalid characters with blank space
                else:
                    continue
            if is_word is True and len(word) > 0:  # if is_word variable true and word is not blank/null add word
                add_word(word, dic)
            else:
                continue


def pretty_print(dic):
    print(f'{nl}Length of the dictionary: {len(dic)}{nl}')
    # sort by frequency then by word
    sort_dic = sorted(dic.items(), key=itemgetter(0))  # first pass sorts on word
    sort_dic2 = sorted(sort_dic, key=itemgetter(1), reverse=True)  # second pass sorts by frequency
    print("{:<15}{:<10}\n".format('WORD', 'FREQUENCY'))  # formatted header
    print(f'{dash*25}')  # line under header
    for i in sort_dic2:
        print("{:<15}{:<10}".format(i[0], i[1]))  # formatted values


def process_file(dic):
    with open('result_file.txt', 'w+') as write_file:  # create new file in which the results will be stored
        write_file.truncate()  # if the same file exists and has data in it, delete it and clear the file
        write_file.write(f'Length of the dictionary: {len(dic)}{2*nl}')  # write dictionary length to file
        # sort by frequency then by word
        sort_dic = sorted(dic.items(), key=itemgetter(0))  # first pass sorts on word
        sort_dic2 = sorted(sort_dic, key=itemgetter(1), reverse=True)  # second pass sorts by frequency
        write_file.write("{:<15}{:<10}\n".format('WORD', 'FREQUENCY'))  # write formatted header
        write_file.write(f'{dash*25}{nl}')  # write line under header
        for i in sort_dic2:
            write_file.write("{:<15}{:<10}\n".format(i[0], i[1]))  # write formatted values
        write_file.seek(0)  # once finished writing set the pointer to the beginning of the file


def main():
    dic = {}
    file = 'gettysburg'
    with open(file, 'r') as read_file:  # open file
        for line in read_file:
            process_line(line, dic)
        process_file(dic)

        # not sure if you want to print to screen using pretty_print or open/read the written file??
#         pretty_print(dic)
        with open('result_file.txt', 'r') as read_result_file:
            print(read_result_file.read())


if __name__ == '__main__':
    main()
