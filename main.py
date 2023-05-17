import tkinter as tk
import tkinter.font as tkfont
import re

from DBMS import print_tables, create, triggers, views, insert, queries
import messages


############ Общеоконные параметры ############

root = tk.Tk()

root.geometry("1200x900")

root.configure(bg='#444444')

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

font = tkfont.Font(size=20)

#############################################################


############ Очистка окна ############

def clean_window(window):

    for widget in window.winfo_children():
        widget.destroy()
        
#############################################################


############ Перезапуск базы данных ############

def restart_db():

    clean_window(root)

    create.create_db()
    triggers.create_triggers()
    views.create_views()
    insert.insert_massive()

    label = tk.Label(root, text="База данных перезапущенна", font=font, bg='white')
    label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    root.after(5000, main)

#############################################################


############ Ветка окон для вставок ############

def parse_entry(value):
    
    regexp = r'''(?:(?:"([^"]*)")|(?:'([^']*)')|\S+)'''
    
    data = value.split(',')
    
    result = []
    
    for elem in data:
        
        row = re.findall(regexp, elem)
        
        result.append(tuple(' '.join(token) for token in row))
        
    return result


def inser_to_table(table_name):

    insert_window = tk.Tk()

    insert_window.geometry("1200x1000")
    insert_window.configure(bg='#444444')

    insert_window.columnconfigure(0, weight=1)
    insert_window.rowconfigure(0, weight=1)

    function = getattr(insert, 'insert_' + table_name)
    message = messages.messages[table_name + '_message']

    label = tk.Label(insert_window, text=message, font=font, bg='white', width=20, height=5)
    label.grid(row=0, column=0, sticky="nsew", padx=int(0.03 * 1200), pady=int(0.02 * 900))

    entry = tk.Entry(insert_window, bg='white')
    entry.configure(width=20, font=20)
    entry.grid(row=1, column=0, sticky="nsew", padx=int(0.02 * 1200), pady=int(0.01 * 900))

    submit_button = tk.Button(insert_window, text="Выполнить вставку", command=lambda: function(parse_entry(entry.get())), font=font, bg='white', width=20, height=3)
    submit_button.grid(row=2, sticky="nsew", column=0, padx=int(0.03 * 1200), pady=int(0.02 * 900))


def switch_to_insertions():

    clean_window(root)
    
    products_insert_button = tk.Button(root, text="Вставка в таблицу Products", command=lambda: inser_to_table('products'), font=font, bg='white', width=20, height=3)
    products_insert_button.grid(row=0, column=0, sticky="nsew", padx=int(0.03 * 1200), pady=int(0.02 * 900))

    stuff_insert_button = tk.Button(root, text="Вставка в таблицу Stuff", command=lambda: inser_to_table('stuff'), font=font, bg='white', width=20, height=3)
    stuff_insert_button.grid(row=1, column=0, sticky="nsew", padx=int(0.03 * 1200), pady=int(0.02 * 900))

    orders_insert_button = tk.Button(root, text="Вставка в таблицу Orders", command=lambda: inser_to_table('orders'), font=font, bg='white', width=20, height=3)
    orders_insert_button.grid(row=2, column=0, sticky="nsew", padx=int(0.03 * 1200), pady=int(0.02 * 900))

    op_insert_button = tk.Button(root, text="Вставка в таблицу Ordered_Products", command=lambda: inser_to_table('op'), font=font, bg='white', width=20, height=3)
    op_insert_button.grid(row=3, column=0, sticky="nsew", padx=int(0.03 * 1200), pady=int(0.02 * 900))

    deliveries_insert_button = tk.Button(root, text="Вставка в таблицу Deliveries", command=lambda: inser_to_table('deliveries'), font=font, bg='white', width=20, height=3)
    deliveries_insert_button.grid(row=4, column=0, sticky="nsew", padx=int(0.03 * 1200), pady=int(0.02 * 900))

    back_button = tk.Button(root, text="Перейти назад", command=main, font=font, bg='white', width=20, height=3)
    back_button.grid(row=5, column=0, sticky="nsew", padx=int(0.03 * 1200), pady=int(0.02 * 900))

#############################################################


############ Ветка окон для выборок ############

