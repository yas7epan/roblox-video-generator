from moviepy.editor import *
import fandom
from gtts import gTTS

# Настройка Fandom
fandom.set_lang("ru") # Язык вики
fandom.set_wiki("robloxcreepypasta") # Вики
rasskaz = fandom.page("G0Z") # Страница вики

# Настройка говорилки
print("Диктор читает, подожди...")
gTTS(rasskaz.plain_text, lang='ru').save('диктор.wav')
print("Диктор завершил чтение!")
print("Видео рендерится...")
videoclip = VideoFileClip("fon1.mp4")
audioclip = AudioFileClip("диктор.wav")
txt_clip = ( TextClip(rasskaz.title,fontsize=120,color='red')
             .set_position('center')
             .set_duration(3) )
result = CompositeVideoClip([videoclip.set_audio(audioclip), txt_clip])
result.write_videofile("результат.mp4",fps=25)
input("Готово!")