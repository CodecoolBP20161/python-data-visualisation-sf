from connection import *

class Client(object):
    def __init__(self, company_name, num_of_project, color_mix):
        self.company_name = company_name
        self.num_of_project = num_of_project
        self.color_mix = color_mix


    @classmethod
    def gen_list(cls):
        clients = []
        cursor.execute("SELECT count(name), company_name from project GROUP BY company_name")
        companies = cursor.fetchall()
        for company in companies:
            project_number = company[0]
            query = "SELECT main_color from project WHERE company_name = '" + company[1] + "'"
            cursor.execute(query)
            color_mix_fetch = cursor.fetchall()
            color_mix = []
            for color in color_mix_fetch:
                color_mix.append(color[0])
            clients.append(cls(company[1], project_number, color_mix))
        return clients

clients = Client.gen_list()
print(clients[3].__dict__)
