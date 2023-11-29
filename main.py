import code_def
import menu
menu_user = 1


while True: 
    code_def.menu_tea() ##เมนูชา
    if code_def.menu_number != 0 :
        print(code_def.list_menu_user)
        while True:
            topping_yn = input(
                "\033[1;34m\nDo you want to add toppings ?\n\033[0m \n"
                "\033[1;32mY.ต้องการเพิ่ม\033[0m\n\033[1;31mN.ไม่ต้องการ(ดำเนินการต่อ) \033[0m\n"
                "\033[1;34m9.กลับไปเลือก เมนู ใหม่ "
                "\n0 ยกเลิก\n"
                "\033[1;34m\nY/N >>>:\033[0m ")

            if topping_yn == ("Y") or topping_yn == ("y"): 
                code_def.menutopping_new()
                print("price : ",menu.price)
                break
            elif topping_yn == ("N") or topping_yn == ("n"):
                print("ไม่เลือกท๊อปปิ้ง")
                code_def.list_topping_user.append(" ")
                code_def.list_topping_user.append(" ")
                code_def.list_topping_user.append(" ")
                break
            elif topping_yn == ("9"):
                code_def.list_menu_user.pop()
                print(code_def.list_menu_user)#เช็คลบlist
                break
            elif topping_yn == ("0"):
                break
            else: 
                print("กรุณาใส่ตัวเลข")
                continue
            
        if topping_yn == ("9"):continue   #topping
        # elif topping_yn == ("9"):continue
    else:
        print("ยกเลิก")
        
    if code_def.menu_number != 0 :
        while True:
            menu.sugar_choice()
            code_def.sugar_seclect_new()
            code_def.cup_select_new()
            break
    if menu_user == 1:
        code_def.price1 = code_def.price1 + menu.price
        code_def.finish_new()
    elif menu_user == 2:
        code_def.finish_new()
        code_def.finish_new2()
    if code_def.menu_number!= 0 and menu_user < 2:
        want_more = input("คุณต้องการสั่งอีกแก้วหรือไม่ : ")
        if want_more == "Y" or want_more == "y":
            menu_user = menu_user + 1
            code_def.topping_numberall = []
            
            continue
        elif want_more == "N" or want_more == "n":
            break

    if want_more !="Y" or want_more!= "y":
        break
    ##### 