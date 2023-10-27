def main():
    file_path = "books/frankenstein.txt"
    file_contents = read_file(file_path)
    word_count = count_words(file_contents)
    letter_count = get_letter_count(file_contents)
    letter_list = convert_dict_to_list(letter_count)
    print_report(file_path, word_count, letter_list)

def read_file(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    return len(text.split())

def get_letter_count(text):
    charDict = {}
    for char in text:
        lower_char = char.lower()
        if lower_char in charDict:
            charDict[lower_char] += 1
        else:
            charDict[lower_char] = 1
    return charDict

def convert_dict_to_list(dict):
    list = []
    for letter in dict:
        if letter.isalpha():
            letter_tuple = (letter, dict[letter])
            list.append(letter_tuple)
    list.sort(key=lambda x: -x[1])
    return list

def print_report(file, word_count, letter_list):
    print(f"--- Begin report of {file} ---")
    print(f"{word_count} words found in the document \n")
    for letter in letter_list:
        print(f"The {letter[0]} character was found {letter[1]} times")
    print("--- End of report ---")


main()