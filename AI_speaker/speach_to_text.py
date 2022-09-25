from cgitb import text
from email.mime import audio
from random import sample
import speech_recognition as sr

#구글의 API 를 이용하여 음성인식해서 재생

#마이크로부터 음성인식하기
r = sr.Recognizer()
with sr.Microphone() as source:
    print('듣고 있어요....')
    audio = r.listen(source) # 마이크로부터 음성 듣기. (Only Network)

try:
    # Google API 이용 -> 하루 50번 제한이라는 썰.
    text = r.recognize_google(audio_data=audio, language='ko-KR')
    print(text)
except sr.UnknownValueError:
    print('인식 실패..') #인식 실패
except sr.RequestError as e:
    print('요청 실패 : {0}'.format(e)) # API key error
    
#파일로부터 인식하기 (wav, aiff/aiff-c, flac) mp3 X
r = sr.Recognizer()
with sr.AudioFile('sample.wav') as source:
    audio = r.record(source=source)
