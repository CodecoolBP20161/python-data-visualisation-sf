from connection import *
from task import *


class Company(Task):

    def __init__(self, *args):
        super().__init__(*args)

    # Generate a list with company instances, with the necessary attributes
    @classmethod
    def gen_list(cls):
        # company_list = []
        companies = mydb.execute("""SELECT company_name, main_color,cast(budget_value as float) FROM project WHERE status BETWEEN '2' AND '4'
                        and maintenance_requested = 'true'
                        and main_color != ''
                        and budget_currency = 'GBP';""")
        calculator = 100 / max([i[2] for i in companies])
        return [Company(i[0], i[2] * calculator, i[1]) for i in companies]
