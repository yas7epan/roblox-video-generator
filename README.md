# Генератор видео по Роблоксу
Самостоятельно озвучивает и делает видео на указанную тему. Использует Fandom для темы роликов. К сожалению оно не доработано до идеала пока что.

# Пример
https://files.catbox.moe/v80eep.mp4

# Установка

cd Расположение Папки с файлами исходного кода

pip install -r requirements.txt

python основной.py

# Настройки

Чтобы поменять тему для ролика нужно поменять следующие строчки:

fandom.set_wiki("Название Fandom, брать из URL, например в https://robloxcreepypasta.fandom.com/ru/wiki/G0Z нужно написать только robloxcreepypasta")

rasskaz = fandom.page("Название страницы Fandom")

Вы можете поменять разрешение видео, поменяв фон в fon1.mp4 (Обычно стоит 9:16)
И ещё чтобы поменять язык на английский измените следующие строчки:

fandom.set_lang("ru") на fandom.set_lang("en")

gTTS(rasskaz.plain_text, lang='ru').save('диктор.wav') на gTTS(rasskaz.plain_text).save('диктор.wav')

# Возможно я буду обновлять этот Гитхаб
Я не очень программист не кидайтесь помидорами
