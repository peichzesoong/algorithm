from Problem2 import countposnegneut
from Problem2 import countwordstop
from Problem2 import graphs
from Problem2 import senti_conclusion
from Problem2 import stopword
from Problem2 import trie

def prob2():
    file_list = [["citylink1", "citylink2", "citylink3"], ["DHL1", "DHL2", "DHL3"], ["GDEX1", "GDEX2", "GDEX3"],
                 ["J&T1", "J&T2", "J&T3"], ["poslaju1", "poslaju2", "poslaju3"]]
    total_words_arr = []  # total word count of all articles for each courier company
    total_stop_words_arr = []  # total stop word of all articles for each courier company
    total_positive_words_arr = []  # total positive words of all articles for each courier company
    total_negative_words_arr = []  # total negative words of all articles for each courier company
    total_neutral_words_arr = []  # total neutral words of all articles for each courier company
    courier_company = ["City-Link Express", "DHL", "GDEX", "J&T", "Pos Laju"]

    # declare trie for stop word, positive word and negative word
    stop_trie = trie.Trie()
    positive_trie = trie.Trie()
    negative_trie = trie.Trie()

    # store stop words into trie
    stopword.store_stop_trie(stop_trie)
    # to count the total word count and total stop words of all articles for each courier company
    countwordstop.count_and_stop(file_list, total_words_arr, total_stop_words_arr, stop_trie)
    # to store positive words into the trie
    countposnegneut.store_positive_word(positive_trie)
    # to store negative words into the trie
    countposnegneut.store_negative_word(negative_trie)
    # to count number of positive words, negative words and neutral words
    countposnegneut.count(file_list, positive_trie, negative_trie, total_positive_words_arr,
                          total_negative_words_arr, total_neutral_words_arr)

    print("total word count: ", total_words_arr)
    print("total stop words: ", total_stop_words_arr)
    print("total positive words: ", total_positive_words_arr)
    print("total negative words: ", total_negative_words_arr)
    print("total neutral words: ", total_neutral_words_arr)

    # declare all as dictionary
    positive_sentiment = {}
    negative_sentiment = {}
    neutral_sentiment = {}
    sentiratio = {}
    # run sentiment analysis and display result
    senti_conclusion.conclude(courier_company, total_positive_words_arr, total_negative_words_arr,
                              total_neutral_words_arr, positive_sentiment, negative_sentiment,
                              neutral_sentiment, sentiratio)

    # plot and display graphs
    return graphs.plotGraphs(courier_company, total_words_arr, total_stop_words_arr,
                      total_positive_words_arr, total_negative_words_arr, total_neutral_words_arr,
                      positive_sentiment, negative_sentiment, neutral_sentiment)
