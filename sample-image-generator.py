from connection import *
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


img = Image.new("RGB", (512, 512), "red")
draw = ImageDraw.Draw(img)
#font = ImageFont.truetype(<font-file>, <font-size>)
#font = ImageFont.truetype("sans-serif.ttf", 16)
text_options = {
    'fill': (255, 255, 255)
}
text_content_list = [i[0] for i in rows]
text_content = text_content_list[0]
text_size = draw.textsize(text_content)
# draw.text((x, y),text_content,(r,g,b))
draw.text((50, 50), text_content, **text_options)
draw.text((0, text_size[1]), text_content, **text_options)
draw.text((text_size[0], 0), text_content, **text_options)
draw.text(text_size, text_content, **text_options)
img.save('sample-out.png')
img.show()
