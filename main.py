import mysql.connector


def create_handler(host, user, password, database):
    connection = mysql.connector.connect(user=user, password=password,
                                         host=host, database=database)
    handler = Handler(connection)
    connection.ping()
    return handler


class Handler:
    def __init__(self, connection) -> None:
        self.connection = connection
        self.cursor = connection.cursor()

    def execute(self, command):
        try:
            self.cursor.execute(command)
            # result = self.cursor.fetchone()
            result = self.cursor.fetchall()

        except Exception as e:
            return e
        if result:
            return result

    def print_result(self, result):
        if result == None:
            return None
        if len(result) == 0:
            return None
        for i in result:
            print(i)
        print("")

    def __del__(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Database connection closed.")


class Process:
    def __init__(self) -> None:
        pass

    def run_singl_sheet_example(self, handler):
        database = 'demo'

        print('show databases')
        command = 'show databases;'.format(database)
        result = handler.execute(command)
        handler.print_result(result)

        print('use database')
        command = 'use {};'.format(database)
        result = handler.execute(command)
        handler.print_result(result)

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
        result = handler.execute(command)
        handler.print_result(result)

        print('insert data')
        command = """
            insert into users
            (name,mail,phone,messages)
            values
            ('{}','{}','{}','{}');
            """.format('jay', 'jay@qq.com', '0912345678', 'homosexuality')
        result = handler.execute(command)
        handler.print_result(result)
        command = """
            insert into users
            (name,mail,phone,messages)
            values
            ('{}','{}','{}','{}');
            """.format('may', 'may@qq.com', '0912345678', 'people')
        result = handler.execute(command)
        handler.print_result(result)
        command = """
            insert into users
            (name,mail,phone,messages)
            values
            ('{}','{}','{}','{}');
            """.format('kay', 'kay@qq.com', '0912345678', 'today')
        result = handler.execute(command)
        handler.print_result(result)
        command = """
            insert into users
            (name,mail,phone,messages)
            values
            ('{}','{}','{}','{}');
            """.format('amy', 'amy@qq.com', '0912345678', 'today')
        result = handler.execute(command)
        handler.print_result(result)

        print('show data')
        command = """
            select * from users;
            """
        result = handler.execute(command)
        handler.print_result(result)

        print('show data with condition')
        command = """
            select * from users where name='jay';
            """
        result = handler.execute(command)
        handler.print_result(result)

        print('show data order by')
        command = """
            select * from users order by name;
            """
        result = handler.execute(command)
        handler.print_result(result)

        print('delete sepecific data')
        command = "delete from users where name='amy';"
        result = handler.execute(command)
        handler.print_result(result)

        print('show data order by')
        command = """
            select * from users order by name;
            """
        result = handler.execute(command)
        handler.print_result(result)

        print('update data')
        command = """
            UPDATE users
            set name='jjj'
            where
            name='jay';
            """.format('jay', 'jay@qq.com', '0912345678', 'homosexuality')
        result = handler.execute(command)
        handler.print_result(result)

        print('show data order by')
        command = """
            select * from users order by name;
            """
        result = handler.execute(command)
        handler.print_result(result)

        print('limit')
        command = """
            select * from users limit 2;
            """
        result = handler.execute(command)
        handler.print_result(result)

        print('drop table')
        command = """
            drop table users;
            """
        result = handler.execute(command)
        handler.print_result(result)


if __name__ == '__main__':
    handler = create_handler('0.0.0.0', 'root', 'testpassword', 'demo')
    process = Process()
    process.run_singl_sheet_example(handler)
    del handler
