import sqlite3
from constants import *


def create_table_database():
    connect_db = sqlite3.connect(DATABASE_DB)
    cursor = connect_db.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS pizza (id INTEGER PRIMARY KEY AUTOINCREMENT, "
                                                       "name VARCHAR (150) NOT NULL, "
                                                       "price INT (8) NOT NULL);")
    data_pizza = [(1, 'Гавайская', 108),
                  (2, 'Барбекю', 108),
                  (3, 'Прованс', 132),
                  (4, 'Кантри', 132),
                  (5, 'Баварская', 108),
                  (6, 'Тоскана', 150)
                  ]
    cursor.executemany("INSERT INTO pizza VALUES (?,?,?)", data_pizza)
    connect_db.commit()

    cursor.execute("CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY AUTOINCREMENT, "
                                                       "delivery_address VARCHAR (250) NOT NULL, "
                                                       "comment_on_order VARCHAR (150), "
                                                       "data_order DATETIME, "
                                                       "quantity INTEGER (2), "
                                                       "id_customer REFERENCES customer (id_customer), "
                                                       "id_pizza REFERENCES pizza (id_pizza));")
    data_orders = [(1,'Щорса 32, кв 15', 'третий подьезд', '11.10.2019',2,1,3),
                   (2,'Базарная 42б кв 3', 'до 17-00', '11.10.2019',4,3,1),
                   (3,'Михайловская 8 , кв 213', '5-парадная', '11.10.2019',2,1,3),
                   (4,'Левитана 13б кв 45', 'с 16-00 до 18-00', '12.10.2019',2,2,2),
                   (5,'Косвенная 26', 'порезать', '12.10.2019',1,3,5),
                   (6, 'Михайловская 8 , кв 213', '5-парадная', '11.10.2019', 2, 1, 3),
                   (7, 'Левитана 13б кв 45', 'с 16-00 до 18-00', '12.10.2019', 1, 2, 2),
                   (8, 'Косвенная 26', 'порезать', '12.10.2019', 1, 3, 4)
                   ]
    cursor.executemany("INSERT INTO orders VALUES (?,?,?,?,?,?,?)", data_orders)
    connect_db.commit()

    cursor.execute("CREATE TABLE IF NOT EXISTS customer (id INTEGER PRIMARY KEY AUTOINCREMENT, "
                                                           "first_name VARCHAR (50) NOT NULL, "
                                                           "family_name VARCHAR (100) NOT NULL, "
                                                           "telephone_number INTEGER (12) NOT NULL, "
                                                           "Email VARCHAR (150), Date_Birth DATE);")
    cursor.execute("INSERT INTO customer VALUES (1, 'Vova', 'Petrov', '380675554433', 'vovka@gmail.com', '11.11.2000' )")
    cursor.execute("INSERT INTO customer VALUES (2, 'Yra', 'Dokienko', '380957985588', 'yradok@gmail.com', '26.05.1984' )")
    cursor.execute("INSERT INTO customer VALUES (3, 'Ivan', 'Ivanov', '380957776655', 'ivanov@gmail.com', '01.03.1984' )")
    connect_db.commit()
    cursor.close()
    connect_db.close()



