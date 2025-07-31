import win32com.client

speaker=win32com.client.Dispatch("SAPI.SpVoice")

L=["Ali", "Ehtesham", "Musa"]

for name in L:
    sentence=f"Hello {name} Sir "
    print(sentence)
    speaker.Speak(sentence)

