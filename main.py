
def main():
    book = "books/frankenstein.txt"
    text = get_text(book)
    word_count = count_words(text)
    letter_total = count_letters(text)
    sorted_letters = sort_letters(letter_total)
    
    print(f"----- Beginning of Statistical Analysis of {book} -----")
    print('')
    print(f"Word Count: {word_count}")
    for pair in sorted_letters:
        print(f"{pair['char']} appears in the text {pair['num']} times!")
    

def get_text(path):
    with open(path) as f:
        return (f.read())
    
def count_words(words):
    return (len(words.split()))

def count_letters(word_list):
    letter_count= {}
    for word in word_list:
        letters = word.lower().split()
        for letter in letters:
            if letter not in letter_count:
                letter_count[letter] = 0
            letter_count[letter] += 1
    return letter_count

def sort_on(list):
    return list["num"]


def sort_letters(dict):
    dict_list = []
    for key in dict:
        if key.isalpha() == True:
            temp_dict = {"char": key, "num": dict[key]}
            dict_list.append(temp_dict)
    dict_list.sort(reverse = True, key = sort_on)
    return dict_list


main()