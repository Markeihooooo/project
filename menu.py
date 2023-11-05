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
    print("\n1.วุ้นอโล      ---- +5 ฿")
    print("2.สโนว์มุก     ---- +5 ฿")
    print("3.ไข่มุกโนบิ    ---- +5 ฿")
    print("4.เยลลี่ ผลไม้  ---- +5 ฿")
    print("5.บุกราวน์ชูการ์ ---- +5 ฿\n")

def topping_not1():
    print(f"\n{gray_code}1.วุ้นอโล      ---- +5 ฿{reset_code}")
    print("2.สโนว์มุก     ---- +5 ฿")
    print("3.ไข่มุกโนบิ    ---- +5 ฿")
    print("4.เยลลี่ ผลไม้  ---- +5 ฿")
    print("5.บุกราวน์ชูการ์ ---- +5 ฿\n")

