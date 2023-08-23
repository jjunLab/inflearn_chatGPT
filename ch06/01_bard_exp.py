from bardapi import Bard

token = 'Bard token'
bard = Bard(token=token,timeout=30)
result = bard.get_answer("LG 트윈스에 대해 설명해줘")
print(result)