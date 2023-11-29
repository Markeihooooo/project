import menu
####################
# menu_number = 0
list_menu_user=[]
list_topping_user=[]
list_sugar_user=[]
list_cup_user=[]
list_price_user=[]
topping_numberall = []
price1 = 0

topping_number2 = None
topping_number3 = None
def topping_check(selected_items):
    print("\033[1;35m==================== topping ==========================\033[0m")
    for i in range(1, 11):
         if i in selected_items:
             print("\033[1;32m", end='')  # สีเทา
         else:
             print("\033[0m", end='')  # สีปกติ


         if  i == 1:
             print("1.วุ้นอโล        ---- +15 ฿", end='')
         elif i == 2:
             print("    2.สโนว์มุก       ---- +10 ฿")
         elif i == 3:
             print("3.ไข่มุกโนบิ      ---- +10 ฿", end='')
         elif i == 4:
             print("    4.เยลลี่ ผลไม้    ---- +10 ฿")
         elif i == 5:
           print("5.บุกราวน์ชูการ์   ---- +10 ฿", end='')
         elif i == 6:
            print("    6.คาราเมล      ---- +10 ฿")
         elif i == 7:
             print("7.สตอเบอรี่      ---- +10 ฿", end='')
         elif i == 8:
             print("    8.ไข่มุกราวน์ชูการ์ ---- +15 ฿")
         elif i == 9:
             print("9.บุกคริสตัส      ---- +15 ฿", end='')
         elif i == 10:
            print("    10.ราสเบอรี่     ---- +10 ฿\n")
    print("\033[0;37;40m", end='')
    print("\033[1;35m=======================================================\033[0m")

###############



def menu_tea():
    global menu_number
    global check_menu
    while True:
        menu.menu()
        menu_number = input("\n\033[1;34mPlease choose the menu you want. : \033[0m")
        print("\n\n###########################################################")
        if menu_number.isdigit():
            menu_number = int(menu_number)
            if 1 <= menu_number <= 11:
                print("\n\n\033[1;34mYour chosen menu is\033[0m\n\n",menu.menu_list[menu_number-1],"ราคา ",menu.menu_price[menu_number-1]," ฿\n")#+ menu.menu_price[menu_number-1]
                while True:
                    check_menu = input("\033[1;34mคุณต้องการดำเนินการต่อหรือไม่\033[0m\n\n\033[1;32mY = ดำเนินการต่อ\033[0m\n\033[1;33mN = แก้ไขรายการเมนู\033[0m\n\033[1;31m0 = ยกเลิก\033[0m\n\n\033[1;34m[Y/N] :\033[0m ")#
                    if check_menu == "Y" or check_menu == "y" or check_menu == "1":
                        menu.price = menu.price + menu.menu_price[menu_number-1]
                        list_menu_user.append(menu.menu_list[menu_number-1])
                        break
                    elif check_menu == "N" or check_menu == "n" or check_menu == "2":
                        break
                    elif check_menu == "0":
                        menu_number=0
                        break
                    else:
                        print("กรุณาใส่ตัวเลข")
                        continue
                if check_menu == "N" or check_menu =="n":continue

            elif menu_number == 0:
                break
            elif 1>menu_number<11:
                print("\n\033[1;31mคุณกรอกรายการที่ไม่ถูกต้อง\033[0m")
                continue
            else:
                print("\n\033[1;31mคุณกรอกรายการที่ไม่ถูกต้อง\033[0m")
                continue
        elif menu_number == " ":
            print("\033[1;31mคุณยังไม่ได้กรอกข้อมูล\033[0m")
            continue
        else:
            print("\n\033[1;31m======= โปรดป้อนตัวเลขเท่านั้น =======\033[0m\n ")
            continue
        break  

def menutopping_new():
    global  topping_want 
    global topping_number1
    global topping_select
    global list_topping_user
    while True:
        menu.topping_showall()
        topping_want = input("\n\033[1;34mHow many toppings do you want to add? Maximum is 3\033[0m"
                            "\n\n\033[1;34m9 = เลือกเมนูใหม่\033[0m"
                            "\n\n\033[1;31m0 = ยกเลิกท๊อปปิ้ง(ดำเนินการต่อ) \033[0m"
                            "\n\n\033[1;34mต้องการใส่กี่อย่าง >>>:\033[0m " )
        if topping_want.isdigit():
            topping_want = int(topping_want)
            if 1 <= topping_want <= 3:
                menu.topping_showall()
                if topping_want == 1 :  # ต้องการท๊อปปิ้ง 1 อย่าง
                    while True:
                        topping_1()
                        check_want_topping()
                        if check_topping_select != "2":break
                        menu.topping_showall()

                    if check_topping_select =="9":
                        continue

                elif topping_want == 2:
                    while True:
                        topping_1()
                        check_want_topping()
                        topping_2()
                        check_want_topping()
                        if check_topping_select != "2":break
                        menu.topping_showall()

                elif topping_want == 3:
                    while True:
                        topping_3()
                        check_want_topping()
                        if check_want_topping != "2":break
                        menu.topping_showall()
            elif topping_want == 0:
                break
            else:
                print("กรุณาใส่ตัวเลขที่กำหนด")
                continue
        else:
            print("กรุณาใส่ตัวเลข")
            continue

        if check_topping_select =="9":
            continue
        break

