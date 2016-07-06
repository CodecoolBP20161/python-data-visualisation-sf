from connection import *
from task import *


class Client(Task):

    def __init__(self,*args):
        super().__init__(*args)

    # Generate a list with company instances, with the necessary attributes
    @classmethod
    def gen_list(cls):
        clients = []
        cursor.execute("SELECT count(name), company_name from project GROUP BY company_name")
        companies = cursor.fetchall()
        calculator = 100/max([i[0] for i in companies])
        # Filling the colom_mix list and making the instances
        for company in companies:
            project_number = company[0]
            cursor.execute("SELECT main_color from project WHERE company_name = '" + company[1] + "'")
            color_mix = []
            for color in cursor.fetchall():
                color_mix.append(color[0])
            clients.append(cls(company[1], project_number*calculator, color_mix))
        return clients

x = Client.gen_list()
print(x[2].priority)
