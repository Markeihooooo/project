gray_code = "\033[1;30m" # กำหนดสี 
##################################
"""import profile
price = profile.price"""
import menu

current_price = menu.price_use()

print(current_price)

topping_item = " "
def menu_showall():
    print("\n1.วุ้นอโล      ---- +5 ฿")
    print("2.สโนว์มุก     ---- +5 ฿")
    print("3.ไข่มุกโนบิ    ---- +5 ฿")
    print("4.เยลลี่ ผลไม้  ---- +5 ฿")
    print("5.บุกราวน์ชูการ์ ---- +5 ฿\n")

def menu_not1():
    print(f"\n{gray_code}1.วุ้นอโล      ---- +5 ฿")
    print("2.สโนว์มุก     ---- +5 ฿")
    print("3.ไข่มุกโนบิ    ---- +5 ฿")
    print("4.เยลลี่ ผลไม้  ---- +5 ฿")
    print("5.บุกราวน์ชูการ์ ---- +5 ฿\n")

menu_showall()
topping_list = ["วุ้นอโล", "สโนว์มุก", "ไข่มุกโนบิ", "เยลลี่ ผลไม้", "บุกราวน์ชูการ์"]
topping_choice = int(input("คุณต้องการอะไรบ้าง: "))

if topping_choice == 1:
    topping_item = topping_item + topping_list[topping_choice-1]
    print("ตอนนี้คุณเลือก : ",topping_item)
    checktopping_up = input("คุณต้องการเลือกท๊อปปิ้งอีก หรือไม่ Y/n : ")
    if checktopping_up == "Y" or checktopping_up == "y":
        pass
