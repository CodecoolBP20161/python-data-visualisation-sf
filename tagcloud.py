from client import Client
from company_name import Company
from project import Project
from headquarter import Headquarter
from manager import Manager
from PIL import Image, ImageDraw, ImageFont, ImageColor
import random
import math
import os

class TagCloud():

    FONTS = {'aquawax': 'Aquawax Black Trial.ttf', 'arial': 'arial_narrow_7.ttf', 'DK': 'DK Cinnabar Brush.ttf',
             'keepcalm': 'KeepCalm-Medium.ttf', 'kenyan': 'kenyan coffee bd.ttf'}
    MAIN_PATH = os.path.dirname(os.path.abspath(__file__))
    def __init__(self, object_list, width=1000, height=800, background_color="#fff", font="DK Cinnabar Brush.ttf"):
        self.width = width
        self.height = height
        self.image = Image.new('RGBA', [width, height], background_color)
        self.draw = ImageDraw.Draw(self.image)
        self.words = []
        self.font = TagCloud.MAIN_PATH + "/fonts/" + font
        self.object_list = object_list
        self._check_window_occupation = False

    def drawing(self):
        self._word_list()
        for word in self.words:
            self.draw.text((word['position'][0], word['position'][1]), word['text'],
                           font=ImageFont.truetype(self.font, word['font_size']), fill=word['fill'])
        self.image.show()
        self.image.save('blabla.png')

    # Fill up words list with the necessary text properties
    def _word_list(self, font_size_calculator=5):

        for object in self.object_list:
            text = object.name

            try:
                color = object.mixer()
            except AttributeError:
                color = object.rgb_color

            if object.priority > 90:
                font_size = int(object.priority / font_size_calculator)
            elif object.priority > 85:
                font_size = int(object.priority / (font_size_calculator * 1.2))
            else:
                font_size = int(object.priority / (font_size_calculator * 2))



            width, height = self.draw.textsize(text, font=ImageFont.truetype(self.font, font_size))

            position = [self.width/2 - width, self.height/2 - height]
            t = random.randint(1, 100)
            spiral_coord = (0.25 * (math.cos(t) + t * math.sin(t)), 0.25 * (math.sin(t) - t * math.cos(t)))
            while not self._overlap(position, width, height):
                position = [self.width/2 - width + spiral_coord[0], self.height/2 - height + spiral_coord[1]]
                t += 0.5
                spiral_coord = (0.25 * (math.cos(t) + t * math.sin(t)), 0.25 * (math.sin(t) - t * math.cos(t)))
            self.words.append({'text': text, 'font_size': font_size, 'width': width, 'height': height,
                               'position': position, 'fill': color})

        # check if the window is much larger than the tagcloud
        if self._is_window_large():
            if font_size_calculator > 1:
                font_size_calculator -= 1
            else:
                return 0
            self.words = []
            self._word_list(font_size_calculator)
            if self._check_window_occupation:
                return 0
        self._check_window_occupation = True

    def _overlap(self, position, width, height):
        if len(self.words) > 0:
            for word in self.words:
                x_ref = word['position'][0]
                y_ref = word['position'][1]
                if not ((x_ref + word['width'] < position[0] or position[0] < x_ref - width)
                        or (y_ref + word['height'] < position[1] or position[1] < y_ref - height)):
                    return False
                if (position[0] + width > self.width or position[0] < 0) or (position[1] + height > self.height
                                                                             or position[1] < 0):
                    return False
            return True
        else:
            return True

    def _is_window_large(self):
        x_max, x_min, y_max, y_min = self._check_tag_borders()
        if x_max < self.width and x_min > 0 and y_max < self.height and y_min > 0:
            return True
        return False

    def _check_tag_borders(self):
        x_max, x_min, y_max, y_min = 0, self.width, 0, self.height
        for word in self.words:
            text_x_max = word['position'][0] + word['width']
            text_x_min = word['position'][0]
            text_y_min = word['position'][1]
            text_y_max = word['position'][1] + word['height']
            if text_x_max > x_max:
                x_max = text_x_max
            if text_y_max > y_max:
                y_max = text_y_max
            if text_x_min < x_min:
                x_min = text_x_min
            if text_y_min < y_min:
                y_min = text_y_min
        return x_max, x_min, y_max, y_min

inst = TagCloud(Headquarter.gen_list(), font='arial_narrow_7.ttf')
inst.drawing()