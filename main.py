import flet as ft
import sqlite3


def main(page: ft.Page):
    page.title = "IUVO"
    page.window_width = 1067  # window's width is 200 px
    page.window_height = 604  # window's height is 200 px
    page.window_resizable = False  # window is not resizable
    page.bgcolor = ft.colors.BLUE_GREY_900
    page.update()


#<==========================================================================>
#создание действий для каждой карточки

    dlg = ft.AlertDialog(
        title=ft.Text("Вам необходимо войти!"), on_dismiss=lambda e: print("Dialog dismissed!")
    )

    def open_dlg(e):
        page.dialog = dlg
        dlg.open = True
        page.update()



# <==========================================================================>
# <================карточки======================================>
# <================криптография==================================================>
    crypto_title = 'Криптография'
    crypto_description = 'Курс обучает шифрованию и алгоритмам безопасности, пригодным для успешного участия в соревнованиях по информационной безопасности.'
    progress = 0
    crypto_card = ft.Container(
            content=ft.Column([
                ft.Text(value=crypto_title, size=20, weight=ft.FontWeight.BOLD),
                ft.Text(value=crypto_description, size=15),
                ft.ProgressBar(value=progress, width=250),
                ft.Row([
                    ft.Text(value="Извините, вы еще не начали прохождение курсов, может, стоит начать?", size=10),
                    ft.Text(value=f"{progress}%", size=10, color=ft.colors.AMBER, weight=ft.FontWeight.BOLD),
                ], alignment=ft.alignment.center)
            ]),
            border_radius=20,
            padding=20,
            margin=10,
            width=500,
            height=200,
            bgcolor=ft.colors.BLUE,
            on_click=open_dlg,
        )

# <=====================веб-технологии==========================================>
    web_title = "Веб-технологии"
    web_description = 'Курс обучает шифрованию и алгоритмам безопасности, пригодным для успешного участия в соревнованиях по информационной безопасности.'
    progress = 0
    web_card = ft.Container(
            content=ft.Column([
                ft.Text(value=web_title, size=20, weight=ft.FontWeight.BOLD),
                ft.Text(value=web_description, size=15),
                ft.ProgressBar(value=progress, width=250),
                ft.Row([
                    ft.Text(value="Извините, вы еще не начали прохождение курсов, может, стоит начать?", size=10),
                    ft.Text(value=f"{progress}%", size=10, color=ft.colors.AMBER, weight=ft.FontWeight.BOLD),
                ], alignment=ft.alignment.center)
            ]),
            border_radius=20,
            padding=20,
            margin=10,
            width=500,
            height=200,
            bgcolor=ft.colors.BLUE,
            on_click=open_dlg,
        )

# <=====================osint==========================================>
    osint_title = "OSINT"
    osint_description = "Сбором и анализом информации из общественных источников занимается OSINT. В этом курсе мы рассказываем, как журналисты проводят расследования и можно ли вычислить человека по IP-адресу."
    progress = 0
    osint_card = ft.Container(
        content=ft.Column([
            ft.Text(value=osint_title, size=20, weight=ft.FontWeight.BOLD),
            ft.Text(value=osint_description, size=15),
            ft.ProgressBar(value=progress, width=250),
            ft.Row([
                ft.Text(value="Извините, вы еще не начали прохождение курсов, может, стоит начать?", size=10),
                ft.Text(value=f"{progress}%", size=10, color=ft.colors.AMBER, weight=ft.FontWeight.BOLD),
            ], alignment=ft.alignment.center)
        ]),
        border_radius=20,
        padding=20,
        margin=10,
        width=500,
        height=200,
        bgcolor=ft.colors.BLUE,
        on_click=open_dlg,
    )

