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


def size_cup():
    print("\n======== Glass =========")
    print("| 1.s      ----- Free ฿ |")
    print("| 2.M      ----- 5 ฿    |")
    print("| 3.L      ----- 10 ฿   |")
    print("| 4.XL     ----- 15 ฿   |")
    print("=========================\n")



gray_code = "\033[1;30m" # กำหนดสี 
reset_code = "\033[0m"


g = int(input("Number"))
i = int(input("Number"))
z = int(input("Number"))
selected_items = [g, i, z]

def topping_showall(selected_items):
    print(selected_items)
    for i in range(1, 6):
        if i in selected_items:
            print("\033[1;30m", end='')  # สีเทา
        else:
            print("\033[0m", end='')  # สีปกติ
        
        if i == 1:
            print("1.วุ้นอโล      ---- +10 ฿")
        elif i == 2:
            print("2.สโนว์มุก     ---- +10 ฿")
        elif i == 3:
            print("3.ไข่มุกโนบิ    ---- +10 ฿")
        elif i == 4:
            print("4.เยลลี่ ผลไม้  ---- +10 ฿")
        elif i == 5:
            print("5.บุกราวน์ชูการ์ ---- +10 ฿")
    
    print("\033[0;37;40m", end='')  # คืนสีปกติ

# ตัวอย่างการใช้งาน
# selected_items = [1, 3]  # เลือกรายการ 1 และ 3
topping_showall(selected_items)