def topping_1():
    # from menu import topping_list
    global  topping_want 
    global topping_number1
    global topping_select
    global list_topping_user
    global topping_numberall
    while True:
        topping_number1 = input("\n\033[1;34mPlease choose the topping you want. : \033[0m")
        if topping_number1.isdigit():
            topping_number1 = int(topping_number1)
            if 1 <= topping_number1 <= 10:
                menu.topping_showall()
                topping_select = menu.topping_list[topping_number1-1]
                print("\n\033[1;32mYou choose : " + topping_select)
                if topping_want == 1 or topping_want == "1":
                    list_topping_user.append(menu.topping_list[topping_number1-1])
                    list_topping_user.append(" ")
                    list_topping_user.append(" ")
                else:
                    list_topping_user.append(menu.topping_list[topping_number1-1])
                topping_numberall.append(topping_number1)
                topping_check(topping_numberall)
                break
            else:
                print("\n\033[1;31m======= โปรดป้อนตัวเลขเท่านั้นในรายการเท่านั้น =======\033[0m\n")
                menu.topping_showall()
                continue
        elif topping_number1 == " " :
            print("\n\033[1;31m======= โปรดป้อนตัวเลขเท่านั้นในรายการเท่านั้น =======\033[0m\n")
            menu.topping_showall()
            continue
        else:
            print("\n\033[1;31m======= โปรดป้อนตัวเลขเท่านั้นในรายการเท่านั้น =======\033[0m\n")
            menu.topping_showall()


def topping_2():
    global  topping_want 
    global topping_number1
    global topping_number2
    global topping_select
    global list_topping_user
    global topping_numberall

    while True:
        topping_check(topping_numberall)
        topping_number2 = input("\n\033[1;34mPlease choose the topping you want 2. : \033[0m")
        if topping_number2.isdigit():topping_number2= int(topping_number2)
            

        if topping_number2> 10 or topping_number2<1:
            menu.topping_showall
            continue
        elif topping_number2 == topping_number1:
            print("\n\033[1;31mกรุณาเลือกรายการซ้ำกับรายการที่ 1 กรุณาเลือกรายการที่ 2 ใหม่\033[0m \n")
            continue
        elif topping_number1 == " ":
            print("\033[1;31mคุณยังไม่ได้กรอกข้อมูล\033[0m")
        else:
            pass

            topping_select = menu.topping_list[topping_number2-1]
            print("\n\033[1;32mYou choose : " + topping_select)
            if topping_want == 2 or topping_want == "2":
                list_topping_user.append(menu.topping_list[topping_number2-1])
                list_topping_user.append(" ")
            elif topping_want == 3 or topping_want == "3":
                list_topping_user.append(menu.topping_list[topping_number2-1])
                
            topping_numberall.append(topping_number2)
            topping_check(topping_numberall)
            break
        break






def topping_3():
    print("topping 3")

def check_want_topping():
    # from menu import price_use
    # from menu import set_price
    global topping_select
    global list_topping_user
    global check_topping_select
    global topping_numberall
    global topping_want
    global topping_number1
    global topping_number2
    global topping_number3
    while True:
        check_topping_select = input("\033[1;34mคุณต้องการดำเนินการต่อหรือไม่\033[0m\n\033[1;32m1.ดำเนินการต่อไป\033[0m"
                                    "\033[1;33m\n2.เปลี่ยนท็อปปิง\033[0m \033[1;36m\n9.เลือกจำนวนท็อปปิงใหม่\033[0m"
                                    "\033[1;31m\n0.ยกเลิกท็อปปิง(เเละดำเนินการต่อไป)\033[0m \n\n>>>: " )
        if check_topping_select == "1":
            if topping_want == "1" or topping_want == 1:
                menu.price = menu.price + menu.topping_price[int(topping_number1)-1]
                break

            elif topping_want == "2" or (topping_want == 2):
            # topping_want == "2" or topping_want == 2 and topping_number2 != "":
                if topping_number2 != None:
                    menu.price = menu.price + menu.topping_price[int(topping_number1)-1]
                    menu.price = menu.price + menu.topping_price[int(topping_number2) - 1]
                    break
                else:break
                    # menu.price = menu.price + menu.topping_price[int(topping_number2)-1]

            elif topping_want == "3" or (topping_want == 3):
                if topping_number3 != None:
                    menu.price(menu.price_use()+menu.topping_price[topping_number1-1])
                    menu.price(menu.price_use()+menu.topping_price[topping_number2-1])
                    menu.price(menu.price_use()+menu.topping_price[topping_number3-1])
                    break
                else:break
            else:
                break
        elif check_topping_select == "2":
            topping_select = ""
            list_topping_user = []
            topping_number1 = ""
            topping_numberall = []
            break
        elif check_topping_select == "9":
            topping_select = ""
            list_topping_user = []
            topping_want =""
            topping_numberall = []
            break
        elif check_topping_select == "0":
            topping_select = ""
            list_topping_user = []
            topping_want = ""
            #result = 0
            break
        else:
            print("\n\033[1;31m======= โปรดป้อนตัวเลขเท่านั้น =======\033[0m\n")
            continue


