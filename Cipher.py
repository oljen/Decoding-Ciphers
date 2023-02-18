encoded_message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
offset = 10

decoded_message = ""
for letter in encoded_message:
    if letter.isalpha():
        # Shift the letter by the offset, wrapping around if necessary
        new_letter_code = (ord(letter) - ord('a') + offset) % 26 + ord('a')
        decoded_message += chr(new_letter_code)
    else:
        # Add non-alphabetic characters as-is
        decoded_message += letter

print(decoded_message)



def caesar_encode(message, offset):
    encoded_message = ""
    for letter in message:
        if letter.isalpha():
            new_letter_code = (ord(letter) - ord('a') + offset) % 26 + ord('a')
            encoded_message += chr(new_letter_code)
        else:
            encoded_message += letter
    return encoded_message


def caesar_decode(message, offset):
    decoded_message = ""
    for letter in message:
        if letter.isalpha():
            new_letter_code = (ord(letter) - ord('a') - offset) % 26 + ord('a')
            decoded_message += chr(new_letter_code)
        else:
            decoded_message += letter
    return decoded_message


def vigenere_decoder(coded_message, keyword):
    # Repeat the keyword to generate the keyword phrase
    keyword_phrase = (keyword * (len(coded_message) // len(keyword) + 1))[:len(coded_message)]
    
    decoded_message = ""
    for i in range(len(coded_message)):
        # Convert the letters to numbers
        coded_num = ord(coded_message[i]) - ord('a')
        keyword_num = ord(keyword_phrase[i]) - ord('a')
        
        # Compute the shift
        shift = keyword_num
        
        # Shift the letter and add it to the decoded message
        decoded_num = (coded_num - shift) % 26
        decoded_char = chr(decoded_num + ord('a'))
        decoded_message += decoded_char
    
    return decoded_message
