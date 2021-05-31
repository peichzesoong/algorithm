import cleanfile


# to store the stop words into the trie
def store_stop_trie(stop_trie):
    cleanfile.clean_file("stopwords")
    stop_clean = open("texts/stopwords_clean.txt", "r", encoding="utf8")
    cstop_clean = stop_clean.readlines()

    # to store the stop words into the trie
    for i in cstop_clean:
        keys = i.split()
    for key in keys:
        stop_trie.insert(key)

    stop_clean.close()


# to filter stop words
def filter_stop_words(file_name, stop_trie):
    file2 = open("texts/" + file_name + ".txt", "r", encoding="utf8")
    cfile2 = file2.readlines()
    string = []
    for line in cfile2:
        temp = ' '.join(i for i in line.split() if not stop_trie.search(i)) + " "
        string.append(temp)

    file2 = open("texts/" + file_name + ".txt", "w", encoding="utf8")
    file2.writelines(string)
    file2.close()
