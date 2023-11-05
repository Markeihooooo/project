##################################
topping_list = ["วุ้นอโล", "สโนว์มุก", "ไข่มุกโนบิ", "เยลลี่ผลไม้", "บุกราวน์ชูการ์"]
import menu
current_price = menu.price_use()
topping_item = " "



while True:
    topping_showall = menu.topping_showall()
    topping_want = int(input("คุณต้องการใส่ท็อปปิ้งกี่อย่าง"))
    try:
        if topping_want == 1 :
            topping_number1 = int(input("Number"))
        elif topping_want == 2 :
            topping_number1 = int(input("Number"))
            topping_number2 = int(input("Number"))
        elif topping_want == 3 :
            topping_number3 = int(input("Number"))
        elif topping_want == 4 :
            topping_number4 = int(input("Number"))
        elif topping_want == 5 :
            topping_number5 = int(input("Number"))
        elif topping_want == 6 :
            topping_number6 = int(input("Number"))
        elif topping_want == 7 :
            topping_number7 = int(input("Number"))
        elif topping_want == 8 :
            topping_number8 = int(input("Number"))
        elif topping_want == 9 :
            topping_number9 = int(input("Number"))
        elif topping_want == 10 :
            topping_number10 = int(input("Number"))

        # elif topping_want == 2 :
        #     topping_number = int(input("Number"))
        #     topping_number2 = int(input("Number"))
    except ValueError:
        print("***กรุณาใส่เลือกรายการเฉพาะตัวเลข***")















    # topping_choice = int(input("คุณต้องการใส่อะไรบ้าง: "))
    # try:
    #     if topping_choice == 1:
    #         topping_item = topping_item+ topping_list[topping_choice-1]
    #         print("ตอนนี้คุณเลือก : \n==========",topping_item)
    #         menu.topping_not1()
          





    #                     menu.topping_not1()
    #                     topping_choice1 = int(input("คุณต้องการใส่อะไรอีก 1 อย่าง : "))
    #                     if topping_choice1 == 1 :
    #                         print("คุณเลือกรายการซ้ำ กรุณาเลือกใหม่ : ")
    #                     elif topping_choice1 == 2 :
    #                         topping_item = topping_item +","+ topping_list[topping_choice-2]
    #                         print("ตอนนี้คุณเลือก : ",topping_item)
    #                         menu.topping_not12()
    #                         break
    #                 except ValueError:
    #                         print("***กรุณาใส่เลือกรายการเฉพาะตัวเลข***")
    #                         pass
    #         elif checktopping_up == "N" or checktopping_up == "n":
    #             pass   
    # except ValueError:
    #     pass






                 
    
