import sqlite3

from prettytable import from_db_cursor


############ Блок запросов на полный вывод таблиц ############

def get_tables():

    connection = sqlite3.connect('Warhouse.sqlite')

    cursor = connection.cursor()

    cursor.execute('''Select * From Products''')

    products_table = from_db_cursor(cursor)


    cursor.execute('''Select * From Stuff''')

    stuff_table = from_db_cursor(cursor)


    cursor.execute('''Select * From Orders Order By o_delivery''')

    orders_table = from_db_cursor(cursor)


    cursor.execute('''Select * From Ordered_Products Order By op_order_id, op_product_id''')

    op_table = from_db_cursor(cursor)


    cursor.execute('''Select * From Deliveries Order By d_order_id''')

    deliveries_table = from_db_cursor(cursor)


    cursor.execute('''Select * From Products_log Order By pl_id''')

    pl_table = from_db_cursor(cursor)


    cursor.execute('''Select * From Stuff_log Order By sl_id''')

    sl_table = from_db_cursor(cursor)
    
    connection.close()

    tables = {
        'Products': products_table,
        'Stuff': stuff_table,
        'Orders': orders_table,
        'OP': op_table,
        'Deliveries': deliveries_table,
        'PL': pl_table,
        'SL': sl_table
    }

    return tables

#############################################################


############ Блок функций возврата таблиц ############

def return_optional(table_name):

    tables = get_tables()

    return tables[table_name]
    
#############################################################