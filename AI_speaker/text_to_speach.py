from gtts import gTTS
from playsound import playsound

# 문장을 입력 or 입력받고 그 문장을 gTTS 를 이용하여 mp3로 저장후 재생
# text = 'Can I help you?'
file_name = 'sample.mp3'
# tts_en = gTTS(text=text, lang='en')
# tts_en.save(file_name)

# text = '다른 누구도 아닌, 자신을 등불 삼으라 - 석가모니'
# tts_ko = gTTS(text = text, lang='ko')
# tts_ko.save(file_name)
# playsound(file_name) # .mp3 파일 재생

#긴 문장을 가지고 와서 처리.
with open('sample.txt', 'r', encoding='utf8') as f:
    text = f.read()    
tts_ko = gTTS(text = text, lang='ko')
tts_ko.save(file_name)
playsound(file_name) # .mp3 파일 재생

