import menu
while True:
    menu_data = menu.menu()
    menu_number = input("\nเลือกเมนูที่คุณต้องการ : ")
    print("\n\n###########################################################")
    try:
        menu_number = int(menu_number)
        if menu_number == 1:
            print("\n\nเมนูที่คุณเลือก\n***ชานมใต้หวัน(Taiwan Mile Tea)     29฿ ***")
            menu.set_price(menu.price_use() + 29)
        elif menu_number == 2:
            pass
        elif menu_number == 3:
            pass
        elif menu_number == 4:
            pass
        break  
    except ValueError:
        print("***กรุณาใส่เลือกรายการเฉพาะตัวเลข***")

topping_yn = input("คุณต้องการเพิ่ม ท๊อปปิ้ง ไหม \nY.ต้องการเพิ่ม\nN.ไม่ต้องการ\n\nY/N : ")
if topping_yn == ("Y") or topping_yn == ("y"):
    import code_cal