import speech_recognition as sr
import query_test


def to_text(file_name):
    # initialize the recognizer
    r = sr.Recognizer()
    # open the file
    with sr.AudioFile(file_name) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text = r.recognize_google(audio_data, language= 'ar-LB')
        # insert into the database
        query_test.insert('Texts','tex_info',text)
        print(text)
        # connect the text with the voice in the database by the forgien key
        voice_last_id = query_test.get_last_id("Voices","voi_id")
        text_last_id = query_test.get_last_id("Texts","tex_id")
        query_test.update("Texts","Voi_id",voice_last_id,"tex_id",text_last_id)
      