import logging
import os
from datetime import datetime

# Create the file
logging.basicConfig(filename='logtest.log', level=logging.DEBUG)


def getmessage(message):
    return " {date}; {username}; {message}".format(date=datetime.today().strftime('%Y-%m-%d'),
                                                   username=os.getlogin(), message=message)


def reverse(num):
    logging.info(getmessage("reverse function called; {num} passed in".format(num=num)))

    if type(num) == float or type(num) == int:
        num = float(num)

        if num >= 0:
            output = num - (num * 2)
        elif num <= 0:
            output = num + (num * -2)

        logging.info(getmessage("reverse function called; {num} passed in; {output} returned"
                                .format(num=num, output=output)))
        return output
    else:
        logging.warning(getmessage("Handled exception raised 'TypeError: num must be int or float!'"))
        raise TypeError("num must be int or float!")


# reverse("string")



# logging.debug(getmessage("Everything is fine!"))
# logging.info(getmessage("User logged in"))
# logging.warning(getmessage("Please be cautious"))
# logging.critical(getmessage("Things are getting bad!"))
# logging.error(getmessage("Whole system shutdown"))