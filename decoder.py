from inputhelper import input_int, input_str
from filehelper import write_to_file, read_from_file


string = read_from_file("./text/encoded_text_large.txt")

print("Please enter offset")
offset = input_int()

i = 0 
decoded_string = ""
while i < len(string):
    char = string[i]
    unicode_of_char = ord(char)
    new_unicode_of_char = unicode_of_char - offset
    if new_unicode_of_char < 0:
        new_unicode_of_char += 128
    new_char = chr(new_unicode_of_char)
    decoded_string = decoded_string + new_char
    i = i + 1

write_to_file("./decoded/large_text_decoded.txt", decoded_string)

