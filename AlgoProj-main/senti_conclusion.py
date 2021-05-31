# to conclude the sentiment analysis
def conclude(courier_company, total_positive_words_arr, total_negative_words_arr,
             total_neutral_words_arr, positive_sentiment, negative_sentiment, neutral_sentiment):
    ratio = {}

    for i in range(len(courier_company)):
        ratio[courier_company[i]] = round(total_positive_words_arr[i]/total_negative_words_arr[i], 2)

    # if more positive words, positive sentiment. more negative words, negative sentiment
    for i in range(len(courier_company)):
        if ratio.get(courier_company[i]) > 1:
            positive_sentiment[courier_company[i]] = ratio.get(courier_company[i])
            print(courier_company[i] + " has a positive sentiment.")
        elif ratio.get(courier_company[i]) < 1:
            negative_sentiment[courier_company[i]] = total_negative_words_arr[i]
            print(courier_company[i] + " has a negative sentiment.")
        else:
            neutral_sentiment[courier_company[i]] = total_neutral_words_arr[i]
            print(courier_company[i] + " has a neutral sentiment.")

    # print the company that has the best sentiment based on most positive word count
    # from the positive sentiment companies only.
    print(positive_sentiment)
    print(negative_sentiment)
    print(neutral_sentiment)
    print(best_senti(positive_sentiment))

def best_senti(positive_sentiment):
    best_sentiment = max(positive_sentiment, key=positive_sentiment.get)
    return best_sentiment + " has the best sentiment based on ratio of positive words to negative words with " + str(
        positive_sentiment.get(best_sentiment))

