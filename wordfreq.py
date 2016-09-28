# coding=utf-8

# COPYRIGHT by PARK, SIHYUNG, 08-24-2016

# Analyze Top 20 most-used words (longer than 2) in the standard input text
# 인풋 텍스트 파일에서 가장 많이 등장하는 단어 상위 20위를 출력하고 전체 순위를 텍스트 파일로 저장한다.
# 일반적인 복수형, 과거형을 가지는 단어의 경우 같은 단어로 인식하도록 했음 - 일반적이지 않은 경우는 아님...

# [사용 방법]   $ python word_freq.py input.txt
# [아웃풋 파일]    /your_directory/inputFileName_out.txt

"""
This module provides several functions used for counting words and their appear frequencies from input texts.
You can also "run" this module as a script by typing [[python wordfreq.py InputFile.txt]] at the terminal.
"""

def punc_marks():
    """Returns a list of punctuation marks."""
    marks = [",", "-", "_", "'", '"', "!", "?", "~", "‘", ".",
         ".", "+", "/", "#", "(", ")", "`", ":", ";", "’"]
    return marks

def words_to_exclude():
    """Returns a list of words to exclude when counting words from text."""
    excludes = ["as", "is", "am" ,"are", "was", "were", "will", "would", "could",
           "might", "have", "been", "be", "had", "has", "also", "of", "for", "while", "can",
           "by", "from", "in", "on", "a", "the", "and", "though", "although", 
           "that", "such", "should", "to", "not", "nor", "or", "thus", "after",
           "before", "with", "without", "it", "its", "his", "one's", "i", 
            "her", "him", "their", "our", "us", "which", "at", "a", "an", "but",
           "you", "if", "this", "very", "me", "your", "our", "we", "does", "did", "what",
           "who", "when", "where", "why", "there", "these", "research", "researches", "both", "important", "between", "sometimes", "others", "ways", "about", "describes", "used", "they", "strongly", "more", "may", "many", "different", ]
    return excludes

def filtered_words(in_in):
    """Returns a list of words which appears in the text file, filtered by the words in 'words_to_exclude()'."""
    marks = punc_marks()
    excludes = words_to_exclude()
    fhand = open(in_in, "r")
    whole_words = list()
    for l in fhand:
        l = l.lower().strip()
        for mark in marks:
            l = l.replace(mark, " ")
        whole_words += l.split()
    fhand.close()
    for word in whole_words[:]:
        if word in excludes or len(word)<2:
            whole_words.remove(word)
    return whole_words

def wordcount(filtered_words):
    "Returns a dictionary of words(as key) and their corresponding frequencies(as value)"
    wordcount = dict()
    for word in filtered_words[:]:
        wordcount[word] = wordcount.get(word, 0) + 1
    for word in filtered_words[:]:
        for iter_word in filtered_words[:]:
            if iter_word.find(word)==0 and iter_word!=word and (iter_word.endswith("s") or iter_word.endswith("ed")):
                wordcount[iter_word] = wordcount[iter_word] + wordcount[word]
                wordcount[word] = 0
    wordcount = [(v, k) for (k, v) in wordcount.items() if k[0].isalpha]
    wordcount.sort(reverse=True)
    return wordcount

def top(wordcount, n=20):
    """Prints out the top 'n'(default=20) most frequently used words in the text."""
    for k, v in wordcount[:n+1]:
        print " ", k, v

def wordcount_to_text(in_in, wordcount):
    """Write a text file, which contains the whole list of words ans their frequencies, named after the input file."""
    out_out = in_in.split(".")[0]+"_out.txt"
    out = open(out_out, "w")
    for k, v in wordcount[:]:
        out.write(str(k)+" "+str(v)+" \n")
    print("   - Output file: '"+out_out+"' is generated at current directory")

def in_title(in_in, wordcount):
    marks = punc_marks()
    excludes = words_to_exclude()
    fhand = open(in_in, "r")
    first_line = list()
    fl = fhand.readline()
    fl = fl.lower().strip()
    for mark in marks:
        fl = fl.replace(mark, " ")
    first_line += fl.split()
    fhand.close()
    for word in first_line[:]:
        if word in excludes or len(word)<2:
            first_line.remove(word)
    print first_line
    print "  -------------TITLE-------------"
    for k, v in wordcount[:]:
        if v in first_line:
            print " ", k, v

if __name__ == "__main__":
    import sys
    in_in = sys.argv[1]
#
    top(wordcount(filtered_words(in_in)))
    in_title(in_in, wordcount(filtered_words(in_in)))
    wordcount_to_text(in_in, wordcount(filtered_words(in_in)))

