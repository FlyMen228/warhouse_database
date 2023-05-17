import sqlite3


def create_db():

    connection = sqlite3.connect('Warhouse.sqlite')

    cursor = connection.cursor()


    ############ Блок сброса таблиц перед инициализацией ############

    cursor.execute('Drop Table If Exists Products')
    cursor.execute('Drop Table If Exists Stuff')
    cursor.execute('Drop Table If Exists Products_log')
    cursor.execute('Drop Table If Exists Stuff_log')
    cursor.execute('Drop Table If Exists Orders')
    cursor.execute('Drop Table If Exists Ordered_Products')
    cursor.execute('Drop Table If Exists Deliveries')

    #############################################################


    ############ Блок создания таблиц ############

    cursor.execute('''Create Table if Not Exists Products (
        p_id Integer,
        p_name varchar(100) Not Null,
        p_quantity int Default 0,
        p_price numeric Default 0,
        p_stock_status numeric(3) Default 0,
        p_orders int Default 0,
        p_sales int Default 0,
        p_time_in_stock numeric(2) Default 1,
        p_supply_date timestamp,
        Constraint PK_Products Primary Key(p_id),
        Constraint UQ_Products_name Unique(p_name),
        Constraint CK_Products_quantity Check(p_quantity >= 0),
        Constraint CK_Products_stock_status Check(p_stock_status >= 0 and p_stock_status <= 100),
        Constraint CK_Products_orders Check(p_orders >= 0),
        Constraint CK_Products_sales Check(p_sales >= 0),
        Constraint CK_Products_time_in_stock Check(p_time_in_stock >= 1 and p_time_in_stock <= 28),
        Constraint CK_Products_price Check(p_price >= 0))''')

    cursor.execute('''Create Table If Not Exists Stuff (
        s_id Integer,
        s_fullname varchar(50) Not Null,
        s_role varchar(20) Not Null,
        s_phone varchar(7),
        Constraint PK_stuff Primary Key (s_id))''')

    cursor.execute('''Create Table If Not Exists Products_log (
        pl_id int,
        pl_name varchar(100),
        pl_quantity int Default 0,
        pl_price numeric Default 0,
        pl_stock_status numeric(3) Default 0,
        pl_orders int Default 0,
        pl_sales int Default 0,
        pl_time_in_stock numeric(2) Default Null,
        pl_supply_date timestamp Default Null,
        pl_mod_date timestamp Default CURRENT_TIMESTAMP,
        pl_operation varchar(15) Not Null)''')

    cursor.execute('''Create Table If Not Exists Stuff_log (
        sl_id int,
        sl_fullname varchar(50),
        sl_role varchar(20),
        sl_phone varchar(7),
        sl_mod_date timestamp Default CURRENT_TIMESTAMP,
        sl_operation varchar(15) Not Null)''')

    cursor.execute('''Create Table If Not Exists Orders (
        o_id Integer,
        o_delivery varchar(3) Not Null,
        o_address varchar(255),
        o_date timestamp Default CURRENT_TIMESTAMP,
        Constraint PK_Orders Primary Key (o_id),
        Constraint CK_Orders_delivery Check(o_delivery = "Yes" or o_delivery = "No"))''')

    cursor.execute('''Create Table if Not Exists Ordered_Products (
        op_product_id int,
        op_order_id int,
        op_quantity int Not Null,
        op_cost numeric Default 0,
        Constraint PK_OP_product Primary Key (op_product_id, op_order_id),
        Constraint FK_OP_product Foreign Key (op_product_id) References Products (p_id),
        Constraint FK_OP_order Foreign Key (op_order_id) References Orders (o_id) On Delete Cascade,
        Constraint CK_OP_quantity Check(op_quantity > 0))''')

    cursor.execute('''Create Table If Not Exists Deliveries (
        d_id Integer,
        d_order_id int,
        d_deliverer_id int,
        Constraint PK_Deliveries Primary Key (d_id),
        Constraint FK_Deliveries_order Foreign Key (d_order_id) References Orders (o_id) On Delete Cascade,
        Constraint FK_Deliveries_deliverer Foreign Key (d_deliverer_id) References Stuff (s_id))''')

    #############################################################


    connection.close()