import re

words_document = open("all_words.txt", "r")
all_raw_words = words_document.read()
words_document.close()
all_words = all_raw_words.split("\n")
allowed_list = []
amount_passed = 0
amount_failed = 0

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


def convert_to_calculator_number(word_provided):
    translated_numbers = []
    for letter in word_provided:
        translated_numbers.append(letters_to_numbers[letter.lower()])

    translated_numbers.reverse()
    translated_numbers = "".join(translated_numbers)
    return translated_numbers


print("Initial Check:\n---------------------------\n")


for word in all_words:
    if bool(re.match('^[oizehsglb]+$', word.lower())) is True:
        if len(word) > len(highest_allowed_word):
            highest_allowed_word = word
        allowed_list.append(word)
        print("{word} has passed".format(word=word))
        amount_passed = amount_passed + 1
    else:
        print("{word} has failed".format(word=word))
        amount_failed = amount_failed + 1

print("\n\nResults:\n---------------------------\n")

allowed_list.sort(key=len)
for row in allowed_list:
    print("Ordered in longest allowed is: {allowed_words} at {length_of_this_word} characters long. "
          "Shown on a 7-segment-display as {displayed_number}".format(allowed_words=row, length_of_this_word=len(row),
                                                                      displayed_number=convert_to_calculator_number(row)
                                                                      ))


print("\n{amount_of_passed} words have passed, {amount_of_failed} has failed, "
      "with {percentage}% of the words in this list passing.".format(amount_of_passed=amount_passed,
                                                                     amount_of_failed=amount_failed,
                                                                     percentage=(amount_passed/len(all_words)*100)))


print("\nThe longest letter you can put on a upside down 7-segment display is: {longest} \n"
      "The numbers to put in is: {numbers} \n"
      "The word has {length_of_word} characters"
      .format(longest=highest_allowed_word, numbers=convert_to_calculator_number(highest_allowed_word),
              length_of_word=len(highest_allowed_word)))
