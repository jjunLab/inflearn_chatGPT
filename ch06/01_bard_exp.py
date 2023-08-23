from bardapi import Bard

token = 'aAjDVNJSlxf0KxCR02--Xa05nCUjHR_9f-1h5agNoaOOIFB14SrC8ckvQIihE8d9sPyZBg.'
bard = Bard(token=token,timeout=30)
result = bard.get_answer("LG 트윈스에 대해 설명해줘")
print(result)