# Import Module Library
from gtts import gTTS
from pydub import AudioSegment
AudioSegment.converter = "C:\\ffmpeg\\bin\\ffmpeg.exe"
AudioSegment.ffmpeg = "C:\\ffmpeg\\bin\\ffmpeg.exe"
AudioSegment.ffprobe ="C:\\ffmpeg\\bin\\ffprobe.exe"
from pydub.playback import play
import playsound

#Generate Sound File With Google Text To Speak
tts = gTTS(text='Test Hatsune Miku', lang='en', slow=True)
tts.save("input.mp3")

# Customize Sound
sound = AudioSegment.from_file('input.mp3', format="mp3")

octaves = 0.25

new_sample_rate = int(sound.frame_rate * (2.0 ** octaves))

hipitch_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})

hipitch_sound = hipitch_sound.set_frame_rate(44100)

play(hipitch_sound)

# Output Sound Customized
hipitch_sound.export("output.mp3", format="mp3")

# Auto Play Sound
playsound.playsound("output.mp3", True)
