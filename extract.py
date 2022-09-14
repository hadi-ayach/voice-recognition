import re
import query_test

def extract_number(text):
    pattern = "[0-9]+"
    number = re.findall(pattern, text)
    number = query_test.tuple_to_string(number)
    return number