# <=====================ctf==========================================>
    ctf_title = "CTF задачи"
    ctf_description = "CTF - Capture The Flag, вид соревнований в сфере информационной безопасности. В данной главе мы рассказываем, как подступиться к таким задачам, с чего начать, и кто такие 'флаги'."
    progress = 0
    ctf_card = ft.Container(
        content=ft.Column([
            ft.Text(value=ctf_title, size=20, weight=ft.FontWeight.BOLD),
            ft.Text(value=ctf_description, size=15),
            ft.ProgressBar(value=progress, width=250),
            ft.Row([
                ft.Text(value="Извините, вы еще не начали прохождение курсов, может, стоит начать?", size=10),
                ft.Text(value=f"{progress}%", size=10, color=ft.colors.AMBER, weight=ft.FontWeight.BOLD),
            ], alignment=ft.alignment.center)
        ]),
        border_radius=20,
        padding=20,
        margin=10,
        width=500,
        height=200,
        bgcolor=ft.colors.BLUE,
        on_click=open_dlg,
    )




    # def create_menu_item(text, icon_data):
    #     return ft.ListTile(
    #         leading=ft.Icon(icon_data),
    #         title=ft.Text(text),
    #         bgcolor=ft.colors.AMBER,
    #         bgcolor_activated=ft.colors.BROWN
    #     )

    # # Определение пунктов меню
    # menu_items = [
    #     ("Криптография", ft.icons.LOCK),
    #     ("Веб-технологии", ft.icons.WEB),
    #     ("OSINT", ft.icons.SEARCH),
    #     ("CTF задачи", ft.icons.FLAG),
    #     ("Основы Linux", ft.icons.COMPUTER),
    #     ("Hack The Box", ft.icons.SECURITY),
    #     ("Root me", ft.icons.TRENDING_UP),
    #     ("Pico CTF", ft.icons.GAMEPAD),
    #     ("Телеграмм", ft.icons.SEND),
    #     ("Чат курсов", ft.icons.CHAT),
    #     ("Группа VK", ft.icons.GROUP),
    # ]
    #
    #
    # # Функция для закрытия бокового меню
    # def close_sidebar(e):
    #     page.drawer = None
    #
    #
    #
    # close_button = ft.IconButton(icon=ft.icons.CLOSE, on_click=close_sidebar)
    # # Создание бокового меню
    # sidebar = ft.Column(
    #     [close_button, [create_menu_item(text, icon) for text, icon in menu_items]],
    #     width=250,
    #     # bgcolor=ft.colors.WHITE,
    # )
    #
    # # Функция для открытия бокового меню
    # def open_sidebar(e):
    #     page.drawer = sidebar
    #     page.update()

    # Подключение к базе данных (будет создан новый файл базы данных, если он не существует)
    conn = sqlite3.connect('users.db', check_same_thread=False)

    # Создание курсора
    cursor = conn.cursor()

    # Создание таблицы users, если она еще не существует
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            crypto_progress INTEGER DEFAULT 0,
            web_progress INTEGER DEFAULT 0,
            osint_progress INTEGER DEFAULT 0,
            ctf_progress INTEGER DEFAULT 0
        )
        ''')

    # Функция для регистрации нового пользователя
    def register_user(username, password):
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        try:
            cursor.execute('''
            INSERT INTO users (username, password, crypto_progress, web_progress, osint_progress, ctf_progress) 
            VALUES (?, ?, 0, 0, 0, 0)''', (username, password))
            conn.commit()
        except sqlite3.IntegrityError:
            conn.close()
            return False
        conn.close()
        return True

    # Функция для проверки учетных данных пользователя
    def check_login(username, password):
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT id, username, crypto_progress, web_progress, osint_progress, ctf_progress 
            FROM users WHERE username = ? AND password = ?''', (username, password))
        user = cursor.fetchone()
        conn.close()
        if user:
            # Возвращаем ID пользователя и его прогресс по разделам
            user_data = {
                'id': user[0],
                'username': user[1],
                'crypto_progress': user[2],
                'web_progress': user[3],
                'osint_progress': user[4],
                'ctf_progress': user[5],
            }
            return user_data
        return None


    # Проверка логина (вход)
    user_exists = check_login('testuser', 'testpass')
    print('Пользователь найден:', user_exists)

    # Закрытие соединения с базой данных
    conn.close()

    def show_registration_form(e):
        page.controls.clear()
        reg_login_field = ft.TextField(label="логин", autofocus=True)
        reg_password_field = ft.TextField(label="пароль", password=True)
        reg_button = ft.ElevatedButton(text="Зарегестрироваться", on_click=lambda _: register_user(reg_login_field.value, reg_password_field.value))
        back_button = ft.ElevatedButton(text="Назад", on_click=show_login_form)
        page.add(ft.Column([
            reg_login_field,
            reg_password_field,
            reg_button,
            back_button
        ], alignment=ft.MainAxisAlignment.CENTER))

        page.update()

    # Функция для отображения формы входа
    def show_login_form(e):
        page.controls.clear()
        login_field = ft.TextField(label="логин", autofocus=True)
        password_field = ft.TextField(label="пароль", password=True)
        login_button = ft.ElevatedButton(text="Войти", on_click=lambda _: login(login_field.value, password_field.value))
        registration_text = ft.Text("Вы здесь впервые? ")
        registration_link = ft.TextButton(text="регистрация", on_click=show_registration_form)
        page.add(ft.Column([
            login_field,
            password_field,
            login_button,
            ft.Row([registration_text, registration_link], alignment=ft.MainAxisAlignment.CENTER)
        ], alignment=ft.MainAxisAlignment.CENTER))
        page.update()








    # Функция для входа пользователя
    def login(username, password):
        global crypto_progress, web_progress, osint_progress, ctf_progress, current_username
        user_data = check_login(username, password)
        if user_data:
            # Данные пользователя успешно получены, присваиваем переменным
            crypto_progress = user_data['crypto_progress']
            web_progress = user_data['web_progress']
            osint_progress = user_data['osint_progress']
            ctf_progress = user_data['ctf_progress']
            page.controls.clear()
            page.add(ft.Text(f"Добро пожаловать, {username}!"))
            current_username = username
            registred_window(None)
            print(crypto_progress, web_progress)
            page.update()

            # Здесь может быть код для отображения пользовательского интерфейса личного кабинета...
        else:
            err_dlg = ft.AlertDialog(
                title=ft.Text("Ошибка!\nНеверный логин или пароль."), on_dismiss=lambda e: print("Dialog dismissed!")
            )
            page.dialog = err_dlg
            err_dlg.open = True
            page.update()
        conn.close()





    def menu(align: ft.MainAxisAlignment):
        return ft.Row([
            ft.IconButton(icon=ft.icons.MENU, tooltip="Меню"),
            # ft.Expanded(child=ft.TextField(placeholder="Поиск")),
            ft.IconButton(icon=ft.icons.SEARCH, tooltip="Поиск"),
            ft.Text("Последний таск", tooltip="Последний таск"),
            ft.IconButton(icon=ft.icons.HELP_OUTLINE, tooltip="FAQ"),
            ft.TextButton(text="Вход", on_click=show_login_form)
            ], width=page.window_width, alignment=align)

    page.add(menu(ft.MainAxisAlignment.SPACE_BETWEEN))




    # <================зарегестрированные=============================>
    # <================карточки======================================>
    # <================криптография==================================================>
    def reg_crypto_card(crypto_progress):
        crypto_title = 'Криптография'
        crypto_description = 'Курс обучает шифрованию и алгоритмам безопасности, пригодным для успешного участия в соревнованиях по информационной безопасности.'
        progress = crypto_progress
        if progress > 0:
            registred_crypto_card = ft.Container(
                content=ft.Column([
                    ft.Text(value=crypto_title, size=20, weight=ft.FontWeight.BOLD),
                    ft.Text(value=crypto_description, size=15),
                    ft.ProgressBar(value=progress * 0.01, width=250),
                    ft.Row([
                        ft.Text(value=f"{progress}%", size=10, color=ft.colors.AMBER, weight=ft.FontWeight.BOLD),
                    ], alignment=ft.alignment.center)
                ]),
                border_radius=20,
                padding=20,
                margin=10,
                width=500,
                height=200,
                bgcolor=ft.colors.BLUE,
                on_click=show_crypto_info,
            )
        else:
            registred_crypto_card = ft.Container(
                content=ft.Column([
                    ft.Text(value=crypto_title, size=20, weight=ft.FontWeight.BOLD),
                    ft.Text(value=crypto_description, size=15),
                    ft.ProgressBar(value=progress * 0.01, width=250),
                    ft.Row([
                        ft.Text(value="Извините, вы еще не начали прохождение курсов, может, стоит начать?", size=10),
                        ft.Text(value=f"{progress}%", size=10, color=ft.colors.AMBER, weight=ft.FontWeight.BOLD),
                    ], alignment=ft.alignment.center)
                ]),
                border_radius=20,
                padding=20,
                margin=10,
                width=500,
                height=200,
                bgcolor=ft.colors.BLUE,
                on_click=show_crypto_info,
            )
        return registred_crypto_card

    # <=====================веб-технологии==========================================>
    def reg_web_card(web_progress):
        web_title = "Веб-технологии"
        web_description = 'Курс обучает шифрованию и алгоритмам безопасности, пригодным для успешного участия в соревнованиях по информационной безопасности.'
        progress = web_progress
        if progress > 0:
            registred_web_card = ft.Container(
                content=ft.Column([
                    ft.Text(value=web_title, size=20, weight=ft.FontWeight.BOLD),
                    ft.Text(value=web_description, size=15),
                    ft.ProgressBar(value=progress * 0.01, width=250),
                    ft.Row([
                        ft.Text(value=f"{progress}%", size=10, color=ft.colors.AMBER, weight=ft.FontWeight.BOLD),
                    ], alignment=ft.alignment.center)
                ]),
                border_radius=20,
                padding=20,
                margin=10,
                width=500,
                height=200,
                bgcolor=ft.colors.BLUE,
                #on_click=web_card_clicked,
            )
        else:
            registred_web_card = ft.Container(
                content=ft.Column([
                    ft.Text(value=web_title, size=20, weight=ft.FontWeight.BOLD),
                    ft.Text(value=web_description, size=15),
                    ft.ProgressBar(value=progress * 0.01, width=250),
                    ft.Row([
                        ft.Text(value="Извините, вы еще не начали прохождение курсов, может, стоит начать?", size=10),
                        ft.Text(value=f"{progress}%", size=10, color=ft.colors.AMBER, weight=ft.FontWeight.BOLD),
                    ], alignment=ft.alignment.center)
                ]),
                border_radius=20,
                padding=20,
                margin=10,
                width=500,
                height=200,
                bgcolor=ft.colors.BLUE,
                #on_click=web_card_clicked,
            )

        return registred_web_card
    # <=====================osint==========================================>
    def reg_osint_card(osint_progress):
        osint_title = "OSINT"
        osint_description = "Сбором и анализом информации из общественных источников занимается OSINT. В этом курсе мы рассказываем, как журналисты проводят расследования и можно ли вычислить человека по IP-адресу."
        progress = osint_progress
        if progress > 0:
            registred_osint_card = ft.Container(
                content=ft.Column([
                    ft.Text(value=osint_title, size=20, weight=ft.FontWeight.BOLD),
                    ft.Text(value=osint_description, size=15),
                    ft.ProgressBar(value=progress * 0.01, width=250),
                    ft.Row([
                        ft.Text(value=f"{progress}%", size=10, color=ft.colors.AMBER, weight=ft.FontWeight.BOLD),
                    ], alignment=ft.alignment.center)
                ]),
                border_radius=20,
                padding=20,
                margin=10,
                width=500,
                height=200,
                bgcolor=ft.colors.BLUE,
                #on_click=osint_card_clicked,
            )
        else:
            registred_osint_card = ft.Container(
                content=ft.Column([
                    ft.Text(value=osint_title, size=20, weight=ft.FontWeight.BOLD),
                    ft.Text(value=osint_description, size=15),
                    ft.ProgressBar(value=progress * 0.01, width=250),
                    ft.Row([
                        ft.Text(value="Извините, вы еще не начали прохождение курсов, может, стоит начать?", size=10),
                        ft.Text(value=f"{progress}%", size=10, color=ft.colors.AMBER, weight=ft.FontWeight.BOLD),
                    ], alignment=ft.alignment.center)
                ]),
                border_radius=20,
                padding=20,
                margin=10,
                width=500,
                height=200,
                bgcolor=ft.colors.BLUE,
                # on_click=osint_card_clicked,
            )
        return registred_osint_card
    # <=====================ctf==========================================>
    def reg_ctf_card(ctf_progress):
        ctf_title = "CTF задачи"
        ctf_description = "CTF - Capture The Flag, вид соревнований в сфере информационной безопасности. В данной главе мы рассказываем, как подступиться к таким задачам, с чего начать, и кто такие 'флаги'."
        progress = ctf_progress
        if progress > 0:
            registred_ctf_card = ft.Container(
                content=ft.Column([
                    ft.Text(value=ctf_title, size=20, weight=ft.FontWeight.BOLD),
                    ft.Text(value=ctf_description, size=15),
                    ft.ProgressBar(value=progress * 0.01, width=250),
                    ft.Row([
                        ft.Text(value=f"{progress}%", size=10, color=ft.colors.AMBER, weight=ft.FontWeight.BOLD),
                    ], alignment=ft.alignment.center)
                ]),
                border_radius=20,
                padding=20,
                margin=10,
                width=500,
                height=200,
                bgcolor=ft.colors.BLUE,
                #on_click=ctf_card_clicked,
            )
        else:
            registred_ctf_card = ft.Container(
                content=ft.Column([
                    ft.Text(value=ctf_title, size=20, weight=ft.FontWeight.BOLD),
                    ft.Text(value=ctf_description, size=15),
                    ft.ProgressBar(value=progress * 0.01, width=250),
                    ft.Row([
                        ft.Text(value="Извините, вы еще не начали прохождение курсов, может, стоит начать?", size=10),
                        ft.Text(value=f"{progress}%", size=10, color=ft.colors.AMBER, weight=ft.FontWeight.BOLD),
                    ], alignment=ft.alignment.center)
                ]),
                border_radius=20,
                padding=20,
                margin=10,
                width=500,
                height=200,
                bgcolor=ft.colors.BLUE,
                # on_click=ctf_card_clicked,
            )

        return registred_ctf_card














    first_row = ft.Row([crypto_card,web_card])
    second_row = ft.Row([osint_card, ctf_card])
    grid = ft.Column([first_row, second_row])
    page.add(grid)

    def unlogin(e):
        global current_username
        page.controls.clear()
        page.add(menu(ft.MainAxisAlignment.SPACE_BETWEEN))
        current_username = ''
        page.add(grid)
        page.update()

    def reg_menu(align: ft.MainAxisAlignment):
        return ft.Row([
            ft.IconButton(icon=ft.icons.MENU, tooltip="Меню"),
            # ft.Expanded(child=ft.TextField(placeholder="Поиск")),
            ft.IconButton(icon=ft.icons.SEARCH, tooltip="Поиск"),
            ft.Text("Последний таск", tooltip="Последний таск"),
            ft.IconButton(icon=ft.icons.HELP_OUTLINE, tooltip="FAQ"),
            ft.TextButton(text="Выйти", on_click=unlogin)
            ], width=page.window_width, alignment=ft.MainAxisAlignment.SPACE_BETWEEN)


    def registred_window(e):
        page.controls.clear()
        page.add(reg_menu(ft.MainAxisAlignment.SPACE_BETWEEN))
        registred_first_row = ft.Row([reg_crypto_card(crypto_progress), reg_web_card(web_progress)])
        registred_second_row = ft.Row([reg_osint_card(osint_progress), reg_ctf_card(ctf_progress)])
        registred_grid = ft.Column([registred_first_row, registred_second_row])
        page.add(registred_grid)
        page.update()


    def update_crypto_progress(username, new_progress):
        """
        Обновляет прогресс пользователя в области криптографии.

        :param username: Логин пользователя.
        :param new_progress: Новое значение прогресса.
        """
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('''
        UPDATE users SET crypto_progress = ? WHERE username = ?''', (new_progress, username))
        conn.commit()
        conn.close()


