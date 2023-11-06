import menu
# import code_cal
while True:
    menu.menu()
    menu_number = input("\nเลือกเมนูที่คุณต้องการ : ")
    print("\n\n###########################################################")
    if menu_number.isdigit():#.isdigit คือ ตรวจสอบว่าstrที่รับมาเป็นตัวเลขไหม
        menu_number = int(menu_number)
        if 1 <= menu_number <= 11:
            menu.name_menu = menu.menu_list[menu_number-1]
            menu.set_price(menu.price_use() + menu.menu_price[menu_number-1])

            print("\nเมนูที่คุณเลือก\n\n",menu.menu_list[menu_number-1],"ราคา ",menu.price_use()+ menu.menu_price[menu_number-1]," ฿\n")

            check_menu = input("คุณต้องการดำเนินการต่อหรือไม่\nY = ดำเนินการต่อ\nN = แก้ไขรายการเมนู\n0 = ยกเลิก\n(Y/N) : ")
            while True:
                if check_menu == "Y" or check_menu == "y":
                    import code_cal
                    
                    break
                elif check_menu == "N" or check_menu == "n":
                    menu.name_menu = " "
                    menu.price = 0
                    break
                elif check_menu == "0":
                    menu.name_menu = " "
                    menu.price = 0
                    break
                else:
                    print("***โปรดป้อน Y หรือ N***")
        elif menu_number == 0:
            break
        else:
            print("***โปรดป้อนตัวเลข 1-11***")
        pass
    else:
        print("***โปรดป้อนเฉพาะ ตัวเลข 1-11***")
    if check_menu != "n" or check_menu != "N" and menu_number == 0:break





# elif check_menu == "N" or check_menu == "n":
#         print("\n***************** TOPPING *****************\nท๊อปปิ้งของเรามีดังนี้ \n")
#         print(topping_list,"\n")
#         topping_yn = input("คุณต้องการเพิ่ม ท๊อปปิ้ง ไหม \nY.ต้องการเพิ่ม\nN.ไม่ต้องการ\n\nY/N : ")
#         if topping_yn == ("Y") or topping_yn == ("y"):
#             import code_cal
#         elif topping_yn == ("N") or topping_yn == ("n"):
#             pass
        

# print("รายการสินค้า >>>> = " ,menu.price_use() , " ฿")
    




# menu.size_cup()