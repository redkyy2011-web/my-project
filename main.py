from milioner import *
import sys
import random

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

# Вопросы
v = {
    '1': ('Венера','Марс','Меркурий','Земля','Какая планета ближе всего к Солнцу','Меркурий'),
    '2': ('364','365','366','367','Сколько дней в високосном году?','366'),
    '3': ('Слон','Синий кит','Жираф','Носорог','Как называется самое большое млекопитающее на Земле?','Синий кит'),
    '4': ('Фёдор Достоевский','Александр Пушкин','Лев Толстой','Антон Чехов','Кто написал роман «Война и мир»?','Лев Толстой'),
    '5': ('Азот','Кислород','Углекислый газ','Водород','Какой газ необходим человеку для дыхания?','Кислород'),
    '6': ('1957','1961','1965','1970','В каком году человек впервые полетел в космос?','1961'),
    '7': ('Амазонка','Нил','Янцзы','Миссисипи','Как называется самая длинная река в мире?','Нил'),
    '8': ('5','6','7','8','Сколько континентов на Земле?','7'),
    '9': ('Египет','Китай','Греция','Индия','Какая страна изобрела бумагу?','Китай'),
    '10': ('Фтор','Железо','Фосфор','Франций','Какой элемент имеет химический символ Fe?','Железо'),
    '11': ('Авраам Линкольн','Джон Адамс','Джордж Вашингтон','Томас Джефферсон','Кто был первым президентом США?','Джордж Вашингтон'),
    '12': ('2,14','3,14','4,13','3,41','Как называется число π примерно?','3,14'),
    '13': ('1939','1941','1945','1933','В каком году началась Вторая мировая война?','1939'),
    '14': ('США','Индия','Китай','Индонезия','Какая страна имеет наибольшее население в мире\n(по состоянию на последние годы)?','Китай'),
    '15': ('К2','Эльбрус','Джомолунгма','Канченджанга','Как называется самая высокая гора в мире над уровнем моря?','Джомолунгма'),
    '16': ('31 февраля','Деление на ноль','Ход назад во времени','Квадратный круг','Что из этого невозможно?','Квадратный круг')
}


rn_k = 1  # текущий вопрос
rn_n = 1
vo = None
co = None
a = []  # текущие варианты ответов
lb_m = 0

def c_o(o=None):
    global rn_k, vo, co, a, v, lb_m, rn_n

    # Проверяем ответ, если o не None
    if o is not None:
        if str(o) == str(co):
            # Правильный ответ → идём к следующему вопросу
            rn_k += 1
            if rn_k > len(v):
                rn_k = len(v)  # останавливаться на последнем вопросе
                return
            # Загружаем следующий вопрос
            data = v[str(rn_k)]
            vo = data[4]
            co = data[5]
            a = list(data[:4])
            random.shuffle(a)
            if rn_k == 2:
                lb_m += 500
                ui.label_2.setText(f'Money: {str(lb_m)}$')
            elif rn_k <= 3:
                lb_m += 500
                ui.label_2.setText(f'Money: {str(lb_m)}$')
            elif rn_k <= 5:
                lb_m += 1000
                ui.label_2.setText(f'Money: {str(lb_m)}$')
            elif rn_k == 6:
                lb_m += 2000
                ui.label_2.setText(f'Money: {str(lb_m)}$')
            elif rn_k <= 8:
                lb_m += 5000
                ui.label_2.setText(f'Money: {str(lb_m)}$')

            elif rn_k == 9:
                lb_m += 10000 #25,000
                ui.label_2.setText(f'Money: {str(lb_m)}$')

            elif rn_k == 10:
                lb_m += 25000 #50,000
                ui.label_2.setText(f'Money: {str(lb_m)}$')

            elif rn_k == 11:
                lb_m += 50000 #100,000
                ui.label_2.setText(f'Money: {str(lb_m)}$')

            elif rn_k == 12:
                lb_m += 100000  #200,000
                ui.label_2.setText(f'Money: {str(lb_m)}$')

            elif rn_k == 13:
                lb_m += 200000 #400,000
                ui.label_2.setText(f'Money: {str(lb_m)}$')

            elif rn_k == 14:
                lb_m += 400000 #800,000
                ui.label_2.setText(f'Money: {str(lb_m)}$')

            elif rn_k == 15:
                lb_m += 700000 # 1,500,000
                ui.label_2.setText(f'Money: {str(lb_m)}$')

            elif rn_k == 16:
                lb_m += 1500000  # 3,000,000
                ui.label_2.setText(f'Money: {str(lb_m)}$')

            if rn_k == 6:
                ui.label_5.setText(f'Сложность: Нормальная')
            if rn_k == 11:
                ui.label_5.setText(f'Сложность: Тяжело')
            if rn_k == 16:
                ui.label_5.setText(f'Сложность: Невозможно')




        else:
            # Неправильный ответ
            lb_m -= 50
            ui.label_2.setText(f'Money: {str(lb_m)}$')
            pass
    else:
        # Первый запуск
        data = v[str(rn_k)]
        vo = data[4]
        co = data[5]
        a = list(data[:4])
        random.shuffle(a)
        ui.label_5.setText(f'Сложность: Легко')


    # Показываем вопрос и варианты
    ui.label_3.setText(str(vo))
    ui.pushButton.setText(str(a[0]))
    ui.pushButton_2.setText(str(a[1]))
    ui.pushButton_3.setText(str(a[2]))
    ui.pushButton_4.setText(str(a[3]))

# Загружаем первый вопрос
c_o()  # o=None → просто загрузка первого вопроса
print(len(v))


ui.label_2.setText(f'Money: {str(lb_m)}$')

# Подключаем кнопки
ui.pushButton.clicked.connect(lambda: c_o(ui.pushButton.text()))
ui.pushButton_2.clicked.connect(lambda: c_o(ui.pushButton_2.text()))
ui.pushButton_3.clicked.connect(lambda: c_o(ui.pushButton_3.text()))
ui.pushButton_4.clicked.connect(lambda: c_o(ui.pushButton_4.text()))

sys.exit(app.exec_())





# from PyQt5 import uic
# from PyQt5.QtWidgets import QApplication
#
#
#
# Form, Window = uic.loadUiType("milioner.py")
#
# app = QApplication([])
#
# window = Window()
# form = Form()
# form.setupUi(window)
# window.show()
#
#
# app.exec_()
