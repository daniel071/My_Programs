from tkinter import *


def clear():
    global binaryMessage
    global decimalMessage
    global hexadecimalMessage

    binaryMessage.delete('1.0', "end-1c")
    decimalMessage.delete('1.0', "end-1c")
    hexadecimalMessage.delete('1.0', "end-1c")


def base_to_dec(n, base):
    try:
        n1, n2 = n.split(".")
        n1 = int(n1, base)
        n2 = int(n2, base) / (base ** len(n2))
        x = n1 + n2
        return x
    except ValueError:
        x = int(n, base)
        return x


def dec_to_base(n, base):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % base))
        n //= base
    return digits[::-1]


def list_to_hexadecimal(list):
    hexadecimal_codes = {
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F",
    }

    formatted_list = []
    for row in list:
        formatted_list.append(hexadecimal_codes[row])

    final_number = "".join(formatted_list)
    return final_number


def write_to_boxes(binary, decimal, hexadecimal):
    global binaryMessage
    global decimalMessage
    global hexadecimalMessage

    binaryMessage.insert(1.0, binary)
    decimalMessage.insert(1.0, decimal)
    hexadecimalMessage.insert(1.0, hexadecimal)


def binary_pushed():
    # TODO: Fix binary conversion not working
    # TODO: Add hexadecimal conversions

    global binaryMessage
    global decimalMessage
    global hexadecimalMessage

    binary = binaryMessage.get("1.0", "end-1c")
    decimal = base_to_dec(binary, 2)
    hexadecimal = list_to_hexadecimal(dec_to_base(decimal, 16))

    clear()
    write_to_boxes(binary, decimal, hexadecimal)


def decimal_pushed():
    global binaryMessage
    global decimalMessage
    global hexadecimalMessage

    decimal = decimalMessage.get("1.0", "end-1c")
    print(decimal)
    binary = dec_to_base(decimal, 2)
    print(binary)
    hexadecimal = list_to_hexadecimal(dec_to_base(int(decimal), 16))
    clear()
    write_to_boxes(binary, decimal, hexadecimal)


def hexadecimal_pushed():
    global binaryMessage
    global decimalMessage
    global hexadecimalMessage

    hexadecimal = hexadecimalMessage.get("1.0", "end-1c")
    decimal = base_to_dec(hexadecimal, 10)
    print(decimal)
    binary = dec_to_base(decimal, 2)
    print(binary)

    clear()
    write_to_boxes(binary, decimal, hexadecimal)


root = Tk()
root.title("Number System Converter")
root.geometry('1280x720')

title = Label(text="Number System Converter", font=("Roboto", 20))
title.grid(row=0, column=1)


binaryLabel = Label(text="Binary", font=("Roboto", 18))
binaryLabel.grid(row=1, column=0)
binaryMessage = Text(root, width=40, height=10)
binaryMessage.grid(row=2, column=0)
binaryButton = Button(text="Convert!", font=("Roboto", 14), command=binary_pushed)
binaryButton.grid(row=3, column=0)

decimalLabel = Label(text="Decimal", font=("Roboto", 18))
decimalLabel.grid(row=1, column=1)
decimalMessage = Text(root, width=40, height=10)
decimalMessage.grid(row=2, column=1)
decimalButton = Button(text="Convert!", font=("Roboto", 14), command=decimal_pushed)
decimalButton.grid(row=3, column=1)

hexadecimalLabel = Label(text="Hexadecimal", font=("Roboto", 18))
hexadecimalLabel.grid(row=1, column=2)
hexadecimalMessage = Text(root, width=40, height=10)
hexadecimalMessage.grid(row=2, column=2)
hexadecimalButton = Button(text="Convert!", font=("Roboto", 14), command=hexadecimal_pushed)
hexadecimalButton.grid(row=3, column=2)

root.mainloop()

