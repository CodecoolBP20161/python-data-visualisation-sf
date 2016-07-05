from connection import *

class Client(object):
    def __init__(self,company_name,num_of_project,color_mix):
        self.company_name = company_name
        self.num_of_project = num_of_project
        self.color_mix = color_mix


cursor.execute("""select count(name),company_name from project group by company_name;""")
company = cursor.fetchall()
cursor.execute("""select color_mix from project group by company_name;""")
