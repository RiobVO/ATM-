import time

print("Добро пожаловать в Беларусбанк ")

#чтение карты
time.sleep(1)
#пароль


pin = int(input("Введите пин-код банкомата:"))
password = 1234

# Мой баланс
balance = 5000

# проверка пин-кода действителен или нет
if pin == password:
    while True:

        # (Интерфейс)

        print(""" 
        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
		>	                                                            <
		>	                    1 == Баланс                             <
		>	                    2 == Снять баланс                       <
		>	                    3 == Депоситный остаток                 <
		>	                    4 == Выход                              <
		>	                                                            <
		>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
			"""

              )

        try:
            # taking an option from user
            option = int(input("Пожалуйста, введите свой выбор"))
        except:
            print("Пожалуйста, введите правильный вариант")

        # for option 1
        if option == 1:
            print(f"Ваш текущий баланс {balance}")

        if option == 2:
            withdraw_amount = int(input("Пожалуйста, введите сумму вывода "))

            balance = balance - withdraw_amount

            print(f"{withdraw_amount} Списывается с вашего счета")

            print(f"Ваш обновленный баланс {balance}")

        if option == 3:
            deposit_amount = int(input("пожалуйста,введите сумму депозита"))

            balance = balance + deposit_amount

            print(f"{deposit_amount} зачисляется на ваш счет")

            print(f"ваш обновленный баланс {balance}")

        if option == 4:
            break


else:
    print("           Неверный pin-code Пожалуйста, попробуйте еще раз")
