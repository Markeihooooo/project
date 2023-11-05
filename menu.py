gray_code = "\033[1;30m" # กำหนดสี 
reset_code = "\033[0m"
##################################
price = 0 

def set_price(new_price):
    global price
    price = new_price


def price_use():
    return price

## Menu
def menu():
    print("        ┌=======================================┐")
    print("        ╎          |ร้าน ตั้งหวังเกือบเจ้ง|           ╎")
    print("        └=======================================┘\n")
    print("======================== MENU ==============================\n")
    print("| 1.ชานมใต้หวัน          (Taiwan Mile Tea)        ----- 19 ฿ |")
    print("| 2.ชานมกาแฟ           (Coffee Milk Tea)        ----- 19 ฿ |")
    print("| 3.ชานมโกโก้           (Cocoa Milk Tea)         ----- 19 ฿ |")
    print("| 4.ชานมเผือก           (Taro Milk Tea)          ----- 19 ฿ |")
    print("| 5.ชานมลิ้นจี่            (Lychee Milk Tea)        ----- 19 ฿ |")
    print("| 6.ชานมคาราเมล        (caramel Milk Tea)       ----- 19 ฿ |")
    print("| 7.ชานมน้ำผึ้ง           (Honey Milk Tea)         ----- 19 ฿ |")
    print("| 8.ชาดำเย็น            (Thai Tea)               ----- 19 ฿ |")
    print("| 9.ชาไทย             (Thai Milk Tea)          ----- 19 ฿ |")
    print("| 10.ชาเขียว            (green Tea)              ----- 19 ฿ |")
    print("| 11.ชานมเเอปเปิ้ล       (Appln Milk Tea)         ----- 19 ฿ |\n")
    print("============================================================")

def topping_showall():
    print("\n1.วุ้นอโล      ---- +10 ฿")
    print("2.สโนว์มุก     ---- +10 ฿")
    print("3.ไข่มุกโนบิ    ---- +10 ฿")
    print("4.เยลลี่ ผลไม้  ---- +10 ฿")
    print("5.บุกราวน์ชูการ์ ---- +10 ฿\n")

def topping_not1():
    print(f"\n{gray_code}1.วุ้นอโล      ---- +5 ฿{reset_code}")
    print("2.สโนว์มุก     ---- +5 ฿")
    print("3.ไข่มุกโนบิ    ---- +5 ฿")
    print("4.เยลลี่ ผลไม้  ---- +5 ฿")
    print("5.บุกราวน์ชูการ์ ---- +5 ฿\n")

def topping_not2():
    print("\n1.วุ้นอโล      ---- +5 ฿")
    print(f"{gray_code}2.สโนว์มุก ---- +5 ฿{reset_code}")
    print("3.ไข่มุกโนบิ    ---- +5 ฿")
    print("4.เยลลี่ ผลไม้  ---- +5 ฿")
    print("5.บุกราวน์ชูการ์ ---- +5 ฿\n")

def topping_not3():
    print("\n1.วุ้นอโล      ---- +5 ฿")
    print("2.สโนว์มุก     ---- +5 ฿")
    print(f"{gray_code}3.ไข่มุกโนบิ    ---- +5 ฿{reset_code}")
    print("4.เยลลี่ ผลไม้  ---- +5 ฿")
    print("5.บุกราวน์ชูการ์ ---- +5 ฿\n")

def topping_not4():
    print("\n1.วุ้นอโล      ---- +5 ฿")
    print("2.สโนว์มุก     ---- +5 ฿")
    print("3.ไข่มุกโนบิ    ---- +5 ฿")
    print(f"{gray_code}4.เยลลี่ ผลไม้  ---- +5 ฿{reset_code}")
    print("5.บุกราวน์ชูการ์ ---- +5 ฿\n")

def topping_not5():
    print("\n1.วุ้นอโล      ---- +5 ฿")
    print("2.สโนว์มุก     ---- +5 ฿")
    print("3.ไข่มุกโนบิ    ---- +5 ฿")
    print("4.เยลลี่ ผลไม้  ---- +5 ฿")
    print(f"{gray_code}5.บุกราวน์ชูการ์ ---- +5 ฿{reset_code}\n")

def topping_not12():
    print(f"\n{gray_code}1.วุ้นอโล      ---- +5 ฿{reset_code}")
    print(f"{gray_code}5.บุกราวน์ชูการ์ ---- +5 ฿{reset_code}")
    print("3.ไข่มุกโนบิ    ---- +5 ฿")
    print("4.เยลลี่ ผลไม้  ---- +5 ฿")
    print("5.บุกราวน์ชูการ์ ---- +5 ฿\n")