#Первое задание
    right_dlg = ft.AlertDialog(
        title=ft.Text("Поздравляем!\nФлаг верный."), on_dismiss=lambda e: print("Dialog dismissed!"),
    )

    def open_right_dlg(e):
        page.dialog = right_dlg
        right_dlg.open = True
        page.update()


    wrong_dlg = ft.AlertDialog(
        title=ft.Text("Неправильный флаг."), on_dismiss=lambda e: print("Dialog dismissed!")
    )

    def open_wrong_dlg(e):
        page.dialog = wrong_dlg
        wrong_dlg.open = True
        page.update()


    correct_flag = "iuvo{is_that_so_based}"

    # Функция для проверки флага
    def check_flag(e):
        global crypto_progress
        if flag_input.value == correct_flag:
            open_right_dlg(None)
            update_crypto_progress(current_username, 75)
            crypto_progress = 75
        else:
            open_wrong_dlg(None)



    flag_input = ft.TextField(label="Введите ваш флаг", autofocus=True)
    submit_button = ft.ElevatedButton(text="Отправить", on_click=check_flag)
    practice_area = ft.Column([
        ft.Text("Лунной астрономической базе внезапно передали сигнал, явстевнно услышанный всеми астронавтами. Космонавт Федор успел его записать. Помогите ему найти источник."),
        ft.Text("61 58 56 32 62 33 74 70 63 31 39 30 61 47 46 30 58 33 4e 76 58 32 4a 68 63 32 56 6b 66 51 3d 3d", selectable=True),
        ft.Text("Флаг имеет вид iuvo{flag}", size=10),
        ft.Text("Введите флаг, полученный после расшифровки сообщения:"),
        flag_input,
        submit_button
    ])



    # Функции для навигации по разделам криптографии
    def show_history(e):
        text_history.value = history_text
        page.update()

    def show_theory(e):
        text_history.value = theory_text
        page.update()

    def show_practice(e):
        page.controls.clear()
        page.add(ft.ElevatedButton(text="Назад", on_click=show_crypto_info))
        page.add(practice_area)
        page.update()

    # Текст истории криптографии
    history_text = open('crypto_history.txt', 'r')
    history_text = history_text.read()


    theory_text = open('crypto_theory.txt', 'r')
    theory_text = theory_text.read()

    # Создание бокового меню для раздела криптографии
    def create_crypto_sidebar():
        return ft.Column([
            ft.ElevatedButton(text="История", on_click=show_history),
            ft.ElevatedButton(text="Теория", on_click=show_theory),
            ft.ElevatedButton(text="Практика", on_click=show_practice),
            ft.ElevatedButton(text="Назад", on_click=registred_window),
        ], width=200)

    # Виджет для отображения информации
    text_history = ft.Text(value=history_text, selectable=True)

    scroll_view = ft.ListView(height=500, width=700, padding=20)
    scroll_view.controls.append(text_history)



    # Функция для показа информации о криптографии
    def show_crypto_info(e):
        page.controls.clear()
        sidebar = create_crypto_sidebar()
        page.add(ft.Row([sidebar, scroll_view]))
        show_history(None)  # Показываем историю по умолчанию
        page.update()



ft.app(target=main)


