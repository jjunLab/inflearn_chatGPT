import deepl

# auth_key = "API Key"  # Replace with your key
auth_key = "78f46891-6198-d86f-f4da-8ec4dc744663:fx"  # Replace with your key
translator = deepl.Translator(auth_key)

text ="GPT-4 is more creative and collaborative than ever before. It can generate, edit, and iterate with users on creative and technical writing tasks, such as composing songs, writing screenplays, or learning a user??s writing style."

result = translator.translate_text(text, target_lang="KO")
print(result.text)