############ Печать таблиц ############

def print_all():
    
    tables = print_tables.get_tables()
    
    print_window = tk.Tk()
    
    print_window.geometry("1500x1000")

    print_window.configure(bg='#444444')
    
    text_widget = tk.Text(print_window)
    text_widget.pack(fill=tk.BOTH, expand=True)
    
    for key in tables:
        
        text_widget.insert(tk.END, tables[key])


def print_table(table_name):
    
    table = print_tables.return_optional(table_name)
    
    print_window = tk.Tk()
    
    print_window.geometry("1500x1000")

    print_window.configure(bg='#444444')
    
    text_widget = tk.Text(print_window)
    text_widget.pack(fill=tk.BOTH, expand=True)

    text_widget.insert(tk.END, table)


def switch_to_prints():
    
    clean_window(root)
    
    prints_all_button = tk.Button(root, text="Напечатать все таблицы", command=print_all, font=font, bg='white', width=20, height=2)
    prints_all_button.grid(row=0, column=0, sticky="nsew", padx=int(0.03 * 1200), pady=int(0.01 * 900))
    
    print_products_button = tk.Button(root, text="Напечатать таблицу Products", command=lambda: print_table('Products'), font=font, bg='white', width=20, height=2)
    print_products_button.grid(row=1, column=0, sticky="nsew", padx=int(0.03 * 1200), pady=int(0.01 * 900))
    
    print_stuff_button = tk.Button(root, text="Напечатать таблицу Stuff", command=lambda: print_table('Stuff'), font=font, bg='white', width=20, height=2)
    print_stuff_button.grid(row=2, column=0, sticky="nsew", padx=int(0.03 * 1200), pady=int(0.01 * 900))
    
    print_orders_button = tk.Button(root, text="Напечатать таблицу Orders", command=lambda: print_table('Orders'), font=font, bg='white', width=20, height=2)
    print_orders_button.grid(row=3, column=0, sticky="nsew", padx=int(0.03 * 1200), pady=int(0.01 * 900))
    
    print_op_button = tk.Button(root, text="Напечатать таблицу Ordered_Products", command=lambda: print_table('OP'), font=font, bg='white', width=20, height=2)
    print_op_button.grid(row=4, column=0, sticky="nsew", padx=int(0.03 * 1200), pady=int(0.01 * 900))
    
    print_deliveries_button = tk.Button(root, text="Напечатать таблицу Deliveries", command=lambda: print_table('Deliveries'), font=font, bg='white', width=20, height=2)
    print_deliveries_button.grid(row=5, column=0, sticky="nsew", padx=int(0.03 * 1200), pady=int(0.01 * 900))
    
    print_pl_button = tk.Button(root, text="Напечатать таблицу Products_Log", command=lambda: print_table('PL'), font=font, bg='white', width=20, height=2)
    print_pl_button.grid(row=6, column=0, sticky="nsew", padx=int(0.03 * 1200), pady=int(0.01 * 900))
    
    print_sl_button = tk.Button(root, text="Напечатать таблицу Stuff_Log", command=lambda: print_table('SL'), font=font, bg='white', width=20, height=2)
    print_sl_button.grid(row=7, column=0, sticky="nsew", padx=int(0.03 * 1200), pady=int(0.01 * 900))
    
    back_button = tk.Button(root, text="Перейти назад", command=switch_to_selections, font=font, bg='white')
    back_button.grid(row=8, column=0, sticky="nsew", padx=int(0.03 * 1200), pady=int(0.01 * 900))

#############################################################


############ Запросы в базу данных ############

def print_result(function, id):

    table = function(id)

    print_window = tk.Tk()
    
    print_window.geometry("1200x800")

    print_window.configure(bg='#444444')
    
    text_widget = tk.Text(print_window)
    text_widget.pack(fill=tk.BOTH, expand=True)

    text_widget.insert(tk.END, table)


