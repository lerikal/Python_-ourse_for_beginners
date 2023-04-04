words = [i.lower() for i in input().split()]
dictionary = {}

for word in words:
    dictionary[word] = words.count(word)

for i in dictionary:
    print(i, dictionary.get(i))
