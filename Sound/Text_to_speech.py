# Import Module Library
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os

#Generate Sound File With Google Text To Speak
tts = gTTS(text='Miku, Miku, you can call me Miku', lang='en', slow=False)
tts.save("input.mp3")

# Customize Sound
sound = AudioSegment.from_file('input.mp3', format="mp3")

#os.remove("input.mp3")  # removefile

octaves = 0.25

new_sample_rate = int(sound.frame_rate * (3.0 ** octaves))

hipitch_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})

hipitch_sound = hipitch_sound.set_frame_rate(44100)

#playsound
play(hipitch_sound)
