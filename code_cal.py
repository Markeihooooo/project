##################################
topping_list = ["วุ้นอโล", "สโนว์มุก","ไข่มุกโนบิ","เยลลี่ผลไม้", "บุกราวน์ชูการ์ ", "คาราเมล", "สตอเบอรี่", "ไข่มุกราวน์ชูการ์", "บุกคริสตัส", "ราสเบอรี่"]
topping_price = [10, 10, 10, 10, 10, 10, 10, 15, 15, 10]
import menu
current_price = menu.price_use()
topping_item = " "
topping_numberall = [] #ทำให้ท๊อปปิ้งสีดำ
result = 0



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
# topping_check(topping_numberall)0



while True:
    topping_want = input("\nคุณต้องการใส่ท็อปปิ้งกี่อย่าง สูงสุดใส่ได้ 3 อย่าง\n0 = ยกเลิกท๊อปปิ้ง \nต้องการใส่กี่อย่าง >>>: ")

    try:
        while True:
            if topping_want == "0" or 0 :break
            topping_want = int(topping_want)
            if topping_want <=3 :
                topping_showall = menu.topping_showall()
            
                if topping_want == 1 :  # ต้องการท๊อปปิ้ง 1 อย่าง
                    topping_number1 = int(input("รายการท๊อปปิ้งที่คุณต้องการ : "))
                    if topping_number1 > 10 :
                        continue
                    topping_select = topping_list[topping_number1-1]
                    print("###################################\nรายการที่คุณเลือก : ",topping_select,"\n")
                    topping_numberall.append(topping_number1)
                    topping_check(topping_numberall)

                    
                    while True:#check topping
                        cheack_topping = input("คุณต้องการดำเนินการต่อหรือไม่ \n1.ดำเนินการต่อไป   2.เปลี่ยนท็อปปิง   9.เลือกจำนวนท็อปปิงใหม่   0.ยกเลิกท็อปปิง(ดำเนินการต่อไป) \n>>>: ")
                        
                        if cheack_topping == "1":
                            menu.set_price(menu.price_use() + topping_price[topping_number1 - 1])
                            break
                        elif cheack_topping == "2":
                            topping_select = ""
                            topping_numberall = []
                            result = 0
                            break
                        
                        elif cheack_topping == "0":
                            topping_select = ""
                            topping_numberall = []
                            result = 0
                            break
                        elif cheack_topping == "9":
                            topping_select = ""
                            topping_numberall = []
                            topping_want = " "
                            result = 0
                            print(topping_list)
                            break
                        else:
                            print("\nโปรดป้อนตัวเลข 1, 2, 9, หรือ 0 เท่านั้น\n")
                    if cheack_topping != "2" : break
                
            
                    
                elif topping_want == 2 : # ต้องการท๊อปปิ้ง 2 อย่าง
                    topping_number1 = int(input("รายการท๊อปปิ้ง ที่ 1 : "))
                    topping_select = topping_list[topping_number1-1]
                    print("###################################\nรายการที่คุณเลือก : ",topping_select,"\n")
                    topping_numberall.append(topping_number1)
                    topping_check(topping_numberall)
                    # topping_numberall.append(topping_number1)
                    

                    topping_number2 = int(input("รายการท๊อปปิ้ง ที่ 2 : "))
                    # topping_numberall.append(topping_number2)
                    topping_select = topping_select +" "+ topping_list[topping_number2-1]
                    print("###################################\nรายการที่คุณเลือก : ", end='')
                    print(topping_select,"\n")
                    topping_numberall.append(topping_number2)
                    topping_check(topping_numberall)

                    result = result + topping_price[topping_number1 - 1] + topping_price[topping_number2 - 1]
                    while True:
                        cheack_topping = input("คุณต้องการดำเนินการต่อหรือไม่ \n1.ดำเนินการต่อไป   2.เปลี่ยนท็อปปิง   9.เลือกจำนวนท็อปปิงใหม่   0.ยกเลิกท็อปปิง(ดำเนินการต่อไป) \n>>>: ")
                        
                        if cheack_topping == "1":
                            menu.set_price(menu.price_use() + result)
                            break
                        elif cheack_topping == "2":
                            topping_select = ""
                            topping_numberall = []
                            result = 0
                            break
                        
                        elif cheack_topping == "0":
                            topping_select = ""
                            topping_numberall = []
                            result = 0
                            break

                        elif cheack_topping == "9":
                            topping_select = ""
                            topping_numberall = []
                            topping_want = " "
                            result = 0
                            print(topping_list)
                            break
                        else:
                            print("\nโปรดป้อนตัวเลข 1, 2, 9, หรือ 0 เท่านั้น\n")
                    if cheack_topping != "2" : break

                    


                elif topping_want == 3 :# ต้องการท๊อปปิ้ง 3 อย่าง
                    topping_number1 = int(input("รายการท๊อปปิ้ง ที่ 1 : "))
                    topping_select = topping_list[topping_number1-1]
                    print("###################################\nรายการที่คุณเลือก : ",topping_select,"\n")
                    topping_numberall.append(topping_number1)
                    topping_check(topping_numberall)
                    # topping_numberall.append(topping_number1)
                    
                    topping_number2 = int(input("รายการท๊อปปิ้ง ที่ 2 : "))
                    print("รายการที่คุณเลือก : ",topping_list[topping_number2-1],"\n")
                    topping_select = topping_select +" "+ topping_list[topping_number2-1]
                    topping_numberall.append(topping_number2)
                    topping_check(topping_numberall)
                    # topping_numberall.append(topping_number2)

                    topping_number3 = int(input("รายการท๊อปปิ้ง ที่ 3 : "))   
                    # topping_numberall.append(topping_number3)                 
                    topping_select = topping_select +" "+ topping_list[topping_number3-1]
                    print("###################################\nรายการที่คุณเลือก : ", end='')
                    print(topping_select,"\n")
                    topping_numberall.append(topping_number3)
                    topping_check(topping_numberall)
                    
                    result = result + topping_price[topping_number1 - 1] + topping_price[topping_number2 - 1] + topping_price[topping_number3 - 1]
                    while True:
                        cheack_topping = input("คุณต้องการดำเนินการต่อหรือไม่ \n1.ดำเนินการต่อไป   2.เปลี่ยนท็อปปิง   9.เลือกจำนวนท็อปปิงใหม่   0.ยกเลิกท็อปปิง(ดำเนินการต่อไป) \n>>>: ")
                        
                        if cheack_topping == "1":
                            menu.set_price(menu.price_use() + result)
                            break
                        elif cheack_topping == "2":
                            topping_select = ""
                            topping_numberall = []
                            result = 0
                            break
                        
                        elif cheack_topping == "0":
                            topping_select = ""
                            topping_numberall = []
                            result = 0
                            break

                        elif cheack_topping == "9":
                            topping_select = ""
                            topping_numberall = []
                            topping_want = " "
                            result = 0
                            print(topping_list)
                            break
                        else:
                            print("\nโปรดป้อนตัวเลข 1, 2, 9, หรือ 0 เท่านั้น\n")
                    if cheack_topping != "2" : break
                    

                
                else:
                    topping_want = []
                    continue

                if cheack_topping == "9" or cheack_topping == 9:
                                topping_select = " "
                                topping_numberall = []
                                topping_want = " "
                                continue
                
            elif topping_want > 3 or topping_want == 0 :
                topping_want = " "
                print("\n***ใส่สูงสุดได้แค่ 3 รายการ***")
                break

            

        if topping_want != " ":
                    break

    except ValueError:
        print("\n***กรุณาใส่เลือกรายการเฉพาะตัวเลข***")
    



