def sugar_seclect_new ():
    global sugar_check_new
    while True:
        sugar_check_new = input("\033[1;34m กรุณาเลือกความหวานที่คุรต้องการ \033[0m : ")
        if sugar_check_new == "1":
            print("คุณเลือกความหวาน : ",menu.sugar_list[int(sugar_check_new)-1])
            sugar_sure = input("คุณต้องการเลือกความหวานนี้หรือไม่ (Y/N) : ")
            if sugar_sure == "Y" or sugar_sure == "y":
                print("คุณเลือกความหวาน : ",menu.sugar_list[int(sugar_check_new)-1])
                list_sugar_user.append(menu.sugar_list[int(sugar_check_new)-1])
                break
            else:
                continue
        elif sugar_check_new == "2":
            print("คุณเลือกความหวาน : ",menu.sugar_list[int(sugar_check_new)-1])
            sugar_sure = input("คุณต้องการเลือกความหวานนี้หรือไม่ (Y/N) : ")
            if sugar_sure == "Y" or sugar_sure == "y":
                print("คุณเลือกความหวาน : ",menu.sugar_list[int(sugar_check_new)-1])
                list_sugar_user.append(menu.sugar_list[int(sugar_check_new)-1])
                break
            else:
                continue
        elif sugar_check_new == "3":
            print("คุณเลือกความหวาน : ",menu.sugar_list[int(sugar_check_new)-1])
            sugar_sure = input("คุณต้องการเลือกความหวานนี้หรือไม่ (Y/N) : ")
            if sugar_sure == "Y" or sugar_sure == "y":
                print("คุณเลือกความหวาน : ",menu.sugar_list[int(sugar_check_new)-1])
                list_sugar_user.append(menu.sugar_list[int(sugar_check_new)-1])
                break
            else:
                continue
        elif sugar_check_new =="4":
            print("คุณเลือกความหวาน : ",menu.sugar_list[int(sugar_check_new)-1])
            sugar_sure = input("คุณต้องการเลือกความหวานนี้หรือไม่ (Y/N) : ")
            if sugar_sure == "Y" or sugar_sure == "y":
                print("คุณเลือกความหวาน : ",menu.sugar_list[int(sugar_check_new)-1])
                list_sugar_user.append(menu.sugar_list[int(sugar_check_new)-1])
                break
            else:
                continue
        else:
            print("\033[1;31m======= โปรดป้อนตัวเลขเท่านั้น =======\033[0m\n")
            continue


def cup_select_new():
    menu.size_cup()
    while True:
        cup_check_new = input("คุณต้องการใช้แก้วขนาดเท่าไหร่ (ใส่ตัวเลข) : ")
        if cup_check_new == "1" or cup_check_new == "2" or cup_check_new == "3" or cup_check_new == "4":
            menu.price = menu.price + menu.cup_price[int(cup_check_new)-1]
            cup_check_agian = input(f"\033[1;34mยืนยันที่จะเลือกแก้วขนาด {menu.cup_price[int(cup_check_new)-1]} ฿\033[0m (Y/N) : ")
            if cup_check_agian  == "Y" or cup_check_agian == "y":
                list_cup_user.append(menu.cup_size[int(cup_check_new)-1])
                break



def finish_new():
    # global list_menu_user
    # global list_sugar_user
    # global list_topping_user
    # global list_cup_user
    print("\033[1;35mเมนูที่ 1 (Magenta)\033[0m")
    print("คุณเลือกเมนู : ",list_menu_user[0:1])
    result_list = [item for item in list_topping_user[0:3] if item.strip() != ""]
    if result_list:
        print("คุณเลือกท๊อปปิ้ง : ",result_list)
    else:
        print("คุณเลือกท๊อปปิ้ง : ไม่ได้เลือกท๊อปปิ้ง")

    print("คุณเลือกความหวาน : ",list_sugar_user[0:1])
    print("คุณเลือกขนาดแก้ว : ",list_cup_user[0:1])
    print("รวม ราคา : ",price1)
    

def finish_new2():
    # global list_menu_user
    # global list_sugar_user
    # global list_topping_user
    # global list_cup_user
    print("\033[1;35mเมนูที่ 2 (Magenta)\033[0m")
    print("คุณเลือกเมนู : ",list_menu_user[1:2])
    result_list = [item for item in list_topping_user[3:6] if item.strip() != ""]
    if result_list:
        print("คุณเลือกท๊อปปิ้ง : ",result_list)
    else:
        print("คุณเลือกท๊อปปิ้ง : ไม่ได้เลือกท๊อปปิ้ง")

    print("คุณเลือกความหวาน : ",list_sugar_user[1:2])
    print("คุณเลือกขนาดแก้ว : ",list_cup_user[1:2])
    print("รวม ราคา : ",(menu.price-price1))
    print("ราคา รวมทั้งสองเมนู : ",(menu.price))


