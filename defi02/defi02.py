def upperFirstLetter(phrase):
    result = ""
    words = phrase.split(" ")
    for word in words:
        result += word.capitalize() + " "
    return result

def optimizedFirstLetter(phrase):
    return " ".join([word.capitalize() for word in phrase.split(" ")])


phrase = "Bonjour tout le monde"
print(phrase)
print(upperFirstLetter(phrase))

phrase2 = "Ceci est un test"
print(phrase2)
print(optimizedFirstLetter(phrase2))
