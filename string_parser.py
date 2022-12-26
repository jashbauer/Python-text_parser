
def text_parser():

    # USER INPUT TEXT
    text = input("Please, enter a text of your choice: ").lower()

    text_as_list = text.split(" ")

    data_to_show = {}

    # 1) LETTER COUNT DATA

    # Handle commas, points and white spaces
    while True:
        letters_as_list = []
        letters = input("Please, enter the 3 letters of your interest: ").lower()
        chars_to_remove = [" ", ",", "."]
        for char in chars_to_remove:
            if char in letters:
                letters = letters.replace(char, "")

        #print(letters)

        for char in letters:
            letters_as_list.append(char)

        print(letters_as_list)

        if len(letters_as_list) == 3:
            break
        else:
            print("\nYou've entered a lower or higher number of letters.\n")

    #print(letters_as_list)

    letter_count = {}
    for letter in letters_as_list:
        letter_count[letter] = text.count(letter)

    #print(letter_count)

    data_to_show["letter_count"] = letter_count

    # 2) TOTAL WORDS DATA
    total_words = len(text_as_list)
    #print(total_words)

    data_to_show["total_words"] = total_words

    # 3) FIRST AND LAST LETTER
    first_last = {
        "first": text[0],
        "last": text.strip("!.,")[-1]
    }

    data_to_show["first_and_last"] = first_last

    # 4) INVERTED WORDS TEXT
    inverted = text[::-1]
    inverted_words_list = text_as_list
    inverted_words_list.reverse()
    inverted_words = " ".join(inverted_words_list)

    data_to_show["inverted_text"] = {"inverted_letters": inverted, "inverted_words": inverted_words}

    # 5) IS PYTHON IN THE TEXT?
    python_in = "python" in text

    data_to_show["python_in_text"] = python_in

    # FINAL RESULT
    print("\nParsed Data is as follows:")
    for key in data_to_show:
        print(f"{key}: {data_to_show[key]}")

    return data_to_show


data = text_parser()

print(data)