lock_art = '''
            .-""-.
           / .--. \\
          / /    \ \\
          | |    | |
          | |.-""-.|
         ///`.::::.`\\
        ||| ::/  \:: ;
        ||; ::\__/:: ;
         \\\ '::::'  /
          `=':-..-'`
'''

print(f"Caesar Cipher \n{lock_art}")

stop_execution = False


def get_shifted_letter(letter="a", shift_amount="0", cipher_direction="encode"):

    unicode = ord(letter)
    if not unicode >= ord("a") and unicode <= ord("z"):
        return letter
    if (cipher_direction == "decode"):
        current_pos = (26 + unicode - ord("a") - shift_amount) % 26
    else:
        current_pos = (unicode - ord("a") + shift_amount) % 26

    return chr(ord("a") + current_pos)


def caesar(start_text, shift_amount, cipher_direction="encode"):
    end_text = ""
    for letter in start_text:
        end_text += get_shifted_letter(letter, shift_amount, cipher_direction)
    print(f"{cipher_direction.capitalize()}d string is: {end_text}")
    return end_text


while not stop_execution:
    direction = input(
        "Type 'encode' to encrypt, or type 'decode' to decrypt\n")
    message = input("Enter the message\n").lower()
    shift = int(input("Enter the shift number\n"))
    caesar(start_text=message, shift_amount=shift, cipher_direction=direction)
    continue_execution = input(
        "Do you want to continue, type Y to continue or type N to stop \n")
    if not continue_execution == "Y":
        stop_execution = True
        print("Goodbye!")
