from connection import *


class Client(object):

    def __init__(self, company_name, num_of_projects, color_mix):
        self.company_name = company_name
        self.num_of_projects = num_of_projects
        self.color_mix = color_mix

    # Generate a list with company instances, with the necessary attributes
    @classmethod
    def gen_list(cls):
        clients = []
        cursor.execute("SELECT count(name), company_name from project GROUP BY company_name")
        companies = cursor.fetchall()
        # Filling the colom_mix list and making the instances
        for company in companies:
            project_number = company[0]
            cursor.execute("SELECT main_color from project WHERE company_name = '" + company[1] + "'")
            color_mix = []
            for color in cursor.fetchall():
                color_mix.append(color[0])
            clients.append(cls(company[1], project_number, color_mix))
        return clients

