import sqlite3
from prettytable import from_db_cursor


############ Блок запросов на вывод определённых данных ############

def print_deliverer_stat(deliverer_id):

    connection = sqlite3.connect('Warhouse.sqlite')

    cursor = connection.cursor()

    cursor.execute('''Select * From Deliverers_All Where "ID Доставщика" = ?''', [(deliverer_id)])

    result = from_db_cursor(cursor)

    connection.close()
    
    return result


def print_deliverer_sum(deliverer_id):

    connection = sqlite3.connect('Warhouse.sqlite')

    cursor = connection.cursor()

    cursor.execute('''Select * From Deliverers_Summary Where "ID Доставщика" = ?''', [(deliverer_id)])

    result = from_db_cursor(cursor)

    connection.close()
    
    return result


def print_product_history(product_id):
    
    connection = sqlite3.connect('Warhouse.sqlite')

    cursor = connection.cursor()

    cursor.execute('''Select * From Products_History Where "ID Продукта" = ?''', [(product_id)])

    result = from_db_cursor(cursor)

    connection.close()
    
    return result


def print_employee_history(employee_id):

    connection = sqlite3.connect('Warhouse.sqlite')

    cursor = connection.cursor()

    cursor.execute('''Select * From Stuff_History Where "ID Работника" = ?''', [(employee_id)])

    result = from_db_cursor(cursor)

    connection.close()
    
    return result


def print_order_stat(order_id):
    
    connection = sqlite3.connect('Warhouse.sqlite')

    cursor = connection.cursor()

    if cursor.execute('''Select * From Orders_Stat_W_Delivery Where "ID Заказа" = ?''', [(order_id)]).fetchone() != None:
        
        cursor.execute('''Select * From Orders_Stat_W_Delivery Where "ID Заказа" = ?''', [(order_id)])
        
    else:
        
        cursor.execute('''Select * From Orders_Stat_WO_Delivery Where "ID Заказа" = ?''', [(order_id)])

    result = from_db_cursor(cursor)

    connection.close()
    
    return result


def print_order_Summary_cost(order_id):
    
    connection = sqlite3.connect('Warhouse.sqlite')

    cursor = connection.cursor()

    cursor.execute('''Select * From Orders_Cost_Summary Where "ID Заказа" = ?''', [(order_id)])

    result = from_db_cursor(cursor)

    connection.close()
    
    return result
    
    
def print_delivery_stat(delivery_id):

    connection = sqlite3.connect('Warhouse.sqlite')

    cursor = connection.cursor()

    cursor.execute('''Select * From Deliveries_Stat Where "ID Доставки" = ?''', [(delivery_id)])

    result = from_db_cursor(cursor)

    connection.close()
    
    return result

#############################################################