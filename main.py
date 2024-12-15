def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return(file_contents)

def countWords():
    wordCount = len(main().split())
    return(wordCount)

def countCharacters():
    lowered_string = main().lower()
    chars = list(lowered_string)
    letters = {}
    for letter in chars:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return(letters)

def sort_on(dict):
    return dict["count"]

characters = []
letters = countCharacters()
for l in letters:
    if l.isalpha():
        characters.append({"char": l, "count": letters[l]})

characters.sort(reverse=True, key=sort_on)

def bookData(words,chars):
    print("--Here's the report for frankenstein.txt--")
    print("The document has", words, "words.")
    for i in chars:
        print(f"The letter '{i['char']}' appears {i['count']} times.")
    print("-------------End of the report-------------")

bookData(countWords(),characters)