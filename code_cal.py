##################################
topping_list = ["วุ้นอโล", "สโนว์มุก", "ไข่มุกโนบิ", "เยลลี่ ผลไม้", "บุกราวน์ชูการ์"]
import menu
current_price = menu.price_use()

topping_item = " "
topping_showall = menu.topping_showall()



topping_choice = int(input("คุณต้องการอะไรบ้าง: "))

if topping_choice == 1:
    topping_item = topping_item + topping_list[topping_choice-1]
    print("ตอนนี้คุณเลือก : ",topping_item)
    checktopping_up = input("คุณต้องการเลือกท๊อปปิ้งอีก หรือไม่ Y/n : ")
    if checktopping_up == "Y" or checktopping_up == "y":
       menu.topping_not1()
       topping_choice1 = int(input("คุณต้องการใส่อะไรอีก 1 อย่าง : "))
       if topping_choice1 == 1 :
           print("คุณเลือกรายการซ้ำ กรุณาเลือกใหม่ : ")
    elif checktopping_up == "N" or checktopping_up == "n":
        pass   
                 
    
