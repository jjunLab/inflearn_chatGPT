from bardapi import Bard

token = '토큰입력'
bard = Bard(token=token,timeout=30)
result = bard.get_answer("LG 트윈스에 대해 설명해줘")
print(result)