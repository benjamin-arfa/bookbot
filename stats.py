def get_book_text(book: str):
    with open(book) as f:
        file_contents = f.read()
    return len(file_contents.split())

def get_num_words(book: str):
    print("----------- Word Count ----------")
    print(f"Found {get_book_text(book)} total words")

def new_function(book:str):
    print("--------- Character Count -------")
    with open(book) as f:
        file_contents = f.read()
    file_contents = file_contents.lower()
    characters = list(file_contents)
    set_chars = {k for k in set(filter(str.isalnum,characters)) if k not in ("1","2","3","4","5","6","7","8","9","0")}
    char_dict = {k:len([_ for _ in characters if _ == k]) for k in set_chars}
    char_dict = dict(sorted(char_dict.items(),key=lambda x : x[1], reverse=True))
    for k,v in char_dict.items():
        print(f"{k}: {v}")
