

# new_decoder which will cycle through every possible offset, 
# allowing you to decrypt the hidden message.

def de_coder(sentence):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    punctuation = ".,?'! "
    new_sentence = ""
    for i in range(0,26):
        for letter in sentence:
            if not letter in punctuation:
                letter_index = alphabet.find(letter)
                new_sentence += alphabet[(letter_index + i) % 26]
            else:
                new_sentence += letter
        print("Offset: ", i)
        print(new_sentence + "\n")
        new_sentence = ""

#de_coder("vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.")

# below is the original decoder with a for loop before printing the function.

def decoder(message, offset):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    punctuation = ".,?'! "
    new_message = ""
    for letter in message:
        if not letter in punctuation:
            letter_index = alphabet.find(letter)
            new_message += alphabet[(letter_index + int(offset)) % 26]
        else:
            new_message += letter
    return new_message

coded_message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."

for i in range(1,26):
    print("offset: ", i)
    print("\t " + decoder(coded_message, i) + "\n")