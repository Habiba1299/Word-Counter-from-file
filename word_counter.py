import pathlib

path = 'input.txt'
file_path = pathlib.Path(path)


def count_word(item):
    s_word = item.lower()
    count = 0
    file = open('input.txt', 'r')
    while True:
        f_word = file.readline().strip().lower()
        if not f_word:
            break
        if s_word == f_word:
            count = count + 1
            print()
    print(item, "->", count)
    file.close()


if file_path.is_file():
    search_words = ["Python", "C", "OOP", "Hello", "Java"]
    for word in search_words:
        count_word(word)
else:
    print("file doesn't exist")
