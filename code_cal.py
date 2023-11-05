gray_code = "\033[1;30m" # กำหนดสี 
reset_code = "\033[0m"
##################################
"""import profile
price = profile.price"""
import menu
current_price = menu.price_use()

print(current_price)

topping_item = " "
topping_showall = menu.topping_showall()


topping_list = ["วุ้นอโล", "สโนว์มุก", "ไข่มุกโนบิ", "เยลลี่ ผลไม้", "บุกราวน์ชูการ์"]
topping_choice = int(input("คุณต้องการอะไรบ้าง: "))

if topping_choice == 1:
    topping_item = topping_item + topping_list[topping_choice-1]
    print("ตอนนี้คุณเลือก : ",topping_item)
    checktopping_up = input("คุณต้องการเลือกท๊อปปิ้งอีก หรือไม่ Y/n : ")
    if checktopping_up == "Y" or checktopping_up == "y":
        pass
