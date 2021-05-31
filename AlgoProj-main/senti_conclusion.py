import math


# to conclude the sentiment analysis
def conclude(courier_company, total_positive_words_arr, total_negative_words_arr,
             total_neutral_words_arr, positive_sentiment, negative_sentiment, neutral_sentiment
             , total_words_arr, total_stop_words_arr):
    positive_sentper = {}
    # if more positive words, positive sentiment. more negative words, negative sentiment
    for i in range(len(courier_company)):
        if total_positive_words_arr[i] > total_negative_words_arr[i]:
            positive_sentiment[courier_company[i]] = total_positive_words_arr[i]
            print(courier_company[i] + " has a positive sentiment.")
            positive_sentper[courier_company[i]] = round(
                total_positive_words_arr[i] / (total_words_arr[i] - total_stop_words_arr[i]) * 100, 2)
        elif total_positive_words_arr[i] < total_negative_words_arr[i]:
            negative_sentiment[courier_company[i]] = total_negative_words_arr[i]
            print(courier_company[i] + " has a negative sentiment.")
            print("Percentage: ",
                  (total_negative_words_arr[i] / (total_words_arr[i] - total_stop_words_arr[i]) * 100))
        else:
            neutral_sentiment[courier_company[i]] = total_neutral_words_arr[i]
            print(courier_company[i] + " has a neutral sentiment.")

    # print the company that has the best sentiment based on most positive word count
    # from the positive sentiment companies only.
    print(positive_sentiment)
    print(positive_sentper)
    print(negative_sentiment)
    print(neutral_sentiment)

    # ratio of positive and negative words for each company
    for i in range(len(courier_company)):
        findRatio(total_positive_words_arr[i], total_negative_words_arr[i])

    bestsentiment(positive_sentiment, positive_sentper)


def findRatio(a, b):
    c = math.gcd(a, b)
    numerator = int(a / c)
    deno = int(b / c)
    print(numerator, ":", deno)


def bestsentiment(positive_sentiment, positive_sentper):
    # best sentiment
    best_sentiment = max(positive_sentiment, key=positive_sentiment.get)
    best_sentiment_per = positive_sentper.get(best_sentiment)
    print(best_sentiment + " has the best sentiment according to number of positive words.")
    print(best_sentiment, "has the highest positive word percentage with", best_sentiment_per)
    if positive_sentper.get(best_sentiment) > 50:
        print("The sentiment analysis is accurate.")
    else:
        print("The sentiment analysis is less accurate.")
