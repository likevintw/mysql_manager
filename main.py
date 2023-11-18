import mysql.connector


def create_handler(host, user, password, database):
    connect = mysql.connector.connect(user=user, password=password,
                                      host=host, database=database)
    handler = Handler(connect)
    connect.ping()
    return handler


class Handler:
    def __init__(self, connect) -> None:
        self.connect = connect
        self.cursor = connect.cursor()

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
        print("")
        for i in result:
            print(i)


class Process:
    def __init__(self) -> None:
        pass

    def current(self, handler):
        database = 'demo'

        command = 'show databases;'.format(database)
        result = handler.execute(command)
        handler.print_result(result)

        command = 'use {};'.format(database)
        result = handler.execute(command)
        handler.print_result(result)

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

        command = """
            select * from users;
            """
        result = handler.execute(command)
        handler.print_result(result)

        command = """
            select * from users where name='jay';
            """
        result = handler.execute(command)
        handler.print_result(result)

        command = """
            select * from users order by name;
            """
        result = handler.execute(command)
        handler.print_result(result)

        command = "delete from users where name='amy';"
        result = handler.execute(command)
        handler.print_result(result)

        command = """
            select * from users order by name;
            """
        result = handler.execute(command)
        handler.print_result(result)

        command = """
            drop table users;
            """
        result = handler.execute(command)
        handler.print_result(result)


if __name__ == '__main__':
    handler = create_handler('0.0.0.0', 'root', 'testpassword', 'demo')
    process = Process()
    process.current(handler)
