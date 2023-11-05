def menu():
    print("        ┌=======================================┐")
    print("        ╎          |ร้าน ตั้งหวังเกือบเจ้ง|           ╎")
    print("        └=======================================┘\n")
    print("======================== MENU ==============================\n")
    print("| 1.ชานมใต้หวัน          (Taiwan Mile Tea)        ----- 19 ฿ |")
    print("| 2.ชานมกาแฟ           (Coffee Milk Tea)        ----- 19 ฿ |")
    print("| 3.ชานมโกโก้           (Cocoa Milk Tea)         ----- 19 ฿ |")
    print("| 5.ชานมเผือก           (Taro Milk Tea)          ----- 19 ฿ |")
    print("| 6.ชานมลิ้นจี่            (Lychee Milk Tea)        ----- 19 ฿ |")
    print("| 7.ชานมคาราเมล        (caramel Milk Tea)       ----- 19 ฿ |")
    print("| 8.ชานมน้ำผึ้ง           (Honey Milk Tea)         ----- 19 ฿ |")
    print("| 9.ชาดำเย็น            (Thai Tea)               ----- 19 ฿ |")
    print("| 10.ชาไทย             (Thai Milk Tea)          ----- 19 ฿ |")
    print("| 11.ชาเขียว            (green Tea)              ----- 19 ฿ |")
    print("| 12.ชานมเเอปเปิ้ล       (Appln Milk Tea)         ----- 19 ฿ |\n")
    print("============================================================")

price = 0 

def set_price(new_price):
    global price
    price = new_price


def price_use():
    return price