import os

a = True
dohodi = 0
rashodi = 0
balance = 0

def dohod():
  kolvo = float(input("\nВведите сумму дохода>>> "))
  category = input("\nВыберите источник дохода: \n1.Инвестиции \n2.Подработка \n3.Другое\n>>> ")
  global dohodi
  dohodi += kolvo

def rashod():
    kolvo = float(input("\nВведите сумму расхода>>> "))
    category = input("\nВыберите категорию расходов: \n1.Бытовые \n2.Еда \n3.Развлечение \n4.Другое \n>>> ")
    global rashodi
    rashodi += kolvo

while a:
    os.system("cls")
    balance = dohodi - rashodi
    print(f"Баланс: {balance}")
    print(f"Доходы: {dohodi}")
    print(f"Расходы: {rashodi}")
    action = input("Выберите действие: \n1.Добавить доход \n2.Добавить расход \n>>> ")

    if action == "1":
        dohod()
    elif action == "2":
        rashod()
