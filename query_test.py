from msilib.schema import tables
import sqlite3
from venv import create


def insert (table_name, record_name, value):
    # connect to database
    conn = sqlite3.connect('test.db')
    # create a cursor object
    c = conn.cursor()
    # the query of the database
    if record_name == "voi_info" :
        print("insert voice")
        c.execute("INSERT INTO Voices (voi_info) VALUES (?);",(value,))
    else : 
        if record_name == 'tex_info':
            c.execute("INSERT INTO Texts (tex_info) VALUES (?);",(value,)) 
        else : 
            if type(value) == type(000):
                c.execute("INSERT INTO " + table_name +"("+record_name+") VALUES (?);",(value))
        #commit the executed transaction
    conn.commit()
    # close the connection
    conn.close()
    
    
def get_last_id(table_name,table_id_name):
     # connect to database
    conn = sqlite3.connect('test.db')
    # create a cursor object
    c = conn.cursor()
    # the query of the database
    c.execute("select max("+table_id_name+") from "+table_name+";")
    id = c.fetchone()
    #commit the executed transaction
    conn.commit()
    # close the connection
    conn.close()
    # modifying the id from tuple to string 
    id = str(id)
    id = id.replace('(', '')
    id = id.replace(')', '')
    id = id.replace(',', '')
    return id 
    
def update( updated_table_name, changed_column_name, new_value , updated_row_id_name ,updated_row_id_value):
     # connect to database
    conn = sqlite3.connect('test.db')
    # create a cursor object
    c = conn.cursor()
    # the query of the database
    c.execute("UPDATE "+updated_table_name+" SET "+changed_column_name+" = "+new_value+" WHERE "+updated_row_id_name+" = "+updated_row_id_value+";")
    #commit the executed transaction
    conn.commit()
    # close the connection
    conn.close()
def select(table_name, column_name, row_id_name, wanted_id_value):
    # connect to database
    conn = sqlite3.connect('test.db')
    # create a cursor object
    c = conn.cursor()
    # the query of the database
    c.execute("SELECT "+  column_name +" FROM "+ table_name  +" WHERE "+ row_id_name +" = "+ wanted_id_value +";")
    data = c.fetchall()
    #commit the executed transaction
    conn.commit()
    # close the connection
    conn.close()
    return tuple_to_string(data)

def tuple_to_string(tuple):
    # convert tuple to string
    result = ''
    for i in tuple :
        for j in i:
            result = result + j
    return result
def create_database():
    # connect to database
    conn = sqlite3.connect('DataBase.db')
    # create a cursor object
    c = conn.cursor()
    # the query of the database
    c.execute("CREATE table Voices ( voi_id INTEGER primary key autoincrement, voi_info blobs not null);")
    c.execute("CREATE table Types (typ_id INTEGER primary key autoincrement,    typ_name varchar(255) NOT NULL );")
    c.execute("CREATE table Texts (    tex_id INTEGER primary key autoincrement,    tex_info text not null,    Voi_id INTEGER ,    constraint fk foreign key (voi_id) references voices (voi_id));")
    c.execute("CREATE table Bills (    bil_id INTEGER primary key autoincrement,    bil_cost number not null,    bil_description  text not null default 'not added',     is_income boolean not null ,     tex_id INTEGER ,     typ_id INTEGER,    constraint fk foreign key (tex_id) references texts (tex_id),    constraint fk foreign key (typ_id) references Types (typ_id));")
    c.execute("INSERT INTO Types (typ_name ) values ('food');")
    c.execute("INSERT INTO Types (typ_name ) values ('work');")
    c.execute("INSERT INTO Types (typ_name ) values ('education');")
    c.execute("INSERT INTO Types (typ_name ) values ('transport');")
    c.execute("INSERT INTO Types (typ_name ) values ('people');")
    c.execute("INSERT INTO Types (typ_name ) values ('something else');")
    #commit the executed transaction
    conn.commit()
    # close the connection
    conn.close()