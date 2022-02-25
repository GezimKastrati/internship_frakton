class Caesar:
    def __init__(self, text, shift):
        self.text = text
        self.shift = shift

    def encrypt_caesar(self):
        encrypted_text = ""

        for letter in self.text:
            if letter.isupper():
                letter_unicode = ord(letter)
                letter_index = ord(letter) - ord("A")

                # perform the shift
                new_index = (letter_index + self.shift) % 26

                # convert to new character
                new_unicode = new_index + ord("A")
                new_character = chr(new_unicode)

                # append to encrypted string
                encrypted_text = encrypted_text + new_character
            else:
                encrypted_text += letter

        return encrypted_text


input_text = "WKH HDJOH LV LQ SODB; PHHW DW MRH’V"
# in this case we want to decrypt this message and that's why we shift by -3
# if we want to encrypt a text we can shift by 3 or 4 etc

output_text = Caesar(input_text, -3).encrypt_caesar()
print("OUTPUT TEXT:")
print(output_text)
