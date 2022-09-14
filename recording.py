import pyaudio
import wave
import sys
from query_test import insert


#converting voice into binary format for save it 
def convert_voice(filename):
    with open(filename, 'rb') as f:
        data = f.read()
    return data

def recording():
    #internalize the audio
    audio = pyaudio.PyAudio()

    stream = audio.open(format=pyaudio.paInt16, 
                        channels= 1 , rate= 44100, 
                        input = True , 
                        frames_per_buffer= 1024)
    frames = []
    print("recording...")
    try:
        while True:
            data = stream.read(1024)
            frames.append( data )
    except KeyboardInterrupt:
        pass
    #stop recording
    print("done recording")
    stream.stop_stream()
    stream.close()
    audio.terminate()
    #save the recording in file
    wf = wave.open('myrecording.wav', 'wb')
    # set the channels
    wf.setnchannels(1)
    # set the sample format
    wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    # set the sample rate
    wf.setframerate(44100)
    # write the frames as bytes
    wf.writeframes(b"".join(frames))
    # close the file
    wf.close()
    #save the recording into the database
    insert("Voices", 'voi_info', convert_voice('myrecording.wav'))




