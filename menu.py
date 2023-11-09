menu_list = ["ชานมใต้หวัน(Taiwan Mile Tea)","ชานมกาแฟ(Coffee Milk Tea)","ชานมโกโก้(Cocoa Milk Tea)","ชานมเผือก(Taro Milk Tea)","ชานมลิ้นจี่(Lychee Milk Tea)","ชานมคาราเมล(caramel Milk Tea)","ชานมน้ำผึ้ง(Honey Milk Tea)","ชาดำเย็น(Thai Tea)","ชาไทย(Thai Milk Tea)","ชาเขียว(green Tea)","ชานมเเอปเปิ้ล(Appln Milk Tea)"]
topping_list = ["วุ้นอโล", "สโนว์มุก","ไข่มุกโนบิ","เยลลี่ผลไม้", "บุกราวน์ชูการ์ ", "คาราเมล", "สตอเบอรี่", "ไข่มุกราวน์ชูการ์", "บุกคริสตัส", "ราสเบอรี่"]
menu_price = [19,19,19,19,19,19,19,19,19,19,19,19]
topping_price = [15, 10, 10, 10, 10, 10, 10, 15, 15, 10]
price = 0
name_menu = " "



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
    print("| 9.ชาไทย              (Thai Milk Tea)          ----- 19 ฿ |")
    print("| 10.ชาเขียว            (green Tea)              ----- 19 ฿ |")
    print("| 11.ชานมเเอปเปิ้ล       (Appln Milk Tea)         ----- 19 ฿ |\n")
    print("0.ยกเลิกการสั่งซื้อ")
    print("============================================================")

def topping_showall():
    print("\n1.วุ้นอโล        ---- +10 ฿    2.สโนว์มุก       ---- +10 ฿")
    print("3.ไข่มุกโนบิ      ---- +10 ฿    4.เยลลี่ ผลไม้    ---- +10 ฿")
    print("5.บุกราวน์ชูการ์   ---- +10 ฿    6.คาราเมล      ---- +10 ฿")
    print("7.สตอเบอรี่      ---- +10 ฿    8.ไข่มุกราวน์ชูการ์ ---- +15 ฿")
    print("9.บุกคริสตัส      ---- +15 ฿    10.ราสเบอรี่     ---- +10 ฿\n")

def size_cup():
    print("\n======== Glass =========")
    print("| 1.s      ----- Free ฿ |")
    print("| 2.M      ----- 5 ฿    |")
    print("| 3.L      ----- 10 ฿   |")
    print("| 4.XL     ----- 15 ฿   |")
    print("=========================\n")








# def topping_check(selected_items):
#     print(selected_items)
#     for i in range(1, 11):
#         if i in selected_items:
#             print("\033[1;30m", end='')  # สีเทา
#         else:
#             print("\033[0m", end='')  # สีปกติ
        
#         if  i == 1:
#             print("1.วุ้นอโล      ---- +15 ฿")
#         elif i == 2:
#             print("2.สโนว์มุก     ---- +10 ฿")
#         elif i == 3:
#             print("3.ไข่มุกโนบิ    ---- +10 ฿")
#         elif i == 4:
#             print("4.เยลลี่ ผลไม้  ---- +10 ฿")
#         elif i == 5:
#             print("5.บุกราวน์ชูการ์  ---- +15 ฿")
#         elif i == 6:
#             print("6.คาราเมล     ---- +10 ฿")
#         elif i == 7:
#             print("7.สตอเบอรี่     ---- +10 ฿")
#         elif i == 8:
#             print("8.ไข่มุกราวน์ชูการ์ ---- +15 ฿")
#         elif i == 9:
#             print("9.บุกคริสตัส      ---- +15 ฿")
#         elif i == 10:
#             print("10.ราสเบอรี่      ---- +10 ฿")
    
#     print("\033[0;37;40m", end='')  # คืนสีปกติ



