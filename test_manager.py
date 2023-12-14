
import unittest
import manager
import os
import time
import queue
import threading
# python3 -m unittest -v test_manager.py

MYSQL_IP = os.getenv('MYSQL_IP', default='0.0.0.0')
MYSQL_USER = os.getenv('MYSQL_USER', default='customer')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', default='customerpass')
MYSQL_DATABASE = os.getenv('MYSQL_DATABASE', default='app')


class TestRedisManagerMethods(unittest.TestCase):

    def package(self, f, i, q):
        result = f(i)
        q.put(result)

    def test_get_data(self):
        h = manager.create_handler(
            MYSQL_IP, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE)
        result = h.execute_return_all("select * from users;")
        print(result)


if __name__ == '__main__':
    unittest.main()
