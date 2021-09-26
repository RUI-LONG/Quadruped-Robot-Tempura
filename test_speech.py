import speech_recognition as sr

r = sr.Recognizer()
raw_audio = sr.AudioFile('raw_audio.wav')
with raw_audio as source:
    audio = r.record(source)

text = r.recognize_google(audio, show_all=False, language="zh-CN")
print(text)