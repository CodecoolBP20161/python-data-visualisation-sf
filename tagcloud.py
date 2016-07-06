from client import Client
from company_name import Company
from project import Project
from PIL import Image, ImageDraw, ImageFont, ImageColor
import random
import math


class TagCloud():

    def __init__(self, object_list, width=500, height=500, background_color="#fff", font="Hugs & Kisses xoxo Demo.ttf"):
        self.width = width
        self.height = height
        self.image = Image.new('RGBA', [width, height], background_color)
        self.draw = ImageDraw.Draw(self.image)
        self.words = []
        self.font = font
        self.object_list = object_list

    def drawing(self):
        self._word_list()
        for word in self.words:
            self.draw.text((word['position'][0], word['position'][1]), word['text'],
                           font=ImageFont.truetype(self.font, word['font_size']), fill=word['fill'])
        self.image.show()

    # Fill up words list with the necessary text properties
    def _word_list(self):
        for object in self.object_list:
            text = object.name
            color = object.rgb_color
            font_size = int(object.priority / 3)+10
            width, height = self.draw.textsize(text, font=ImageFont.truetype(self.font, font_size))

            position = [self.width/2, self.height/2]
            t = 0.25
            spiral_coord = (0.25 * (math.cos(t) + t * math.sin(t)), 0.25 * (math.sin(t) - t * math.cos(t)))
            while not self._overlap(position, width, height):
                position = [self.width/2 + spiral_coord[0], self.height/2 + spiral_coord[1]]
                t += 0.25
                spiral_coord = (0.25 * (math.cos(t) + t * math.sin(t)), 0.25 * (math.sin(t) - t * math.cos(t)))

            self.words.append({'text': text, 'font_size': font_size, 'width': width, 'height': height,
                               'position': position, 'fill': color})

    def _overlap(self, position, width, height):
        if len(self.words) > 0:
            for word in self.words:
                x_ref = word['position'][0]
                y_ref = word['position'][1]
                if not ((x_ref + word['width'] < position[0] or position[0] < x_ref - width)
                        or (y_ref + word['height'] < position[1] or position[1] < y_ref - height)):
                    return False
                if (position[0] + width > self.width or position[0] < 0) or (position[1] + height > self.height or position[1] < 0):
                    return False
            return True
        else:
            return True
