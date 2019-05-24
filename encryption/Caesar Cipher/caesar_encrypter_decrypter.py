import string
from nltk.corpus import words
from nltk.corpus import brown


def reverse(num):
    num = float(num)

    if num >= 0:
        output = num - (num * 2)
    elif num <= 0:
        output = num + (num * -2)
    else:
        output = 0

    return output


def caesar(text, step):
    print("Text = '{text}', shift = '{shift}'\n".format(text=text, shift=step))
    alphabets = (string.ascii_lowercase, string.ascii_uppercase, string.digits)
    step = int(step)

    def shift(alphabet):
        return alphabet[step:] + alphabet[:step]

    shifted_alphabets = tuple(map(shift, alphabets))
    joined_alphabets = ''.join(alphabets)
    joined_shifted_alphabets = ''.join(shifted_alphabets)
    table = str.maketrans(joined_alphabets, joined_shifted_alphabets)
    return text.translate(table)


def check_english(string):
    string_list = string.split()
    string_length = len(string_list)
    string_english = 0

    if len(string_list) <= 3:
        print("IMPORTANT: Under than 3 words found; using slower but more accurate method.\n")
        for word in string_list:
            if word.lower() in brown.words():
                string_english = string_english + 1
                print("Word '{word}' is an english word".format(word=word))
            else:
                print("Word '{word}' is not an english word".format(word=word))
    else:
        print("IMPORTANT: More than 3 words found; using faster but less accurate method.\n")
        for word in string_list:
            if word.lower() in words.words():
                string_english = string_english + 1
                print("Word '{word}' is an english word".format(word=word))
            else:
                print("Word '{word}' is not an english word".format(word=word))

    english_percentage = (string_english / string_length) * 100
    print("The text '{text}' has \n{english} / {total} words found, the percentage is: {percent}%\n".
          format(text=string, english=string_english, total=string_length, percent=english_percentage))

    return string_english


def find_shift(message):
    results = []

    for i in range(0, 27):
        reverse_i = reverse(i)
        new_message = caesar(message, reverse_i)
        score = check_english(new_message)
        results.append([score, i])

    print("\n \n \nTotal Results:\n------------------\n[<English Words Found>, <Shift Number>]\n")
    for row in results:
        print(row)

    temp_list = max(results)
    print("The selected shift is: {list}".format(list=temp_list))
    return temp_list[1]


while True:
    print("Will you decrypt or encrypt (d / e)")
    userInput = input("".lower())

    if userInput == "e":
        input_message = input("Provide a message to cipher: ")
        input_shift = int(input("Provide the amount to shift: "))
        print("You encoded message is: {message}".format(message=caesar(input_message, input_shift)))
    elif userInput == "d":
        input_message = input("Input ciphered text: ")
        print("Do you know the key for the ciphered text? (y / n) ")
        userInput = input("").lower()
        if userInput == "y":
            input_shift = input("Input shift: ")
            new_input_shift = reverse(input_shift)
            print("Your message decrypted is: {message}".format(message=caesar(input_message, new_input_shift)))
        elif userInput == "n":
            print("Using method to brute force key: \n-----------------\n")
            found_shift = reverse(find_shift(input_message))
            print("Your message decrypted is: {message}".format(message=caesar(input_message, found_shift)))
