import datetime

def is_thursday():
    now = datetime.datetime.now()
    weekday = now.weekday()
    if weekday == 3:   #Monday is 0, Thursday is 3 for weekday
        message = "It's Tuhrsday!"
    else:
        message = "It's not Tuhrsday."
    return message


if __name__ == "__main__":
    message = is_thursday()
    print(message)