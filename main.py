import sqlite3
from extract import extract_number
import query_test
import recording
import convert_to_text
import re
query_test.create_database()
recording.recording()
convert_to_text.to_text("myrecording.wav")
#text = query_test.select('Texts','tex_info','tex_id','3')

#pattern = "[0-9]+"
#number = re.findall(pattern, text)
#number = query_test.tuple_to_string(number)
#print (extract_number(text))
