from Problem2 import cleanfile

def store_positive_word(positive_trie):
    cleanfile.clean_file("positiveWords")
    positive_clean = open("Problem2/texts/positiveWords_clean.txt", "r", encoding="utf8")
    positiveWords_clean = positive_clean.readlines()

    # to store positive words into the trie
    for i in positiveWords_clean:
        keys = i.split()
    for key in keys:
        positive_trie.insert(key)

    positive_clean.close()


def store_negative_word(negative_trie):
    cleanfile.clean_file("negativeWords")
    negative_clean = open("Problem2/texts/negativeWords_clean.txt", "r", encoding="utf8")
    negativeWords_clean = negative_clean.readlines()

    # to store negative words into the trie
    for i in negativeWords_clean:
        keys = i.split()

    for key in keys:
        negative_trie.insert(key)

    negative_clean.close()


# to count the number of positive, negative and neutral words
def count(file_list, positive_trie, negative_trie, total_positive_words_arr,
          total_negative_words_arr, total_neutral_words_arr):
    for i in file_list:
        total_no_of_positive_words = 0
        total_no_of_negative_words = 0
        total_no_of_neutral_words = 0
        for j in i:
            filename = j + "_clean.txt"
            file = open("Problem2/texts/" + filename, "r", encoding="utf8")
            cfile = file.readlines()

            for line in cfile:
                wordlist = line.split()
                for word in wordlist:
                    if positive_trie.search(word):
                        total_no_of_positive_words = total_no_of_positive_words + 1
                    elif negative_trie.search(word):
                        total_no_of_negative_words = total_no_of_negative_words + 1
                    else:
                        total_no_of_neutral_words = total_no_of_neutral_words + 1
            open("Problem2/texts/" + filename, "w", encoding="utf8").close()  # clear the files after count
            file.close()

        total_positive_words_arr.append(total_no_of_positive_words)
        total_negative_words_arr.append(total_no_of_negative_words)
        total_neutral_words_arr.append(total_no_of_neutral_words)