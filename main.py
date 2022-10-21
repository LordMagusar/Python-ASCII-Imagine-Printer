from PIL import Image
import requests
from io import BytesIO

response = requests.get(input("Give image url"))
img = Image.open(BytesIO(response.content))


with open("image.txt", "w") as f:
	for y in range(0, img.size[1], 1):
		for x in range(0, img.size[0], 1):			
			r = img.getpixel((x,y))[0] if isinstance(img.getpixel((x,y)),tuple) else img.getpixel((x,y))
			f.write((" " if r <= 51 else "." if r <= 102 else ":" if r <= 153 else "=" if r <= 204 else "#") + " ")
		f.write("\n")
