from connection import *
from task import *
from PIL import ImageColor


class Client(Task):

    def __init__(self, *args):
        super().__init__(*args)

    # Generate a list with company instances, with the necessary attributes
    @classmethod
    def gen_list(cls):
        clients = []
        companies = mydb.execute(
            "SELECT count(name), company_name from project GROUP BY company_name")
        calculator = 100 / max([i[0] for i in companies])
        # Filling the colom_mix list and making the instances
        for company in companies:
            project_number = company[0]
            colors = mydb.execute(
                "SELECT main_color from project WHERE company_name = '" + company[1] + "'")
            color_mix = []
            for color in colors:
                color_mix.append(color[0])
            clients.append(
                cls(company[1], project_number * calculator, color_mix))
        return clients

    # Accepts a list of hex colors and returns a mix of it's colors in rgb
    # value.
    def mixer(self):
        x = [ImageColor.getrgb(i)
             for i in self.color_mix if i]
        length = len(self.color_mix)
        r = sum([i[0] for i in x]) // length
        g = sum([i[1] for i in x]) // length
        b = sum([i[2] for i in x]) // length
        return (r, g, b)
