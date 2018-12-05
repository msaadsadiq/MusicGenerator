from pydub import AudioSegment
import os

for filename in os.listdir(os.getcwd()):
	newAudio  = AudioSegment.from_mp3(filename)
	
	for i in range(1, (math.floor(len(newAudio)/1000)):
		j = (i-1) *1000 
		newAudio = newAudio[ j : (j + 1000)]
		newAudio.export(filename+'i', format="mp3")



