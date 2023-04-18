def main():
    n_words = int(input())
    correct_words = input_correct_words(n_words)
    n_checks = int(input())
    mistakes = word_check(n_checks, correct_words)

    for mistake in mistakes:
        print(mistake)

def input_correct_words(n_words):
    list_of_words = set()
    while n_words > 0:
        word = str(input().lower())
        list_of_words.add(word)
        n_words -= 1
    return list_of_words

def word_check(n_checks, correct_words):
    mistakes = set()
    while n_checks > 0:
        phrase = [str(i) for i in input().lower().split()]
        for word in phrase:
            if word not in correct_words:
                mistakes.add(word)
        n_checks -= 1
    return mistakes

main()