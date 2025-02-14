# find 3 letter words starting with b inside file
def find_words(filename):
    """
    Prints 3 letter words starting with b from a file
    :param input:
    :return:
    """
    with open(filename) as f:
        for line in f:
            words = line.split()
            for word in words:
                if len(word) == 3 and word [0] in "bB":
                    print(word)

find_words("input.txt")
