import sqlite3

conn = sqlite3.connect('D:\\Python\\work_vasilii\\django_progect\\alhbret\\db.sqlite3') # подключаемся к базе данных
cur = conn.cursor() #осле создания объекта соединения с базой данных нужно создать объект cursor. Он позволяет делать SQL-запросы к базе
cur.execute("SELECT id, name FROM medsite_user")
one_result = cur.fetchone()
print(one_result)
list_name_db = cur.execute("SELECT name FROM medsite_user")
conn.commit()
conn.close()
# def read_sqlite_table(records):
#     try:
#         sqlite_connection = sqlite3.connect('db.sqlite3')
#         cursor = sqlite_connection.cursor()
#         print("Подключен к SQLite")
#
#         sqlite_select_query = """SELECT id FROM medsite_user"""
#         cursor.execute(sqlite_select_query)
#         records = cursor.fetchall()
#         print("Всего строк:  ", len(records))
#         print("Вывод каждой строки")
#         for row in records:
#             print("Имя:", row[1])
#
#         cursor.close()
#
#     except sqlite3.Error as error:
#         print("Ошибка при работе с SQLite", error)
#     finally:
#         if sqlite_connection:
#             sqlite_connection.close()
#             print("Соединение с SQLite закрыто")
#

