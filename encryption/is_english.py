from nltk.corpus import brown


def check_english(string):
    string_list = string.split()
    string_length = len(string_list)
    string_english = 0

    for word in string_list:
        if word in brown.words():
            string_english = string_english + 1
            print("Word '{word}' is an english word".format(word=word))
        else:
            print("Word '{word}' is not an english word".format(word=word))

    english_percentage = (string_english / string_length) * 100
    return "You got {english} / {total}. That is {percent}%".format(english=string_english, total=string_length, percent=english_percentage)


print(check_english("This is something that is called infrastructure ashdoiu eh ofhsdoihfosihfosfjsfojen fodsjnfodj"))
