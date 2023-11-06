import menu
topping_list = ["วุ้นอโล", "สโนว์มุก","ไข่มุกโนบิ","เยลลี่ผลไม้", "บุกราวน์ชูการ์ ", "คาราเมล", "สตอเบอรี่", "ไข่มุกราวน์ชูการ์", "บุกคริสตัส", "ราสเบอรี่"]



def select_menu():
    while True:
        menu.menu()
        menu_number = input("\nเลือกเมนูที่คุณต้องการ : ")
        print("\n\n###########################################################")
        if menu_number.isdigit():
            menu_number=int(menu_number)
            if 1 <= menu_number <= 11:
                print("\nเมนูที่คุณเลือก\n  ",menu.menu_list[menu_number-1],menu.price_use()+ menu.menu_price[menu_number-1],"฿")
                
                
                break
            else:
                print("***โปรดป้อนตัวเลข 1-11***")
        else:
            print("***โปรดป้อนเฉพาะ ตัวเลข 1-11***")
    
select_menu()


# while True:
#     menu_data = menu.menu()
#     menu_number = input("\nเลือกเมนูที่คุณต้องการ : ")
#     print("\n\n###########################################################")
#     try:
#         menu_number = int(menu_number)
#         if menu_number > 12:
#             menu_number == " "
#             break
#         else:
#             break
            
        
#     except ValueError:
#         print("***กรุณาใส่เลือกรายการเฉพาะตัวเลข***")





# print("\nเมนูที่คุณเลือก\n  ",menu.menu_list[menu_number-1],menu.price_use()+ menu.menu_price[menu_number-1]," ฿")
# check_menu = input("คุณต้องการแก้ไข เมนู ที่เลือกหรือไม่ \nY.ต้องการแก้ไข\nN.ไม่ต้องการ\n\nY/N : ")
# if check_menu == "Y" or check_menu == "y":
#     pass
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