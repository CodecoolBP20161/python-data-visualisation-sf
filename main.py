from tagcloud import TagCloud
from client import Client
from project import Project
from company_name import Company
from manager import Manager
from headquarter import Headquarter


def main():
    while True:
        main_menu()


def main_menu():
    print('1. Client\n2. Project\n3. Company\n4. Manager\n5. Headquarter')
    select = input('Please type which task run or E to exit! ')
    if select == 'e':
        exit()
    elif select == '1':
        tag_menu(task=Client.gen_list())
    elif select == '2':
        tag_menu(task=Project.gen_list())
    elif select == '3':
        tag_menu(task=Company.gen_list())
    elif select == '4':
        tag_menu(task=Manager.gen_list())
    elif select == '5':
        tag_menu(task=Headquarter.gen_list())


def tag_menu(task):
    background_color = {'black': '#000', 'white': '#fff', 'grey': '#d3d3d3', 'red': '#FF0000'}
    print('1. aquawax\n2. arial\n3. DK\n4. keepcalm\n5. kenyan')
    options = {'1': 'aquawax', '2': 'arial', '3': 'DK', '4': 'keepcalm', '5': 'kenyan'}
    while True:
        try:
            inst = TagCloud(task, font=TagCloud.FONTS[options[input('Please select the type of font! ')]],
                            background_color=background_color
                            [input("Choose background color from black, white, red and grey! ")])
            inst.drawing()
            break
        except KeyError:
            print('That was invalid option, please try again!')
            print('1. aquawax\n2. arial\n3. DK\n4. keepcalm\n5. kenyan')

main()

