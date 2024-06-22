import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



    
def caesar_cipher(text,shift,direction):
    converted_text=""
    shift_places=0
    if direction=="encode" or direction=="decode":
        if direction=="decode":
            shift*=-1
        for letter in text:
            if letter.isalpha():
                shift_places = alphabet.index(letter)+shift
                if shift_places>=26:
                    wrap=shift_places%26
                    converted_text+=alphabet[wrap]
                elif shift_places<0:
                    wrap=26+shift_places
                    converted_text+=alphabet[wrap]
                else:
                    converted_text+=alphabet[shift_places]
            
            else:
                converted_text+=letter
    else:
        print("wrong entry! type either 'encode' or 'decode'")

    return converted_text

cont = True
while cont:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    text = input("Type your message:\n").lower()

    shift = int(input("Type the shift number:\n"))

    print(caesar_cipher(text,shift,direction))

    resp = input("Would you like to go again?").lower()
        
    if resp=="yes" or resp=="no":
        if resp =="no":
            print(("Goodbye"))
            cont=False
    else:
        print("wrong entry! Enter either 'yes' or 'no'")


