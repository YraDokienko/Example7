from sql_query import Sqlite3DataBase
from database import create_table_database


create_table_database()
queryDataBase = Sqlite3DataBase()
queryDataBase.sql_read_database('pizza')
queryDataBase.sql_add_new_object('pizza', (7, 'Мексикано', 118))
queryDataBase.sql_get_object_by_id('pizza', 5)
queryDataBase.sql_get_list_sorted_by_field('pizza', 'name')
# queryDataBase.sql_delite_table('pizza')
