def upperFirstLetter(phrase):
    result = ""
    words = phrase.split(" ")
    for word in words:
        result += word.capitalize() + " "
    return result
phrase = "Bonjour tout le monde"
print(phrase)
print(upperFirstLetter(phrase))
