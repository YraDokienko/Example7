import sqlite3
from constants import *


class Sqlite3DataBase:

    def __init__(self):
        self.database = DATABASE_DB

    def sql_query_database(self, sql_query):
        connect_db = sqlite3.connect(self.database)
        cursor = connect_db.cursor()
        cursor.execute(sql_query)
        connect_db.commit()
        answer = cursor.fetchall()
        cursor.close()
        connect_db.close()
        return answer


    def sql_read_database(self, table_db):
        """Метод позволяет выводить данные таблицы"""
        sql_query = 'SELECT * FROM ' + str(table_db)
        return print(self.sql_query_database(sql_query))

    def sql_get_last_record_in_table(self, table_db):
        """Метод позволяет получить последнюю запись в таблице"""
        sql_query = 'SELECT * FROM ' + str(table_db) + ' ORDER BY id DESC LIMIT 1'
        return print(self.sql_query_database(sql_query))

    def sql_add_new_object(self, table_db, new_object):
        """Метод позволяет добвлять новый обьек в таблицу"""
        sql_query = 'INSERT INTO ' + str(table_db) + ' VALUES ' + str(new_object)
        self.sql_query_database(sql_query)
        self.sql_get_last_record_in_table(table_db)

    def sql_get_object_by_id(self, table_db, id_object):
        """Метод позволяет получить обьект по его ID  из необходимой таблицы"""
        sql_query = 'SELECT * FROM ' + str(table_db) + ' WHERE id =' + str(id_object)
        return print(self.sql_query_database(sql_query))

    def sql_get_list_sorted_by_field(self, table_db, sort_column):
        sql_query = 'SELECT * FROM ' + str(table_db) + ' ORDER BY ' + str(sort_column)
        sort_list = self.sql_query_database(sql_query)
        for row in sort_list:
            print(row)

    def sql_delite_table(self, table_db):
        """Метод позволяет удалить таблицу из базы данных по имени таблицы"""
        sql_query = 'DROP TABLE IF EXISTS ' + table_db
        self.sql_query_database(sql_query)