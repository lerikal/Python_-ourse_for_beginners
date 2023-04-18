def main():
    dictionary = get_dictionary()
    result_message_out = cipher_message_out(dictionary)
    result_message_in = cipher_message_in(dictionary)
    print(result_message_out)
    print(result_message_in)

def get_dictionary():
    alphabet = [str(i) for i in input()]
    meaning = [str(i) for i in input()]

    dictionary = {}
    index = 0
    for char in alphabet:
        dictionary[char] = meaning[index]
        index += 1
    return dictionary

def cipher_message_out(dictionary):
    message_out = [str(i) for i in input()]
    result = ''
    for char in message_out:
        result += dictionary.get(char)
    return result

def cipher_message_in(dictionary):
    message_in = [str(i) for i in input()]
    result = ''
    for char in message_in:
        for key, value in dictionary.items():
            if char == value:
                result += key
    return result

main()
