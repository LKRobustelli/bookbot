def main():
    book = "books/frankenstein.txt"
    text = get_text(book)
    word_count = count_words(text)
    print (f"Word Count: {word_count}" )

def get_text(path):
    with open(path) as f:
        return (f.read())
    
def count_words(words):
    return (len(words.split()))
    
main()