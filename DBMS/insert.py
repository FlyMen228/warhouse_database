import sqlite3


current_time = "2023-05-06 20:00:00" # Дата и время для быстроты ввода


############ Функции вставок данных в отдельные таблицы ############

def insert_products(rows):

    connection = sqlite3.connect('Warhouse.sqlite')

    cursor = connection.cursor()

    cursor.executemany('''Insert Into Products (p_name, p_quantity, p_price, p_stock_status, p_orders, p_sales, p_time_in_stock, p_supply_date) Values (?, ?, ?, ?, ?, ?, ?, ?)''', rows)

    connection.commit()

    connection.close()


def insert_stuff(rows):

    connection = sqlite3.connect('Warhouse.sqlite')

    cursor = connection.cursor()

    cursor.executemany('''Insert Into Stuff (s_fullname, s_role, s_phone) Values (?, ?, ?)''', rows)

    connection.commit()

    connection.close()


def insert_orders(rows):

    connection = sqlite3.connect('Warhouse.sqlite')

    cursor = connection.cursor()

    cursor.executemany('''Insert Into Orders (o_delivery, o_address) Values (?, ?)''', rows)

    connection.commit()

    connection.close()    


def insert_op(rows):

    connection = sqlite3.connect('Warhouse.sqlite')

    cursor = connection.cursor()

    cursor.executemany('''Insert Into Ordered_Products (op_product_id, op_order_id, op_quantity) Values (?, ?, ?)''', rows)

    connection.commit()

    connection.close()
   
   
def insert_deliveries(rows):

    connection = sqlite3.connect('Warhouse.sqlite')

    cursor = connection.cursor()

    cursor.executemany('''Insert Into Deliveries (d_order_id, d_deliverer_id) Values (?, ?)''', rows)

    connection.commit()

    connection.close()

#############################################################


############ Начальное заполнение таблиц ############

