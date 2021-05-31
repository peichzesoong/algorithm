# to clean the article - remove digit, punctuations and lowercase all letters
def clean_file(file_name):
    file1 = open("texts/" + file_name + ".txt", "r", encoding="utf8")
    cfile1 = file1.readlines()

    file2 = open("texts/" + file_name + "_clean.txt", "a", encoding="utf8")

    for line in cfile1:
        string = ""
        for char in line:
            if char.isalpha() or char == " ":
                string = string + char
        file2.write(string.lower() + "\n")

    file1.close()
