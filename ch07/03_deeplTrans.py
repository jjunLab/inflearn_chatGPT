import deepl

auth_key = "API Key"  # Replace with your key
translator = deepl.Translator(auth_key)

text ="GPT-4 is more creative and collaborative than ever before. It can generate, edit, and iterate with users on creative and technical writing tasks, such as composing songs, writing screenplays, or learning a user??s writing style."

result = translator.translate_text(text, target_lang="KO")
print(result.text)