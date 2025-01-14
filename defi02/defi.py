# defi.py
def upperFirstLetter(phrase):
    result = ""
    words = phrase.split(" ")
    for word in words:
        result += word.capitalize() + " "
    result = result[:-1]
    return result

def optimizedFirstLetter(phrase):
    return " ".join([word.capitalize() for word in phrase.split(" ")])