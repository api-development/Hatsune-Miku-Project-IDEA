# Import Module Library
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os

#Generate Sound File With Google Text To Speak
tts = gTTS(text='Hello Hatsune miku!', lang='th', slow=False)
tts.save("input.mp3")

# Customize Sound
sound = AudioSegment.from_file('input.mp3', format="mp3")

# Remove Input File
os.remove("input.mp3")

octaves = 0.3

new_sample_rate = int(sound.frame_rate * (3.0 ** octaves))

hipitch_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})

hipitch_sound = hipitch_sound.set_frame_rate(44100)

#Play Sound
play(hipitch_sound)

#Save File
#hipitch_sound.export("output.mp3", format="mp3") #Optional
