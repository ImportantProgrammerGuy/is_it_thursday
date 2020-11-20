import datetime

def is_thursday():
    now = datetime.datetime.now()
    weekday = now.weekday()
    if weekday == 3:   #Monday is 0, Thursday is 3 for weekday
        message = "It's Thursday!"
    else:
        message = "It's not Thursday."
    return message


if __name__ == "__main__":
    message = is_thursday()
    print(message)