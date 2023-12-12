
import mysql.connector
import random
import string
from time import time

def create_connector(host, user, password, database):
    connector = mysql.connector.connect(user=user, password=password,
                                        host=host, database=database)
    return connector

def create_handler(host, user, password, database):
    connector = mysql.connector.connect(user=user, password=password,
                                        host=host, database=database)
    h = Handler(connector)
    return h


class Handler:
    def __init__(self, connector) -> None:
        self.connector = connector
        self.cursor = self.connector.cursor()

    def __del__(self):
        if self.cursor:
            self.cursor.close()
        if self.connector:
            self.connector.close()

    def execute_return_all(self, command):
        try:
            self.cursor.execute(command)
            result = self.cursor.fetchall()
            self.connector.commit()

        except Exception as e:
            return e
        if result:
            return result


class Process:
    def __init__(self, connector) -> None:
        self.connector = connector
        self.cursor = self.connector.cursor()

    def __del__(self):
        if self.cursor:
            self.cursor.close()
        if self.connector:
            self.connector.close()

    def execute_return_all(self, command):
        try:
            self.cursor.execute(command)
            result = self.cursor.fetchall()
            self.connector.commit()

        except Exception as e:
            return e
        if result:
            return result

    def execute_return_one(self, command):
        try:
            result = self.cursor.fetchone()
            self.connector.commit()

        except Exception as e:
            return e
        if result:
            return result

    def run_singl_sheet_example(self, handler):
        database = 'demo'

        print('show databases')
        command = 'show databases;'.format(database)
        result = self.cursor.execute(command)
        handler.print_result(result)

        print('use database')
        command = 'use {};'.format(database)
        result = self.cursor.execute(command)
        self.cursor.print_result(result)

        print('create table')
        command = """
            create table users(
            default_id integer auto_increment primary key,
            name char(20),
            mail char(50),
            phone char(50),
            messages char(50)
            );
            """
        result = self.cursor.execute(command)
        self.cursor.print_result(result)

        print('insert data')
        command = """
            insert into users
            (name,mail,phone,messages)
            values
            ('{}','{}','{}','{}');
            """.format('jay', 'jay@qq.com', '0912345678', 'homosexuality')
        result = self.cursorself.cursor.execute(command)
        self.cursor.print_result(result)
        command = """
            insert into users
            (name,mail,phone,messages)
            values
            ('{}','{}','{}','{}');
            """.format('may', 'may@qq.com', '0912345678', 'people')
        result = self.cursor.execute(command)
        self.cursor.print_result(result)
        command = """
            insert into users
            (name,mail,phone,messages)
            values
            ('{}','{}','{}','{}');
            """.format('kay', 'kay@qq.com', '0912345678', 'today')
        result = self.cursor.execute(command)
        self.cursor.print_result(result)
        command = """
            insert into users
            (name,mail,phone,messages)
            values
            ('{}','{}','{}','{}');
            """.format('amy', 'amy@qq.com', '0912345678', 'today')
        result = self.cursor.execute(command)
        self.cursor.print_result(result)

        print('show data')
        command = """
            select * from users;
            """
        result = self.cursor.execute(command)
        self.cursor.print_result(result)

        print('show data with condition')
        command = """
            select * from users where name='jay';
            """
        result = self.cursor.execute(command)
        self.cursor.print_result(result)

        print('show data order by')
        command = """
            select * from users order by name;
            """
        result = self.cursor.execute(command)
        self.cursor.print_result(result)

        print('delete sepecific data')
        command = "delete from users where name='amy';"
        result = self.cursor.execute(command)
        self.cursor.print_result(result)

        print('show data order by')
        command = """
            select * from users order by name;
            """
        result = self.cursor.execute(command)
        self.cursor.print_result(result)

        print('update data')
        command = """
            UPDATE users
            set name='jjj'
            where
            name='jay';
            """.format('jay', 'jay@qq.com', '0912345678', 'homosexuality')
        result = self.cursor.execute(command)
        self.cursor.print_result(result)

        print('show data order by')
        command = """
            select * from users order by name;
            """
        result = self.cursor.execute(command)
        self.cursor.print_result(result)

        print('limit')
        command = """
            select * from users limit 2;
            """
        result = self.cursor.execute(command)
        self.cursor.print_result(result)

        print('drop table')
        command = """
            drop table users;
            """
        result = self.cursor.execute(command)
        self.cursor.print_result(result)

    def create_users_table(self):
        command = """
            CREATE TABLE users (
                user_id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(30) NOT NULL,
                credit DECIMAL(5, 2),
                height FLOAT,
                weight FLOAT,
                age INT,
                update_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                INDEX idx_age (age))           
        """

    def create_market_users_table(self):
        command = """
            CREATE TABLE events( 
                id INT AUTO_INCREMENT PRIMARY KEY, 
                name varchar(30), 
                cart json,
                credit INT
                );
            """

    def create_transcript(self):
        command = """
        CREATE TABLE transcript (
            user_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(30) NOT NULL,
            mandarin INT,
            english INT,
            math INT,
            physics INT,
            update_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            INDEX idx_math (math),
            INDEX idx_physics (physics),
            INDEX science (math,physics),
            INDEX liberal (mandarin,english)
            )           
        """
        self.execute_return_all(command)

    def insert_transcript(self):
        name = ''

        for i in range(5000):
            name = ''
            for _ in range(5):
                name += random.choice(string.ascii_lowercase)
            command = """
            insert into transcript
            (name,mandarin,english,math,physics)
            values
            ('{}','{}','{}','{}','{}');
            """.format(name, random.randint(0, 100),
                       random.randint(0, 100),
                       random.randint(0, 100),
                       random.randint(0, 100))
            self.execute_return_all(command)

    def delete_transcript(self):
        command = """
        DROP TABLE transcript;        
        """
        self.execute_return_all(command)

    def transcript_select_all_time(self):
        command = """
        SELECT * FROM transcript;
        """
        start_time = time()
        self.execute_return_all(command)
        print("elapse: {}".format(time()-start_time))

    def transcript_select_key_large_than_60_time(self, key):
        command = """
        SELECT user_id,name,{} FROM transcript WHERE {}>60;
        """.format(key, key)
        start_time = time()
        self.execute_return_all(command)
        print("elapse: {}".format(time()-start_time))

    def alter_create_index(self):
        command = """
        ALTER TABLE transcript ADD INDEX idx_physics (physics);        
        """

    def run_transcript_example(self):
        self.create_transcript()
        self.insert_transcript()
        self.transcript_select_key_large_than_60_time('math')
        self.transcript_select_key_large_than_60_time('mandarin')
        # self.delete_transcript()

    def counter_example(self):
        command = """
        select user_id(*) as user from transcript;
        """


if __name__ == '__main__':
    connector = create_connector('0.0.0.0', 'root', 'testpassword', 'demo')
    process = Process(connector)
    process.run_transcript_example()
    del process
