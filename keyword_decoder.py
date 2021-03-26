# the keyword decoder needs a keyword to allow the code to decode the string.
# one is for decoding the message the other is to code a message.

alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = ".,?'! "

# Response
def vigenere_decoder(sentence, keyword):
    letter_point = 0
    new_keyword = ""
    for i in range(0,len(sentence)):
        if sentence[i] in punctuation:
            new_keyword += sentence[i]
        else:
            new_keyword += keyword[letter_point]
            letter_point = (letter_point+1) % len(keyword)
    translated_sent = ""
    for i in range(0,len(sentence)):
        if sentence[i] not in punctuation:
            index = alphabet.find(sentence[i]) - alphabet.find(new_keyword[i])
            translated_sent += alphabet[index % 26]
        else:
            translated_sent += sentence[i]
    return translated_sent

# Reply
def vigenere_coder(sentence, keyword):
    letter_point = 0
    new_keyword = ""
    for i in range(0,len(sentence)):
        if sentence[i] in punctuation:
            new_keyword += sentence[i]
        else:
            new_keyword += keyword[letter_point]
            letter_point = (letter_point+1) % len(keyword)
    translated_sent = ""
    for i in range(0,len(sentence)):
        if sentence[i] not in punctuation:
            index = alphabet.find(sentence[i]) + alphabet.find(new_keyword[i])
            translated_sent += alphabet[index % 26]
        else:
            translated_sent += sentence[i]
    return translated_sent

coded_mess = "dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!"
key_mess = "friends"

message_for_v = "thanks for teaching me all these cool ciphers! you really are the best!"
keyword = "besties"

print(vigenere_decoder(coded_mess, key_mess))
# you were able to decode this? nice work! you are becoming quite the expert at crytography!
print(vigenere_coder(message_for_v, keyword), "\nkeyword: " + keyword)
# ulsgsw xpv lxigzjry fm edm xzxai upsd vqtzfvk! rwy jfedeg ejf xzx jiku!
# keyword: besties