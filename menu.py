menu_list = ["ชานมใต้หวัน(Taiwan Mile Tea)","ชานมกาแฟ(Coffee Milk Tea)","ชานมโกโก้(Cocoa Milk Tea)","ชานมเผือก(Taro Milk Tea)","ชานมลิ้นจี่(Lychee Milk Tea)","ชานมคาราเมล(caramel Milk Tea)","ชานมน้ำผึ้ง(Honey Milk Tea)","ชาดำเย็น(Thai Tea)","ชาไทย(Thai Milk Tea)","ชาเขียว(green Tea)","ชานมเเอปเปิ้ล(Appln Milk Tea)"]
topping_list = ["วุ้นอโล", "สโนว์มุก","ไข่มุกโนบิ","เยลลี่ผลไม้", "บุกราวน์ชูการ์", "คาราเมล", "สตอเบอรี่", "ไข่มุกราวน์ชูการ์", "บุกคริสตัส", "ราสเบอรี่"]
menu_price = [19,19,19,19,19,19,19,19,19,19,19,19]
topping_price = [15, 10, 10, 10, 10, 10, 10, 15, 15, 10]
cup_price = [0, 5, 10, 15]
sugar_list = ["ไม่หวาน", "หวานน้อย", "หวานปกติ", "หวานมาก"]
price = 0
name_menu = " "
sugar_selected = []
cup_size = ["8 Oz", "12 Oz", "16 Oz","24 Oz"]

def set_price(new_price):
    global price
    price = new_price


def price_use():
    return price

## Menu
def menu():
    print("        ┌=======================================┐")
    print("        ╎          \033[1;31;40m|ร้าน ตั้งหวังเกือบเจ้ง\033[0m|           ╎")
    print("        └=======================================┘\n")
    print("\033[1;35m=========================== MENU ===========================\033[0m\n")
    print("\033[1;35m|\033[0m 1.ชานมใต้หวัน          (Taiwan Mile Tea)        ----- 19 ฿ \033[1;35m|\033[0m")
    print("\033[1;35m|\033[0m 2.ชานมกาแฟ           (Coffee Milk Tea)        ----- 19 ฿ \033[1;35m|\033[0m")
    print("\033[1;35m|\033[0m 3.ชานมโกโก้           (Cocoa Milk Tea)         ----- 19 ฿ \033[1;35m|\033[0m")
    print("\033[1;35m|\033[0m 4.ชานมเผือก           (Taro Milk Tea)          ----- 19 ฿ \033[1;35m|\033[0m")
    print("\033[1;35m|\033[0m 5.ชานมลิ้นจี่            (Lychee Milk Tea)        ----- 19 ฿ \033[1;35m|\033[0m")
    print("\033[1;35m|\033[0m 6.ชานมคาราเมล        (caramel Milk Tea)       ----- 19 ฿ \033[1;35m|\033[0m")
    print("\033[1;35m|\033[0m 7.ชานมน้ำผึ้ง           (Honey Milk Tea)         ----- 19 ฿ \033[1;35m|\033[0m")
    print("\033[1;35m|\033[0m 8.ชาดำเย็น            (Thai Tea)               ----- 19 ฿ \033[1;35m|\033[0m")
    print("\033[1;35m|\033[0m 9.ชาไทย              (Thai Milk Tea)          ----- 19 ฿ \033[1;35m|\033[0m")
    print("\033[1;35m|\033[0m 10.ชาเขียว            (green Tea)              ----- 19 ฿ \033[1;35m|\033[0m")
    print("\033[1;35m|\033[0m 11.ชานมเเอปเปิ้ล       (Appln Milk Tea)         ----- 19 ฿ \033[1;35m|\033[0m\n")
    print("\033[1;31m0.ยกเลิกการสั่งซื้อ\033[0m")
    print("\033[1;35m============================================================\033[0m")

def topping_showall():
    print("\033[1;35m==================== topping ==========================\033[0m")
    print("\n1.วุ้นอโล        ---- +15 ฿    2.สโนว์มุก       ---- +10 ฿")
    print("3.ไข่มุกโนบิ      ---- +10 ฿    4.เยลลี่ ผลไม้    ---- +10 ฿")
    print("5.บุกราวน์ชูการ์   ---- +10 ฿    6.คาราเมล      ---- +10 ฿")
    print("7.สตอเบอรี่      ---- +10 ฿    8.ไข่มุกราวน์ชูการ์ ---- +15 ฿")
    print("9.บุกคริสตัส      ---- +15 ฿    10.ราสเบอรี่     ---- +10 ฿\n")
    print("\033[1;35m=======================================================\033[0m")


def size_cup():
    print("\n======== Glass ==========")
    print("| 1.8 Oz    ----- Free ฿ |")
    print("| 2.12 Oz    ----- 5 ฿   |")
    print("| 3.16 Oz    ----- 10 ฿  |")
    print("| 4.24 Oz    ----- 15 ฿  |")
    print("| 0.ยกเลิกรายการ          |")
    print("==========================\n")



def sugar_choice():
    print("\n======== Sugar =========")
    print("|      1.ไม่หวาน        |")
    print("|      2.หวานน้อย       |")
    print("|      3.หวานปกติ       |")
    print("|      4.หวานมาก       |")
    print("========================")




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



