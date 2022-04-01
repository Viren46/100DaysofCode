import art

print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
run_program = 'yes'

def caeser(direction,text,shift):
    if direction == 'encode':
        for letter in range(len(text)):
            if text[letter] in alphabet:
                if (alphabet.index(text[letter])+shift) <= 25:
                    word_list[letter] = alphabet[alphabet.index(text[letter])+shift]
                else:
                    word_list[letter] = alphabet[alphabet.index(text[letter])-26+shift]
            else:
                word_list[letter] = text[letter]
        text = ''.join(word_list)
        print(text)
    elif direction == 'decode':
        for letter in range(len(text)):
            if text[letter] in alphabet:
                word_list[letter] = alphabet[alphabet.index(text[letter])-shift]
            else:
                word_list[letter] = text[letter]
        text = ''.join(word_list)
        print(text)
    
while run_program == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 26:
        shift = shift%26
    word_list = list(text)
    caeser(direction,text,shift)
    run_program = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
