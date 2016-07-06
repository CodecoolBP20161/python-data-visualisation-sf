from connection import *

class Client(object):
    clients = []

    def __init__(self, company_name, num_of_project, color_mix):
        self.company_name = company_name
        self.num_of_project = num_of_project
        self.color_mix = color_mix


    @classmethod
    def gen_list(cls):
        cursor.execute("SELECT count(name), company_name from project GROUP BY company_name")
        companies = cursor.fetchall()
        for company in companies:
            project_number = company[0]
            cursor.execute("SELECT main_color from project WHERE company_name = '" + company[1] + "'")
            color_mix = []
            for color in cursor.fetchall():
                color_mix.append(color[0])
            cls.clients.append(cls(company[1], project_number, color_mix))
