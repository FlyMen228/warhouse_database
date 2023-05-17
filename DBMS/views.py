import sqlite3


def create_views():

    connection = sqlite3.connect('Warhouse.sqlite')

    cursor = connection.cursor()


    ############ Блок сброса представлений ############

    cursor.execute('''Drop View If Exists Deliverers_All''')
    cursor.execute('''Drop View If Exists Deliverers_Summary''')
    cursor.execute('''Drop View If Exists Products_History''')
    cursor.execute('''Drop View If Exists Stuff_History''')
    cursor.execute('''Drop View If Exists Orders_Stat_W_Delivery''')
    cursor.execute('''Drop View If Exists Orders_Stat_WO_Delivery''')
    cursor.execute('''Drop View If Exists Orders_Cost_Summary''')
    cursor.execute('''Drop View If Exists Deliveries_Stat''')

    #############################################################


    ############ Блок создания представлений ############

    cursor.execute('''Create View If Not Exists Deliverers_All As
        Select s_id as 'ID Доставщика', s_fullname as 'ФИО Доставщика', d_id as 'ID Доставки', d_order_id as 'ID Заказа'
        From Stuff S Join Deliveries D On S.s_id = D.d_deliverer_id
        Where s_role = 'Deliverer'
        Order By s_id, d_id DESC;''')

    cursor.execute('''Create View If Not Exists Deliverers_Summary As
        Select s_id as 'ID Доставщика', s_fullname as 'ФИО Доставщика', Count(d_id) as 'Количество доставок'
        From Stuff S Join Deliveries D On S.s_id = D.d_deliverer_id
        Where s_role = 'Deliverer'
        Group By s_id
        Order By s_id;''')


    cursor.execute('''Create View If Not Exists Products_History As
        Select pl_id as 'ID Продукта', pl_name as 'Наименование продукта', pl_quantity as 'Остаток Продукта', pl_price as 'Стоимость единицы товара',
            pl_stock_status as 'Заполненность товара', pl_orders as 'Количество заказов товара',
            pl_sales as 'Продажи товара за неделю', pl_time_in_stock as 'День месяца продажи товара',
            pl_supply_date as 'Дата поставок товара на склад', pl_mod_date as 'Дата изменения данных'
        From Products_Log
        Order By pl_id, pl_mod_date;''')


    cursor.execute('''Create View If Not Exists Stuff_History As
        Select sl_id as 'ID Работника', sl_fullname as 'ФИО Работника', sl_role as 'Должность Работника',
            sl_phone as 'Рабочий телефон работника', sl_mod_date as 'Дата изменения данных'
        From Stuff_Log
        Order By sl_id, sl_mod_date;''')


    cursor.execute('''Create View If Not Exists Orders_Stat_W_Delivery As
        Select o_id as 'ID Заказа', p_name as 'Наименование товара', op_cost as 'Стоимость товаров', 
            o_address as 'Адрес доставки', d_id as 'ID Доставщика', s_fullname as 'ФИО Доставщика'
        From Products Join Ordered_Products On p_id = op_product_id
                    Join Orders On o_id = op_order_id
                    Join Deliveries On o_id = d_order_id
                    Join Stuff On d_deliverer_id = s_id
        Where o_delivery = 'Yes'
        Order By o_id, p_id;''')

    cursor.execute('''Create View If Not Exists Orders_Stat_WO_Delivery As
        Select o_id as 'ID Заказа', p_name as 'Наименование товара', op_cost as 'Стоимость товаров', 'Доставка не осуществлялась' as 'Статус Доставки'
        From Products Join Ordered_Products On p_id = op_product_id
                    Join Orders On o_id = op_order_id
        Where o_delivery = 'No'
        Order By o_id, p_id;''')

    cursor.execute('''Create View If Not Exists Orders_Cost_Summary As
        Select o_id as 'ID Заказа', Sum(op_cost) as 'Суммарная стоимость заказа'
        From Orders Join Ordered_Products On o_id = op_order_id
        Group By o_id
        Order By o_id''')


    cursor.execute('''Create View If Not Exists Deliveries_Stat As
        Select d_id as 'ID Доставки', o_id as 'ID Заказа', d_deliverer_id as 'ID Доставщика', s_fullname as 'ФИО Доставщика', o_address as 'Адрес доставки'
        From Orders Join Deliveries On o_id = d_order_id
                    Join Stuff On s_id = d_deliverer_id
        Order By d_id''')

    #############################################################


    connection.close()