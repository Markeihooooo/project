##################################
topping_list = ["วุ้นอโล", "สโนว์มุก","ไข่มุกโนบิ","เยลลี่ผลไม้", "บุกราวน์ชูการ์ ", "คาราเมล", "สตอเบอรี่", "ไข่มุกราวน์ชูการ์", "บุกคริสตัส", "ราสเบอรี่"]
import menu
current_price = menu.price_use()
topping_item = " "
topping_numberall = [] #ทำให้ท๊อปปิ้งสีดำ

def topping_check(selected_items):
     for i in range(1, 11):
         if i in selected_items:
             print("\033[1;30m", end='')  # สีเทา
         else:
             print("\033[0m", end='')  # สีปกติ
        
         if  i == 1:
             print("1.วุ้นอโล        ---- +15 ฿", end='')
         elif i == 2:
             print("    2.สโนว์มุก       ---- +10 ฿")
         elif i == 3:
             print("3.ไข่มุกโนบิ      ---- +10 ฿", end='')
         elif i == 4:
             print("    4.เยลลี่ ผลไม้    ---- +10 ฿")
         elif i == 5:
           print("5.บุกราวน์ชูการ์   ---- +10 ฿", end='')
         elif i == 6:
            print("    6.คาราเมล      ---- +10 ฿")
         elif i == 7:
             print("7.สตอเบอรี่      ---- +10 ฿", end='')
         elif i == 8:
             print("    8.ไข่มุกราวน์ชูการ์ ---- +15 ฿")
         elif i == 9:
             print("9.บุกคริสตัส      ---- +15 ฿", end='')
         elif i == 10:
             print("    10.ราสเบอรี่     ---- +10 ฿\n")
     print("\033[0;37;40m", end='')
# topping_check(topping_numberall)



while True:
    topping_want = input("คุณต้องการใส่ท็อปปิ้งกี่อย่าง สูงสุดใส่ได้ 3 อย่าง\nต้องการใส่กี่อย่าง >>>: ")
    
    try:
        while True:
            topping_showall = menu.topping_showall()
            topping_want = int(topping_want)
            if topping_want == 1 :  
                topping_number1 = int(input("รายการท๊อปปิ้งที่คุณต้องการ : "))
                topping_select = topping_list[topping_number1-1]
                print("รายการที่คุณเลือก : ",topping_select)
                topping_numberall.append(topping_number1)
                topping_check(topping_numberall)
                cheack_topping = input("คุณต้องการดำเนินการต่อหรือไม่ \n1.ดำเนินการต่อไป   2.เปลี่ยนท๊อปปิ้ง   3.ยกเลิกท๊อปปิ้ง \n>>>: ")
                if cheack_topping == "1":
                    break
                elif cheack_topping == "2":
                    topping_select = ""
                    topping_numberall = []
                    continue
                elif cheack_topping == "3":
                    topping_select = ""
                    topping_numberall = ""
                    break
        
                
            elif topping_want == 2 :
                topping_number1 = int(input("รายการท๊อปปิ้ง ที่ 1 : "))
                print("รายการที่คุณเลือก : ",topping_list[topping_number1-1])
                topping_numberall.append(topping_number1)
                topping_number2 = int(input("รายการท๊อปปิ้ง ที่ 2 : "))
                topping_numberall.append(topping_number1)
                print("รายการที่คุณเลือก : ",topping_list[topping_number2-1])
                break
            elif topping_want == 3 :
                topping_number1 = int(input("รายการท๊อปปิ้ง ที่ 1 : "))
                print("รายการที่คุณเลือก : ",topping_list[topping_number1-1])
                topping_number2 = int(input("รายการท๊อปปิ้ง ที่ 2 : "))
                print("รายการที่คุณเลือก : ",topping_list[topping_number2-1])
                topping_number3 = int(input("รายการท๊อปปิ้ง ที่ 3 : "))
                print("รายการที่คุณเลือก : ",topping_list[topping_number3-1])
                break
            break
        break
    except ValueError:
        print("***กรุณาใส่เลือกรายการเฉพาะตัวเลข***")
    

print(topping_select)
















