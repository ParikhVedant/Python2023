from inputhelper import input_int, input_str
from filehelper import write_to_file, read_from_file


string = read_from_file("plain_text_large.txt")

print("Please enter offset")
offset = input_int()

i = 0 
encoded_string = ""
while i < len(string):
    char = string[i]
    unicode_of_char = ord(char)
    new_unicode_of_char = unicode_of_char + offset
    new_char = chr(new_unicode_of_char)
    encoded_string = encoded_string + new_char
    i = i + 1

write_to_file("encoded_text_large.txt", encoded_string)
