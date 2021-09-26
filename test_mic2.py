import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!", source)
    audio = r.listen(source, timeout=5)
    print(audio)

    text = r.recognize_google(audio, show_all=False, language="zh-CN")
    print(text)