'''START OF DATABASE FOR   (BACKEND CODE)'''
import sqlite3

def connect():
    conn=sqlite3.connect("v_health.db")
    cur=conn.cursor()
    cur.execute("create table faculty(f_id varchar(5) primarykey,f_name varchar(20),f_password varchar(20) not null);")
    cur.execute("""create table faculty(f_id varchar(5) primarykey,f_name varchar(20),f_password varchar(20) not null);""")

	cur.execute("""create table doctor(d_id varchar(5) primarykey,d_name varchar(20) ,d_password varchar(20) not null,department varchar(30),timeslot timestamp);""")

	cur.execute("""create table procter(pr_id varchar(5) primarykey,pr_name varchar(20),pr_password varchar(20) not null);""")

    cur.execute("""create table remedy(r_name varchar(20) primarykey,r_desc varchar(200));""")

    cur.execute("""create table mess(m_id varchar(5) primarykey,m_type varchar(20),m_block varchar(200));""")

    cur.execute("""create table student(s_id varchar(5) primery key,s_name varchar(20) not null,s_password varchar(20) not null,s_email varchar(30) check(s_email ),s_address varchar(50), s_hostel varchar(2), s_blood_group varchar(5),s_mess varchar(2)),s_dob date,p_id varchar(5), s_phone varchar(10),s_parent_phone varchar(10),s_password varchar(20);""")

    cur.execute("""create table patient(pa_regno varchar(5) primary key,pa_problem varchar(100),pa_leave_approval varchar(10),pa_password varchar(20));""")
    cur.execute('''
        CREATE TABLE IF NOT EXISTS gps_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            latitude REAL,
            longitude REAL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')


    conn.commit()
    conn.close()

def insert():
    conn=sqlite3.connect("v_health.db")
    cur=conn.cursor()
    cur.execute('''INSERT INTO procter VALUES ('p{i}', '{name[i]}', '{password[0]}')''')
    cur.execute('''INSERT INTO doctor VALUES ('d{i}', '{name[i]}', '{password[0]}')''')
    cur.execute('''INSERT INTO faculty VALUES ('f{i}', '{name[i]+surname[i]}', 'currentDateTime')''')
    cur.execute('''INSERT INTO remedy VALUES ('diaseas{i}', 'desc_diaseas{name[i]}', 'password{0}')''')
    cur.execute('''INSERT INTO mess VALUES ('m{i}','{type[i]}' ,'{mess[i]}','s{i}' )''')
    cur.execute('''INSERT INTO student VALUES ('s{i}', '{name[i]}', '{name[i]+surname[i]}@gmail.com','{address[i]}','{mess[i]}','{bd[i]}','{mess[i]}','currentdate','p{i}','{i}455612239','{i}788984556','{password[0]}')''')
    cur.execute('INSERT INTO gps_data (latitude, longitude) VALUES (?, ?)', (latitude, longitude))
    cur.execute('''INSERT INTO patient VALUES ('s{i}', '{desc_diseas[0]}', '{leave_status[0]}')''')
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("v_health.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM students")
    rows=cur.fetchall()
    conn.close()
    return rows
