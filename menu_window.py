from PyQt5.QtWidgets import QWidget, QLineEdit,QHBoxLayout
QVBoxLayout, QPushButton, QLabel

menu_win = QWidget()

lb_quest = QLabel('Ведіть запитання:')
lb_right_ans = QLabel('Ведіть вірну відповідь:')
lb_wrong_ans1 = QLabel('Ведіть першу хибну відповідь')
lb_wrong_ans2 = QLabel('Ведіть другу хибну відповідь')
lb_wrong_ans3 = QLabel('Ведіть третю хибну відповідь')

le_question = QLineEdit()
le_right_ans = QLineEdit()
le_wrong_ans1 = QLineEdit()
le_wrong_ans2 = QLineEdit()
le_wrong_ans3 = QLineEdit()

lb_header_start = QLabel('Статистика')
lb_header_start.setStyleSheet('font-size: 19px; font-weight: bold;')

lb_statistic = QLabel()

vl_labels = QVBoxLayout()
vl_labels.addWidget(le_question)
vl_labels.addWidget(le_right_ans)
vl_labels.addWidget(le_wrong_ans1)
vl_labels.addWidget(le_wrong_ans2)
vl_labels.addWidget(le_wrong_ans3)

vl_LineEdit = QVBoxLayout()
vl_LineEdit.addWidget(le_question)
vl_LineEdit.addWidget(le_right_ans)
vl_LineEdit.addWidget(le_wrong_ans1)
vl_LineEdit.addWidget(le_wrong_ans2)
vl_LineEdit.addWidget(le_wrong_ans3)

hl_question = QHBoxLayout()
hl_question.addLayout(vl_labels)
hl_question.addLayout(vl_LineEdit)

btn_back = QPushButton('Назад')
btn_add_questio = QPushButton('Додати запитання')
btn_clear = QPushButton('Очистити')
hl_buttons = QHBoxLayout()
hl_buttons.addWidget(btn_add_questio)
hl_buttons.addWidget(btn_clear)

vl_res = QVBoxLayout()
vl_res.addLayout(hl_question)
vl_res.addLayout(hl_buttons)
vl_res.addLayout(lb_header_start)
vl_res.addLayout(lb_statistic)
vl_res.addLayout(btn_back)

menu_win.setLayout(vl_res)
menu_win.resize(550, 450)