import psycopg2

dbname = 'code'#input('Please enter database name!')
user = 'code'#input('Please enter username!')
password = 'code'#input('Please enter password!')

try:
    # setup connection string
    connect_str = "dbname=%s user=%s host='localhost' password=%s"%(dbname,user,password)
    # use our connection values to establish a connection
    conn = psycopg2.connect(connect_str)
    # create a psycopg2 cursor that can execute queries
    cursor = conn.cursor()

    cursor.execute("""SELECT company_hq FROM project;""")

    rows = cursor.fetchall()
    #print(rows)
except Exception as e:
    print("PROBLEM!!!!")
    print(e)
