from client import Client
from PIL import Image, ImageDraw, ImageFont
import random


class TagCloud():

    def __init__(self, width=600, height=600, background_color="#fff", font="arial_narrow_7.ttf"):
        self.width = width
        self.height = height
        self.image = Image.new('RGBA', [width, height], background_color)
        self.draw = ImageDraw.Draw(self.image)
        self.words = []
        self.font = font

    def drawing(self):
        for word in self.words:
            self.draw.text((word['position'][0], word['position'][1]), word['text'],
                           font=ImageFont.truetype(self.font, word['fontsize']), fill=(0,0,0))


    # Fill up words list with the necessary text properties
    def _word_list(self, object_list):
        for object in object_list:
            self.words.append({'text': object.name, 'fontsize': self._fontsize(object.priority),
                               'position': self._position()})

    # get fontsize based on the priority of data
    def _fontsize(self, weight):
        return int(weight / 5)+20

    # give the text a random position
    def _position(self):
        return [random.randint(0, self.width), random.randint(0, self.height)]


    # def _get_size(self, text, font_type):
    #     widt, height = self.draw.textsize(text, )


    # def test(self):
    #     clients = Client.gen_list()
    #     self._word_list(clients)
    #     print(self.words)
    #     self.drawing()
    #     self.image.show()


# task = TagCloud()
# task.test()

