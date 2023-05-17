import sqlite3


def create_triggers():

    connection = sqlite3.connect('Warhouse.sqlite')

    cursor = connection.cursor()


    ############ Блок сброса триггеров перед инициализацией ############

    cursor.execute('''Drop Trigger If Exists After_Insert_Products''')
    cursor.execute('''Drop Trigger If Exists After_Delete_Products''')
    cursor.execute('''Drop Trigger If Exists After_Update_Products''')


    cursor.execute('''Drop Trigger If Exists After_Insert_Stuff''')
    cursor.execute('''Drop Trigger If Exists After_Delete_Stuff''')
    cursor.execute('''Drop Trigger If Exists After_Update_Stuff''')


    cursor.execute('''Drop Trigger If Exists After_Insert_OP''')
    cursor.execute('''Drop Trigger If Exists After_Delete_OP''')
    cursor.execute('''Drop Trigger If Exists After_Update_OP''')

    #############################################################


    ############ Блок создания триггеров для таблицы Products_log ############

    cursor.execute('''Create Trigger If Not Exists After_Insert_Products
        After Insert On Products
        Begin
            Insert Into Products_log
            Values (New.p_id, New.p_name, New.p_quantity, New.p_price, New.p_stock_status, New.p_orders,
                    New.p_sales, New.p_time_in_stock, New.p_supply_date, CURRENT_TIMESTAMP, "Insert");
        End''')

    cursor.execute('''Create Trigger If Not Exists After_Delete_Products
        After Delete On Products
        Begin
            Insert Into Products_log
            Values (Old.p_id, Old.p_name, Old.p_quantity, Old.p_price, Old.p_stock_status, Old.p_orders,
                    Old.p_sales, Old.p_time_in_stock, Old.p_supply_date, CURRENT_TIMESTAMP, "Delete");
        End''')

    cursor.execute('''Create Trigger If Not Exists After_Update_Products
        After Update On Products
        Begin
            Insert Into Products_log
            Values (New.p_id, New.p_name, New.p_quantity, New.p_price, New.p_stock_status, New.p_orders,
                    New.p_sales, New.p_time_in_stock, New.p_supply_date, CURRENT_TIMESTAMP, "Update");
        End''')

    #############################################################


    ############ Блок создания триггеров для таблицы Stuff_log ############

    cursor.execute('''Create Trigger If Not Exists After_Insert_Stuff
        After Insert On Stuff
        Begin
            Insert Into Stuff_log
            Values (New.s_id, New.s_fullname, New.s_role, New.s_phone, CURRENT_TIMESTAMP, "Insert");
        End''')

    cursor.execute('''Create Trigger If Not Exists After_Delete_Stuff
        After Delete On Stuff
        Begin
            Insert Into Stuff_log
            Values (Old.s_id, Old.s_fullname, Old.s_role, Old.s_phone, CURRENT_TIMESTAMP, "Delete");
        End''')

    cursor.execute('''Create Trigger If Not Exists After_Update_Stuff
        After Update On Stuff
        Begin
            Insert Into Stuff_log
            Values (New.s_id, New.s_fullname, New.s_role, New.s_phone, CURRENT_TIMESTAMP, "Insert");
        End''')

    #############################################################


    ############ Блок создания триггеров для таблицы Ordered_Products ############

    cursor.execute('''Create Trigger If Not Exists After_Insert_OP
        After Insert On Ordered_Products
        When (Select p_quantity From Products Where p_id = New.op_product_id) >= New.op_quantity
        Begin
            Update Products Set p_quantity = (Select p_quantity - New.op_quantity From Products Where p_id = New.op_product_id) Where p_id = New.op_product_id;
            Update Ordered_Products Set op_cost = (Select p_price From Products Where p_id = op_product_id) * op_quantity;
        End''')

    cursor.execute('''Create Trigger If Not Exists After_Delete_OP
        After Delete On Ordered_Products
        Begin
            Update Products Set p_quantity = p_quantity + Old.op_quantity Where p_id = Old.op_product_id;
        End''')
    
    cursor.execute('''Create Trigger If Not Exists After_Update_OP
        After Update On Ordered_Products
        When (Select p_price * New.op_quantity From Products Where p_id = New.op_product_id) != (Select p_price * Old.op_quantity From Products Where p_id = Old.op_product_id) and (Select p_quantity From Products Where p_id = New.op_product_id) + Old.op_quantity >= New.op_quantity
        Begin
            Update Products Set p_quantity = p_quantity + Old.op_quantity - New.op_quantity Where p_id = New.op_product_id;
            Update Ordered_Products Set op_cost = (Select p_price From Products Where p_id = op_product_id) * op_quantity;
        End''')

    #############################################################


    connection.close()