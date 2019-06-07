import re

words_document = open("all_words.txt", "r")
all_raw_words = words_document.read()
words_document.close()
all_words = all_raw_words.split("\n")

highest_allowed_word = ""

allowed_letters = "OIZEhSgLB"
letters_to_numbers = {
    "o": "0",
    "i": "1",
    "z": "2",
    "e": "3",
    "h": "4",
    "s": "5",
    "g": "6",
    "l": "7",
    "b": "8",
}

for word in all_words:
    if len(word) > len(highest_allowed_word):
        if bool(re.match('^[oizehsglb]+$', word.lower())) is True:
            highest_allowed_word = word
            print("{word} has passed".format(word=word))
        else:
            print("{word} has failed".format(word=word))


translated_numbers = []
for letter in highest_allowed_word:
    translated_numbers.append(letters_to_numbers[letter.lower()])

translated_numbers.reverse()
translated_numbers = "".join(translated_numbers)

print("The longest letter you can put on a upside down 7-segment display is: {longest} \n"
      "The numbers to put in is: {numbers} \n"
      "The word has {length_of_word} characters"
      .format(longest=highest_allowed_word, numbers=translated_numbers, length_of_word=len(highest_allowed_word)))
