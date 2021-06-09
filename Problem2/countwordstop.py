from Problem2 import cleanfile
from Problem2 import countwords
from Problem2 import stopword

# to count the total word count and total stop words of all articles for each courier company
def count_and_stop(file_list, total_words_arr, total_stop_words_arr, stop_trie):
    for i in file_list:
        total_no_of_words = 0
        total_no_of_stopwords = 0
        for j in i:
            cleanfile.clean_file(j)
            # before removing stop words
            no_of_words = countwords.count_words(j + "_clean")
            total_no_of_words = total_no_of_words + no_of_words
            stopword.filter_stop_words(j + "_clean", stop_trie)
            # no of stop words
            no_of_stopwords = no_of_words - countwords.count_words(j + "_clean")
            total_no_of_stopwords = total_no_of_stopwords + no_of_stopwords

        total_words_arr.append(total_no_of_words)
        total_stop_words_arr.append(total_no_of_stopwords)
