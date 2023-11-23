import caesar_ciper_art as art


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


print(art.logo)


def cipher(start_text, shift_amount, direct):
    end_text = ""
    if shift_amount > 26:
        shift_amount = shift_amount % 26
    else:
        shift_amount = shift_amount
    if direct == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here's the {direct}d result: {end_text}")


repeat = True
while repeat:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    cipher(start_text=text, shift_amount=shift, direct=direction)
    rpt = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if rpt == "yes":
        repeat = True
    else:
        repeat = False
        print("Good Bye")