def insert_massive():

    connection = sqlite3.connect('Warhouse.sqlite')

    cursor = connection.cursor()

    ############ Блок очистки таблиц перед вставками ############

    cursor.execute('Delete From Products')
    connection.commit()

    cursor.execute('Delete From Stuff')
    connection.commit()

    cursor.execute('Delete From Orders')
    connection.commit()

    cursor.execute('Delete From Ordered_Products')
    connection.commit()

    cursor.execute('Delete From Deliveries')
    connection.commit()

    cursor.execute('Delete From Products_log')
    connection.commit()

    cursor.execute('Delete From Stuff_log')
    connection.commit()

    #############################################################

    connection.close()


    ############ Блок вставок ############

    productsArr = [
        ("Дезодорант 'Stay Fresh' Rexona", 1101, 399, 35, 50, 3000, 14, current_time),
        ("Дезодорант 'Captain' Old Spice", 989, 299, 20, 20, 2500, 6, current_time),
        ("Крем-гель для умывания 'Красота и Здоровье' Nivea", 0, 430, 0, 0, 0, None, None),
        ("Дезодорант 'Сухость Пудры' Rexona", 531, 349, 10, 20, 2365, 6, current_time),
        ("Лосьон 'Ромашка Био' Yves Rocher", 165, 399, 20, 65, 2119, 27, current_time),
        ("Гель для душа 'Аромат дерева' Nivea", 3011, 279, 48, 20, 2500, 6, current_time),
        ("Шампунь 'Освежение' Head & Shoulders", 8670, 190, 80, 20, 3500, 13, current_time),
        ("Маска для волос 'Сила и блеск' L'Oreal", 454, 310, 61, 20, 1511, 2, current_time),
        ("Маска для волос 'Роскошь' Schwarzkopf ", 0, 899, 0, 0, 0, None, None),
        ("Крем для лица 'Увлажнение и защита' Rexona", 76, 420, 54, 20, 1142, 21, current_time),
        ("Гель для бритья 'Свежесть и защита' Gillette", 820, 290, 36, 20, 2500, 11, current_time),
        ("Пена для бритья 'Чистая кожа' Nivea Men", 2316, 179, 20, 40, 4845, 16, current_time),
        ("Гель для бритья 'Гладкость и уход' L'Oreal Men Expert", 2521, 220, 81, 20, 3134, 5, current_time),
        ("Крем для рук 'Бережный уход' Dove", 4561, 179, 26, 20, 2500, 21, current_time),
        ("Крем для тела 'Шелковистая кожа' Nivea", 2870, 250, 10, 20, 4511, 25, current_time),
        ("Дезодорант 'Шоколад' AXE", 1391, 290, 20, 76, 3149, 6, current_time),
        ("Жидкое мыло 'Травяной аромат' Fa", 4591, 119, 41, 20, 4923, 12, current_time),
        ("Гель для умывания 'Очищение и тонизирование' Garnier", 1382, 289, 17, 20, 2200, 8, current_time),
        ("Лосьон для тела 'Увлажнение и питание' Nivea", 766, 319, 79, 20, 2006, 19, current_time),
        ("Средство для снятия макияжа 'Нежность и забота' L'Oreal", 632, 280, 81, 20, 3761, 6, current_time),
        ("Скраб для тела 'Мягкий уход' Palmolive", 0, 180, 0, 0, 0, None, None),
    ]

    insert_products(productsArr)


    stuffArr = [
        #Руководство
        ("Абрамзон А.А.", "DB_admin", "111-111"),
        ("Шакиров Д.И.", "Director", "222-222"),
        ("Макарова К.А", "Associate Director", "333-333"),
        ("Конякин К.А", "Admin", "444-444"),
        #Логистика
        ("Самсонов И.Д.", "Logistician", "100-100"),
        ("Медведева Т.Ю.", "Logistician", "101-101"),
        ("Баранов Г.М.", "Logistician", "102-102"),
        #Доставка
        ("Тимофеев М.В.", "Deliverer", "000-001"),
        ("Романов М.В.", "Deliverer", "000-002"),
        ("Третьяков И.Е.", "Deliverer", "000-003"),
        ("Филиппов И.А.", "Deliverer", "000-004"),
        ("Александров Д.Г.", "Deliverer", "000-005"),
        #Кладовщики
        ("Ершова Е.В.", "Storekeeper", "000-100"),
        #Грузчики
        ("Сергеев Е.С.", "Movers", "000-010"),
        ("Соколов А.В.", "Movers", "000-020"),
        ("Баранов Г.М.", "Movers", "000-030"),
        ("Ковалев С.В.", "Movers", "000-040"),
        ("Смирнов О.П.", "Movers", "000-050"),
        #Сортировщики
        ("Сергеев Е.С.", "Sorters", "001-001"),
        ("Соколов А.В.", "Sorters", "002-002"),
    ]

    insert_stuff(stuffArr)


    ordersArr = [
        ("Yes", "г. Челябинск, ул. Б. Кашириных 129"),
        ("Yes", "г. Санкт-Петербург, ул. Исаакиевская площадь 4"),
        ("Yes", "г. Санкт-Петербург, ул. Невский проспект 22"),
        ("Yes", "г. Москва, ул. Кузнецова 12"),
        ("Yes", "г. Тверь, пер. Набережный 30"),
        ("No", None),
        ("Yes", "г. Новосибирск, ул. Южная 6"),
        ("Yes", "г. Екатеринбург, пер. Набережный 30"),
        ("Yes", "г. Омск, Ленина 128"),
        ("Yes", "г. Самара, ул. Ленина 66"),
        ("No", None),
        ("Yes", "г. Магнитогорск, ул. Комсомольская 7"),
        ("No", None),
        ("Yes", "г. Курск, ул. Ленина 45"),
        ("Yes", "г. Тюмень, ул. Мельникайте 32"),
        ("Yes", "г. Кемерово, ул. Советская 34"),
        ("Yes", "г. Ярославль, ул. Советская 15"),
        ("Yes", "г. Казань, ул. Пушкина 25"),
        ("Yes", "г. Магнитогорск, ул. Строителей 48"),
        ("Yes", "г. Челябинск, ул. Гагарина 7"),
        ("Yes", "г. Москва, ул. Ленина 5")
    ]

    insert_orders(ordersArr)


    opArr = [
        (1, 1, 20), 
        (2, 1, 21),
        
        (4, 2, 31), 
        (5, 2, 36),

        (6, 3, 24),
        (7, 3, 39),

        (8, 4, 27),
        (10, 4, 22),

        (11, 5, 21),
        (12, 5, 18),

        (13, 6, 37),
        (14, 6, 34),

        (15, 7, 25),
        (16, 7, 41),

        (17, 8, 24),
        (18, 8, 32),

        (19, 9, 20),
        (1, 9, 37),

        (2, 10, 32),
        (4, 10, 45),

        (5, 11, 29),
        (6, 11, 31),

        (7, 12, 47),
        (8, 13, 38),

        (10, 14, 17),
        (11, 14, 22),

        (12, 15, 36),
        (13, 15, 28),

        (14, 16, 35),
        (15, 16, 25),

        (16, 17, 30),
        (17, 18, 20),

        (18, 19, 11),
        (19, 19, 29),

        (1, 20, 10),
        (2, 20, 30),

        (4, 21, 30),
        (5, 21, 20),

    ]

    insert_op(opArr)


    deliveriesArr = [
        (1, 8),
        (2, 10),
        (3, 12),
        (4, 11),
        (5, 9),
        (7, 8),
        (8, 9),
        (9, 10),
        (10, 11),
        (12, 8),
        (14, 9),
        (15, 11),
        (16, 10),
        (17, 8),
        (18, 12),
    ]

    insert_deliveries(deliveriesArr)
    
#############################################################