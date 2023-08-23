from pathlib import Path
from instagrapi import Client
from PIL import Image

# USER_ID = "instagram ID"
# USER_PASSWORD = "Password!"
USER_ID = "autoinstaupload"
USER_PASSWORD = "wnstjd1246!"

# 이미지 사이즈 변환
image = Image.open("instaimg.jpg")
image = image.convert("RGB")
new_image = image.resize((1080, 1080))
new_image.save("new_picture.jpg")

#인스타그램 로그인
cl = Client()
cl.login(USER_ID, USER_PASSWORD)

#사진 가져오기
phot_path = "new_picture.jpg"
phot_path  = Path(phot_path)
print(phot_path)

#업로드하기
cl.photo_upload(phot_path , "hello this is a test from instagrapi")