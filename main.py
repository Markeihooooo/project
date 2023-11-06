import menu
topping_list = ["วุ้นอโล", "สโนว์มุก","ไข่มุกโนบิ","เยลลี่ผลไม้", "บุกราวน์ชูการ์ ", "คาราเมล", "สตอเบอรี่", "ไข่มุกราวน์ชูการ์", "บุกคริสตัส", "ราสเบอรี่"]

while True:
    menu_data = menu.menu()
    menu_number = input("\nเลือกเมนูที่คุณต้องการ : ")
    print("\n\n###########################################################")
    try:
        menu_number = int(menu_number)
        if menu_number == 1:
            print("\n\nเมนูที่คุณเลือก\n***ชานมใต้หวัน(Taiwan Mile Tea)     19฿ ***")
            menu.set_price(menu.price_use() + 19)
        elif menu_number == 2:
            print("\n\nเมนูที่คุณเลือก\n***ชานมกาแฟ(Coffee Milk Tea)     19฿ ***")
            menu.set_price(menu.price_use() + 19)
        elif menu_number == 3:
            print("\n\nเมนูที่คุณเลือก\n***ชานมโกโก้(Cocoa Milk Tea)     19฿ ***")
            menu.set_price(menu.price_use() + 19)
        elif menu_number == 4:
            print("\n\nเมนูที่คุณเลือก\n***ชานมเผือก(Taro Milk Tea)      19฿ ***")
            menu.set_price(menu.price_use() + 19)
        elif menu_number == 5:
            print("\n\nเมนูที่คุณเลือก\n***ชานมลิ้นจี่(Lychee Milk Tea)  19฿ ***")
            menu.set_price(menu.price_use() + 19)
        elif menu_number == 6:
            print("\n\nเมนูที่คุณเลือก\n***ชานมคาราเมล(caramel Milk Tea) 19฿ ***")
            menu.set_price(menu.price_use() + 19)
        elif menu_number == 7:
            print("\n\nเมนูที่คุณเลือก\n***ชานมน้ำผึ้ง(Honey Milk Tea)   19฿ ***")
            menu.set_price(menu.price_use() + 19)
        elif menu_number == 8:
            print("\n\nเมนูที่คุณเลือก\n***ชาดำเย็น(Thai Tea)         19฿ ***")
            menu.set_price(menu.price_use() + 19)
        elif menu_number == 9:
            print("\n\nเมนูที่คุณเลือก\n***ชาไทย(Thai Milk Tea)        19฿ ***")
            menu.set_price(menu.price_use() + 19)
        elif menu_number == 10:
            print("\n\nเมนูที่คุณเลือก\n***ชาเขียว(green Tea)          19฿ ***")
            menu.set_price(menu.price_use() + 19)
        elif menu_number == 11:
            print("\n\nเมนูที่คุณเลือก\n***ชานมเเอปเปิ้ล(Appln Milk Tea) 19฿ ***")
            menu.set_price(menu.price_use() + 19)
        break
    except ValueError:
        print("***กรุณาใส่เลือกรายการเฉพาะตัวเลข***")
print("\n***************** TOPPING *****************\nท๊อปปิ้งของเรามีดังนี้ \n")
print(topping_list,"\n")
topping_yn = input("คุณต้องการเพิ่ม ท๊อปปิ้ง ไหม \nY.ต้องการเพิ่ม\nN.ไม่ต้องการ\n\nY/N : ")
if topping_yn == ("Y") or topping_yn == ("y"):
    import code_cal
elif topping_yn == ("N") or topping_yn == ("n"):
    pass


menu.size_cup()