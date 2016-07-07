from connection import *
from task import *
import datetime


today = datetime.date.today()


class Manager(Task):

    def __init__(self, *args):
        super().__init__(*args)

    # Generate a list with company instances, with the necessary attributes
    @classmethod
    def gen_list(cls):
        cursor.execute("""SELECT manager, duedate, cast(budget_value AS float), main_color FROM project
                          WHERE duedate BETWEEN '2000-01-01' AND now()
                          AND budget_currency = 'EUR'
                          AND manager != ''
                          ORDER BY manager;""")
        managers = cursor.fetchall()
        managers = [[i[0], (today - i[1]).days, i[2], i[3], i[4]] for i in managers]
        managers = [[i[0], i[1]/i[2], i[4]] for i in managers]
        calculator = 100/max([i[1] for i in managers])
        return [Manager(i[0], i[1] * calculator, i[2]) for i in managers]
