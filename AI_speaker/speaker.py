#간단한 인공지능 스피커 상황을 고려
#내가 말함 -> 스피커에서 인식 -> 인식한 상황에 맞는 답변 대답
import time, os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

# 음성 인식 부분(듣기)/STT
def listen(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language='ko')
        print('[나] ' +  text)
        answer(text) # 답변
    except sr.UnknownValueError:
        print('인식 실패..') #인식 실패
    except sr.RequestError as e:
        print('요청 실패 : {0}'.format(e)) # API key error
    

# 대답하기
def answer(input_text):
    global endFlag
    answer_text = ''
    if '안녕' in input_text:
        answer_text = '안녕하세요, 저도 반갑습니다.'
    elif '날씨' in input_text:
        answer_text = '오늘은 조금 쌀쌀한 날씨가 예상됩니다.'
    elif '환율' in input_text:
        answer_text = '현재 원 달러 환율은 1480원 입니다.'
    elif '고마워' in input_text:
        answer_text = '별 말씀을요.'
    elif '종료' in input_text:
        answer_text = '다음에 또 만나요.'
        stop_listening(wait_for_stop=False)
        speak(answer_text)
        endFlag = True
        return
    else:
        answer_text = '다시 한 번 말씀해 주시겠어요?'
    speak(answer_text)

#읽어주기/TTS
def speak(text):
    print('[인공지능] ' + text)  
    file_name = 'voice.mp3'
    tts = gTTS(text=text, lang='ko')
    tts.save(file_name)
    playsound(file_name)
    #voice file delete
    if os.path.exists(file_name):
        os.remove(file_name)


r = sr.Recognizer()
m = sr.Microphone()

endFlag = False

speak('무엇을 도와드릴까요?')
stop_listening = r.listen_in_background(m, callback=listen)
#stop_listening(wait_for_stop=False) # 더 이상 듣지 않는다.

while not endFlag:
    time.sleep(0.1)
