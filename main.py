def wordCount(texts):
    words = texts.split(" ")
    count = len(words)
    return count

def getText (filePath):
    with open(filePath) as f:
        return f.read()

def charCount(text):
    charCount = {}
    textLower = text.lower()
    for char in textLower:
        if char in charCount.keys():
            charCount[char] += 1
        else:
            charCount[char] = 1
    return charCount

def main():
    path = "books/frankenstein.txt"
    texts = getText(path)
    charCounts = charCount(texts)
    print(f"{wordCount(texts)} words found in the book \n \n")
    for char in charCounts:
        print(f"The {char} character was found {charCounts[char]} times")

    



main()