def topping_not13():
    print(f"\n{gray_code}1.วุ้นอโล      ---- +5 ฿{reset_code}")
    print("2.สโนว์มุก     ---- +5 ฿")
    print(f"{gray_code}3.ไข่มุกโนบิ    ---- +5 ฿{reset_code}")
    print("4.เยลลี่ ผลไม้  ---- +5 ฿")
    print("5.บุกราวน์ชูการ์ ---- +5 ฿\n")

def topping_not14():
    print(f"\n{gray_code}1.วุ้นอโล      ---- +5 ฿{reset_code}")
    print("2.สโนว์มุก     ---- +5 ฿")
    print("3.ไข่มุกโนบิ    ---- +5 ฿")
    print(f"{gray_code}4.เยลลี่ ผลไม้  ---- +5 ฿{reset_code}")
    print("5.บุกราวน์ชูการ์ ---- +5 ฿\n")

def topping_not15():
    print(f"\n{gray_code}1.วุ้นอโล      ---- +5 ฿{reset_code}")
    print("2.สโนว์มุก     ---- +5 ฿")
    print("3.ไข่มุกโนบิ    ---- +5 ฿")
    print("4.เยลลี่ ผลไม้  ---- +5 ฿")
    print(f"{gray_code}5.บุกราวน์ชูการ์ ---- +5 ฿{reset_code}\n")

def topping_not23():
    print("\n1.วุ้นอโล      ---- +5 ฿")
    print(f"{gray_code}5.บุกราวน์ชูการ์ ---- +5 ฿{reset_code}\n")
    print(f"{gray_code}3.ไข่มุกโนบิ    ---- +5 ฿{reset_code}")
    print("4.เยลลี่ ผลไม้  ---- +5 ฿")
    print("5.บุกราวน์ชูการ์ ---- +5 ฿\n")

def topping_not24():
    print("\n1.วุ้นอโล      ---- +5 ฿")
    print(f"{gray_code}5.บุกราวน์ชูการ์ ---- +5 ฿{reset_code}\n")
    print("3.ไข่มุกโนบิ    ---- +5 ฿")
    print(f"{gray_code}4.เยลลี่ ผลไม้  ---- +5 ฿{reset_code}")
    print("5.บุกราวน์ชูการ์ ---- +5 ฿\n")

def topping_not25():
    print("\n1.วุ้นอโล      ---- +5 ฿")
    print(f"{gray_code}5.บุกราวน์ชูการ์ ---- +5 ฿{reset_code}\n")
    print("3.ไข่มุกโนบิ    ---- +5 ฿")
    print("4.เยลลี่ ผลไม้  ---- +5 ฿")
    print(f"{gray_code}5.บุกราวน์ชูการ์ ---- +5 ฿{reset_code}\n")

def topping_not34():
    print("\n1.วุ้นอโล      ---- +5 ฿")
    print("2.สโนว์มุก     ---- +5 ฿")
    print(f"{gray_code}3.ไข่มุกโนบิ    ---- +5 ฿{reset_code}")
    print(f"{gray_code}4.เยลลี่ ผลไม้  ---- +5 ฿{reset_code}")
    print("5.บุกราวน์ชูการ์ ---- +5 ฿\n")

def topping_not35():
    print("\n1.วุ้นอโล      ---- +5 ฿")
    print("2.สโนว์มุก     ---- +5 ฿")
    print(f"{gray_code}3.ไข่มุกโนบิ    ---- +5 ฿{reset_code}")
    print("4.เยลลี่ ผลไม้  ---- +5 ฿")
    print(f"{gray_code}5.บุกราวน์ชูการ์ ---- +5 ฿{reset_code}\n")

def topping_not45():
    print("\n1.วุ้นอโล      ---- +5 ฿")
    print("2.สโนว์มุก     ---- +5 ฿")
    print("3.ไข่มุกโนบิ    ---- +5 ฿")
    print(f"{gray_code}4.เยลลี่ ผลไม้  ---- +5 ฿{reset_code}")
    print(f"{gray_code}5.บุกราวน์ชูการ์ ---- +5 ฿{reset_code}\n")

def size_cup():
    print("\n======== Glass =========")
    print("| 1.s      ----- Free ฿ |")
    print("| 2.M      ----- 5 ฿    |")
    print("| 3.L      ----- 10 ฿   |")
    print("| 4.XL     ----- 15 ฿   |")
    print("=========================\n")
