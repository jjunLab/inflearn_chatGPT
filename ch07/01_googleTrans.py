from googletrans import Translator

def google_trans(messages):
    google = Translator()
    result = google.translate(messages, dest="ko")

    return result.text


text ="GPT-4 is more creative and collaborative than ever before. It can generate, edit, and iterate with users on creative and technical writing tasks, such as composing songs, writing screenplays, or learning a user??s writing style."

result = google_trans(text)
print(result)