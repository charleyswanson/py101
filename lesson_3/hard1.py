# 4
# def is_an_ip_number(input_number):
#     return 0 <= int(input_number) <= 255

def is_an_ip_number(str):
    if str.isdigit():
        number = int(str)
        return 0 <= number <= 255
    return False

def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    if len(dot_separated_words) == 4:
        while len(dot_separated_words) > 0:
            word = dot_separated_words.pop()
            if not is_an_ip_number(word):
                return False

        return True
    
    return False

print(is_dot_separated_ip_address("2.3.100.15"))

