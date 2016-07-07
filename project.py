from task import *
from connection import *
import math


class Project(Task):

    def __init__(self, *args):
        super().__init__(*args)

    @staticmethod
    def gen_list():
        project = mydb.execute(
            '''select name, main_color, budget_currency, cast(budget_value as float) from project where name != ''; ''')
        gbp = 1.3
        eur = 1.1
        eur_to_usd = [[i[0], i[1], math.floor(
            int(i[3]) * eur)] for i in project if i[2] == 'EUR']
        gbp_to_usd = [[i[0], i[1], math.floor(
            int(i[3]) * gbp)] for i in project if i[2] == 'GBP']
        usd = [[i[0], i[1], math.floor(int(i[3]))]
               for i in project if i[2] == 'USD']
        full = eur_to_usd + gbp_to_usd + usd
        calculator = 100 / max([i[2] for i in full])
        return [Project(i[0], i[2] * calculator, i[1])for i in full]
