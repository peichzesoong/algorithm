# to count the num of words in the file
def count_words(file_name):
    file = open("Problem2/texts/" + file_name + ".txt", "r", encoding="utf8")
    cfile = file.readlines()
    wordcount = 0
    for line in cfile:
        wordlist = line.split()
        wordcount = wordcount + len(wordlist)
    file.close()
    return wordcount
