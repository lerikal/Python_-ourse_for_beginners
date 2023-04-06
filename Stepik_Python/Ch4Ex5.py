def main():
    lines = get_lines()
    list_of_words = get_words(lines)
    res_word, res_count = find_the_longgest_word(list_of_words)
    update_file(res_word, res_count)
    return res_word, res_count

def get_lines():
    data = open("C:\\Users\\user\\Documents\\Python_projects\\Stepik_Python\\dataset_3363_3.txt", "r")
    data_set = data.readlines()

    lines = []
    for line in data_set:
        lines.append(line.replace('\n', ''))
    
    data.close()
    return lines

def get_words(lines):
    list_of_words = ''
    for line in lines:
        list_of_words += line
    
    list_of_words = list_of_words.lower().split()
    list_of_words.sort()
    return list_of_words

def find_the_longgest_word(list_of_words):
    our_word = ''
    count = 0
    for word in list_of_words:
        if count < list_of_words.count(word):
            our_word = word
            count = list_of_words.count(word)
    
    return our_word, count

def update_file(res_word, res_count):
    data = open("C:\\Users\\user\\Documents\\Python_projects\\Stepik_Python\\dataset_3363_3.txt", "w")
    data.write(res_word)
    data.write(' ')
    data.write(str(res_count))
    data.close()

print(main())