def execute_query(query):

    clean_window(root)

    function = getattr(queries, query)

    label = tk.Label(root, text='Введите ID для запроса', font=font, bg='white', width=100, height=5)
    label.grid(row=0, column=0, columnspan=2, padx=int(0.03 * 1200), pady=int(0.02 * 900))

    entry = tk.Entry(root, bg='white')
    entry.configure(width=40, font=50)
    entry.grid(row=1, column=0, padx=int(0.03 * 1200), pady=int(0.02 * 900))

    submit_button = tk.Button(root, text="Выполнить запрос", command=lambda: print_result(function, entry.get()), font=font, bg='white', width=30, height=3)
    submit_button.grid(row=1, column=1, padx=int(0.03 * 1200), pady=int(0.02 * 900))

    back_button = tk.Button(root, text="Вернуться назад", command=switch_to_queries, font=font, bg='white', width=20, height=2)
    back_button.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=int(0.03 * 1200), pady=int(0.02 * 900))


def switch_to_queries():

    clean_window(root)

    deliverer_print_button = tk.Button(root, text="Запрос на вывод доставщика", command=lambda: execute_query('print_deliverer_stat'), font=font, bg='white', width=20, height=3)
    deliverer_print_button.grid(row=0, column=0, sticky="nsew", padx=int(0.03 * 1200), pady=int(0.02 * 900))

    product_print_button = tk.Button(root, text="Запрос на вывод истории продукта", command=lambda: execute_query('print_product_history'), font=font, bg='white', width=20, height=3)
    product_print_button.grid(row=1, column=0, sticky="nsew", padx=int(0.03 * 1200), pady=int(0.02 * 900))

    employee_print_button = tk.Button(root, text="Запрос на вывод истории работника", command=lambda: execute_query('print_employee_history'), font=font, bg='white', width=20, height=3)
    employee_print_button.grid(row=2, column=0, sticky="nsew", padx=int(0.03 * 1200), pady=int(0.02 * 900))

    order_print_button = tk.Button(root, text="Запрос на вывод заказа", command=lambda: execute_query('print_order_stat'), font=font, bg='white', width=20, height=3)
    order_print_button.grid(row=3, column=0, sticky="nsew", padx=int(0.03 * 1200), pady=int(0.02 * 900))

    delivery_print_button = tk.Button(root, text="Запрос на вывод доставки", command=lambda: execute_query('print_delivery_stat'), font=font, bg='white', width=20, height=3)
    delivery_print_button.grid(row=4, column=0, sticky="nsew", padx=int(0.03 * 1200), pady=int(0.02 * 900))

    back_button = tk.Button(root, text="Перейти назад", command=switch_to_selections, font=font, bg='white', width=20, height=3)
    back_button.grid(row=5, column=0, sticky="nsew", padx=int(0.03 * 1200), pady=int(0.02 * 900))

#############################################################


def switch_to_selections():
    
    clean_window(root)
    
    prints_button = tk.Button(root, text="Перейти к выводу данных из таблицы", command=switch_to_prints, font=font, bg='white')
    prints_button.grid(row=0, column=0, sticky="nsew", padx=int(0.03 * 1200), pady=int(0.04 * 900))
    
    select_button = tk.Button(root, text="Перейти к запросам на вывод", command=switch_to_queries, font=font, bg='white')
    select_button.grid(row=1, column=0, sticky="nsew", padx=int(0.03 * 1200), pady=int(0.04 * 900))
    
    back_button = tk.Button(root, text="Перейти назад", command=main, font=font, bg='white')
    back_button.grid(row=2, column=0, sticky="nsew", padx=int(0.03 * 1200), pady=int(0.04 * 900))

#############################################################


def main():

    clean_window(root)

    insert_button = tk.Button(root, text="Перейти к разделу вставок", command=switch_to_insertions, font=font, bg='white')
    insert_button.grid(row=0, column=0, sticky="nsew", padx=int(0.03 * 1200), pady=int(0.04 * 900))

    select_button = tk.Button(root, text="Перейти к разделу выборок", command=switch_to_selections, font=font, bg='white')
    select_button.grid(row=1, column=0, sticky="nsew", padx=int(0.03 * 1200), pady=int(0.04 * 900))

    restart_button = tk.Button(root, text="Перезапустить базу данных", command=restart_db, font=font, bg='white')
    restart_button.grid(row=2, column=0, sticky="nsew", padx=int(0.03 * 1200), pady=int(0.04 * 900))

    root.mainloop()


if __name__ == '__main__':
    
    main()