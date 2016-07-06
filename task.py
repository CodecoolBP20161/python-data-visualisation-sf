from PIL import ImageColor

class Task(object):

    def __init__(self,name,priority,color_mix):
        self.name = name
        self.priority = priority
        self.color_mix = color_mix

    @property
    def rgb_color(self):
        if self.color_mix is None:
            return (0, 0, 0)
        else:
            return ImageColor.getrgb(self.color_mix)
