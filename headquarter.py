from task import *
from connection import *



class Headquarter(Task):

    def __init__(self, *args):
        super().__init__(*args)

    @staticmethod
    def gen_list():
        cursor.execute(
            '''select company_hq, main_color, duedate from project where company_hq != '' order by duedate limit 30; ''')
        project = cursor.fetchall()
        calculator = 100/len(project)
        return [Headquarter(i[0], 100-calculator*(project.index(i)), i[1])for i in project]
        
