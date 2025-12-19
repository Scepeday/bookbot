def get_num_words():
    with open("books/frankenstein.txt") as file:
        file_content = file.read()
        c = file_content.split()
        print (f"Found {len(c)} total words")

def count_characters():
    dic = {}
    with open("books/frankenstein.txt") as file:
        file_content = file.read()
        lower = file_content.lower()
        for words in lower:
            if words in dic:
                dic[words] += 1
            else:
                dic[words] = 1

        print (dic)




