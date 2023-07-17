from pathlib import Path
from instagrapi import Client
from PIL import Image
USER_ID = "autoinstaupload"
USER_PASSWORD = "wnstjd1246!"

image = Image.open("instaimg.jpg")
image = image.convert("RGB")
new_image = image.resize((1080, 1080))
new_image.save("new_picture.jpg")
cl = Client()
cl.login(USER_ID, USER_PASSWORD)

phot_path = "new_picture.jpg"
phot_path  = Path(phot_path)
print(phot_path)
cl.photo_upload(phot_path , "hello this is a test from instagrapi")