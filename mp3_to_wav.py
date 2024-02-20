from os import path 
from pydub import AudioSegment 
  
# assign files 
audio_string = "data/Chill-HoliznaCC0%20-%20Movement"
input_file = audio_string+".mp3"
output_file = audio_string+".wav"
  
# convert mp3 file to wav file 
sound = AudioSegment.from_mp3(input_file) 
sound.export(output_file, format="wav")