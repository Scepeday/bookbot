from stats import get_num_words, count_characters, get_book_text, sort_on

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    get_num_words()
    print("--------- Character Count -------")
    dic = count_characters()
    sort_on(dic)
    print("============= END ===============")
    
main()
