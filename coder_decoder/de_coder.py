def de_coder(sentence):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    punctuation = ".,?'! "
    new_sentence = ""
    for letter in sentence:
        if not letter in punctuation:
            letter_index = alphabet.find(letter)
            new_sentence += alphabet[(letter_index + 10) % 26]
        else:
            new_sentence += letter
    print(new_sentence)

de_coder("xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!")

# part2

def decoder2(message, offset):
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

decoder2("jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.", 10)