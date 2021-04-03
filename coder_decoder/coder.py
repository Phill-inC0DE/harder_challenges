def coder(sentence):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    punctuation = ".,?'! "
    new_sentence = ""
    for letter in sentence:
        if not letter in punctuation:
            letter_index = alphabet.find(letter)
            new_sentence += alphabet[(letter_index - 10) % 26]
        else:
            new_sentence += letter
    print(new_sentence)

coder("Hello! my good friend, I hope you're well. I love this little game we're playing!")

#part2

def coder2(message, offset):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    punctuation = ".,?'! "
    new_message = ""
    for letter in message:
        if not letter in punctuation:
            letter_index = alphabet.find(letter)
            new_message += alphabet[(letter_index + int(offset)) % 26]
        else:
            new_message += letter
    print(new_message)

coder2("bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!", 14)