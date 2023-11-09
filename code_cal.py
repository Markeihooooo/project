##################################
import menu
current_price = menu.price_use()
topping_item = " "
topping_numberall = [] #ทำให้ท๊อปปิ้งสีดำ
result = 0

def topping_check(selected_items):
     for i in range(1, 11):
         if i in selected_items:
             print("\033[1;32m", end='')  # สีเทา
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
    menu.menu()
    menu_number = input("\nเลือกเมนูที่คุณต้องการ : ")
    print("\n\n###########################################################")
    if menu_number.isdigit():#.isdigit คือ ตรวจสอบว่าstrที่รับมาเป็นตัวเลขไหม
        menu_number = int(menu_number)
        if 1 <= menu_number <= 11:
            menu.name_menu = menu.menu_list[menu_number-1]
            menu.set_price(menu.price_use() + menu.menu_price[menu_number-1])

            print("\nเมนูที่คุณเลือก\n\n",menu.menu_list[menu_number-1],"ราคา ",menu.price_use()," ฿\n")#+ menu.menu_price[menu_number-1]

            while True:
                check_menu = input("คุณต้องการดำเนินการต่อหรือไม่\nY = ดำเนินการต่อ\nN = แก้ไขรายการเมนู\n0 = ยกเลิก\n(Y/N) : ")#
                if check_menu == "Y" or check_menu == "y" or check_menu == "1":
                    while True:###################################################
                                print("\n***************** TOPPING *****************\nท๊อปปิ้งของเรามีดังนี้ \n\n",menu.topping_list,"\n")
                                topping_yn = input("คุณต้องการเพิ่ม ท๊อปปิ้ง ไหม \nY.ต้องการเพิ่ม\nN.ไม่ต้องการ\nY/N >>>: ")
                                if topping_yn == ("Y") or topping_yn == ("y"):

                                    while True:
                                        topping_want = input("\nคุณต้องการใส่ท็อปปิ้งกี่อย่าง สูงสุดใส่ได้ 3 อย่าง\n0 = ยกเลิกท๊อปปิ้ง \nต้องการใส่กี่อย่าง >>>: ")

                                        if topping_want.isdigit():
                                            while True:
                                                topping_want = int(topping_want)  
                                                if 1 <= topping_want <= 3:
                                                        if topping_want == "0" or 0 :break
                                                        if topping_want <=3 :
                                                            topping_showall = menu.topping_showall()
                                                            if topping_want == 1 :  # ต้องการท๊อปปิ้ง 1 อย่าง
                                                                while True:
                                                                    topping_number1 = input("รายการท๊อปปิ้งที่คุณต้องการ  ") ## แก้ไข
                                                                    if topping_number1.isdigit():
                                                                        topping_number1 = int(topping_number1)
                                                                        if topping_number1 > 10 or topping_number1 < 1:
                                                                            menu.topping_showall()
                                                                            continue
                                                                        elif topping_want == " ":
                                                                            print("คุณยังไม่ได้กรอกข้อมูล")
                                                                            menu.topping_showall()
                                                                            continue
                                                                        else:
                                                                            menu.topping_showall()
                                                                            pass
                                                                        topping_select = menu.topping_list[topping_number1-1]
                                                                        print("###################################\nรายการที่คุณเลือก : ",topping_select,"\n")
                                                                        topping_numberall.append(topping_number1)
                                                                        topping_check(topping_numberall)
                                                                        break
                                                                    else:
                                                                        print("โปรดป้อนตัวเลขเท่านั้น ")
                                                                        menu.topping_showall()

                                                                
                                                                while True:#check topping
                                                                    cheack_topping = input("คุณต้องการดำเนินการต่อหรือไม่ \n1.ดำเนินการต่อไป   2.เปลี่ยนท็อปปิง   9.เลือกจำนวนท็อปปิงใหม่   0.ยกเลิกท็อปปิง(ดำเนินการต่อไป) \n>>>: ")
                                                                    
                                                                    if cheack_topping == "1":
                                                                        menu.set_price(menu.price_use() + menu.topping_price[topping_number1 - 1])
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
                                                                        print(menu.topping_list)
                                                                        break


                                                                    else:
                                                                        print("\nโปรดป้อนตัวเลข 1, 2, 9, หรือ 0 เท่านั้น\n")
                                                                if cheack_topping != "2" : break
                                                                else : continue

################################################################################################################################################################
                                                            
                                                            elif topping_want == 2 : # ต้องการท๊อปปิ้ง 2 อย่าง
                                                                while True:
                                                                    topping_number1 = (input("รายการท๊อปปิ้ง ที่ 1 : "))
                                                                    if topping_number1.isdigit():
                                                                        topping_number1 = int(topping_number1)
                                                                        if topping_number1 > 10 or topping_number1 < 1:
                                                                            menu.topping_showall()
                                                                            continue
                                                                        
                                                                        elif topping_want == " ":
                                                                            print("คุณยังไม่ได้กรอกข้อมูล")
                                                                            menu.topping_showall()
                                                                            continue

                                                                        else:
                                                                            menu.topping_showall()
                                                                            pass

                                                                        topping_select = menu.topping_list[topping_number1-1]
                                                                        print("###################################\nรายการที่คุณเลือก : ",topping_select,"\n")
                                                                        topping_numberall.append(topping_number1)
                                                                        topping_check(topping_numberall)
                                                                        break
                                                                    else:
                                                                        print("โปรดป้อนตัวเลขเท่านั้น ")
                                                                        menu.topping_showall()
                                                                while True:
                                                                    
                                                                    topping_number2 = (input("รายการท๊อปปิ้ง ที่ 2 : "))
                                                                    if topping_number2.isdigit():
                                                                        topping_number2 = int(topping_number2)
                                                                        if topping_number2 > 10 or topping_number2 < 1 :
                                                                            topping_check(topping_numberall)
                                                                            print("คุณกรอกรายการที่ไม่ถูกต้อง")
                                                                            continue
                                                                        
                                                                        elif topping_number2 == topping_number1:
                                                                            print("กรุณาเลือกรายการที่ไม่เหมือนกัน กรุณาเลือกรายการที่ 2 ใหม่ ")
                                                                            topping_check(topping_numberall)
                                                                            continue
                                                                    elif topping_want == " ":
                                                                            print("คุณยังไม่ได้กรอกข้อมูล")
                                                                            topping_check(topping_numberall)
                                                                            continue
                                                                    else:
                                                                        topping_check(topping_numberall)
                                                                        continue
                                                                    break
                                                                
                                                                
                                                                topping_select = topping_select +" "+ menu.topping_list[topping_number2-1]
                                                                print("###################################\nรายการที่คุณเลือก : ", end='')
                                                                print(topping_select,"\n")
                                                                topping_numberall.append(topping_number2)
                                                                topping_check(topping_numberall)
                                                                result = result + menu.topping_price[topping_number1 - 1] + menu.topping_price[topping_number2 - 1]
                                                                
                                                                

                                                                                                                                
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
                                                                        print(menu.topping_list)
                                                                        break
                                                                    else:
                                                                        print("\nโปรดป้อนตัวเลข 1, 2, 9, หรือ 0 เท่านั้น\n")
                                                                if cheack_topping != "2" : break
                                                                else : continue
                                                            
                                                                
                                                            
                                                            elif topping_want == 3 :# ต้องการท๊อปปิ้ง 3 อย่าง
                                                                while True:
                                                                    topping_number1 = input("รายการท๊อปปิ้ง ที่ 1 : ")
                                                                    if topping_number1.isdigit():
                                                                        topping_number1 = int(topping_number1)
                                                                        if topping_number1 > 10 or topping_number1 < 1 :
                                                                            menu.topping_showall()
                                                                            continue

                                                                        elif topping_want == " ":
                                                                            menu.topping_showall()
                                                                            continue

                                                                        else:
                                                                            menu.topping_showall
                                                                            pass
                                                                    
                                                                        topping_select = menu.topping_list[topping_number1-1]
                                                                        print("###################################\nรายการที่คุณเลือก : ",topping_select,"\n")
                                                                        topping_numberall.append(topping_number1)
                                                                        topping_check(topping_numberall)
                                                                        break
                                                                    else:
                                                                        print("โปรดป้อนตัวเลขเท่านั้น ")
                                                                        menu.topping_showall()
                                                                    
                                                                # topping_numberall.append(topping_number1)
                                                                
                                                                while True:
                                                                    topping_number2 = (input("รายการท๊อปปิ้ง ที่ 2 : "))
                                                                    if topping_number2.isdigit():
                                                                        topping_number2 = int(topping_number2)
                                                                        if topping_number2 > 10 or topping_number2 < 1 :
                                                                            topping_check(topping_numberall)
                                                                            print("คุณกรอกรายการที่ไม่ถูกต้อง")
                                                                            continue
                                                                            
                                                                        elif topping_number2 == topping_number1:
                                                                            print("กรุณาเลือกรายการที่ไม่เหมือนกัน กรุณาเลือกรายการที่ 2 ใหม่ ")
                                                                            topping_check(topping_numberall)
                                                                            continue
                                                                    elif topping_want == " ":
                                                                            print("คุณยังไม่ได้กรอกข้อมูล")
                                                                            topping_check(topping_numberall)
                                                                            continue
                                                                    

                                                                    else:
                                                                        topping_check(topping_numberall)
                                                                        continue

                                                                    break
                                                                    
                                                                    
                                                                topping_select = topping_select +" "+ menu.topping_list[topping_number2-1]
                                                                print("###################################\nรายการที่คุณเลือก : ", end='')
                                                                print(topping_select,"\n")
                                                                topping_numberall.append(topping_number2)
                                                                topping_check(topping_numberall)
                                                                result = result + menu.topping_price[topping_number1 - 1] + menu.topping_price[topping_number2 - 1]

                                                                while True:
                                                                    topping_number3 = (input("รายการท๊อปปิ้ง ที่ 3 : "))
                                                                    if topping_number3.isdigit():
                                                                        topping_number3 = int(topping_number3)
                                                                        if topping_number3 > 10 or topping_number3 < 1 :
                                                                            topping_check(topping_numberall)
                                                                            print("คุณกรอกรายการที่ไม่ถูกต้อง")
                                                                            continue

                                                                        elif topping_number3 == topping_number1 or topping_number3 == topping_number2 :
                                                                            print("กรุณาเลือกรายการที่ไม่เหมือนกัน กรุณาเลือกรายการที่ 2 ใหม่ ")
                                                                            topping_check(topping_numberall)
                                                                            continue
                                                                    elif topping_want == " ":
                                                                            print("คุณยังไม่ได้กรอกข้อมูล")
                                                                            topping_check(topping_numberall)
                                                                            continue
                                                                    else:
                                                                        topping_check(topping_numberall)
                                                                        continue
                                                                    break

                                                                topping_select = topping_select +" "+ menu.topping_list[topping_number3-1]
                                                                print("###################################\nรายการที่คุณเลือก : ", end='')
                                                                print(topping_select,"\n")
                                                                topping_numberall.append(topping_number3)
                                                                topping_check(topping_numberall)
                                                                result = result + menu.topping_price[topping_number1 - 1] + menu.topping_price[topping_number2 - 1] + menu.topping_price[topping_number3 - 1]                                                        
                                                                
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
                                                                            print(menu.topping_list)
                                                                            break
                                                                    else:
                                                                            print("\nโปรดป้อนตัวเลข 1, 2, 9, หรือ 0 เท่านั้น\n")
                                                                if cheack_topping != "2" : break
                                                                else:
                                                                    continue

                                                        elif cheack_topping == "9" or cheack_topping == 9:
                                                            topping_select = " "
                                                            topping_numberall = []
                                                            topping_want = " "
                                                            break
                                                            
                                                elif topping_want > 3 :
                                                    topping_want = " "
                                                    print("\n\033[1;31m***ใส่สูงสุดได้แค่ 3 รายการ***\033[0m")
                                                    break


                                                        

                                                                                        
                                                elif topping_want == 0 or topping_want == "0": #หยุดเมื่อเลือกท๊อป 0 คือไม่ใส่
                                                    break
                                                
                                            if topping_want != " ":    
                                                break

                                        else:
                                            print("\n***กรุณาใส่เลือกรายการเฉพาะตัวเลข***")

                                    break#หาทางออกจากท๊อปิ้ง
                                


                                elif topping_yn == "N" or topping_yn == "n":
                                    break
                        
                    
                elif check_menu == "N" or check_menu == "n":
                    menu.set_price(menu.price_use() - menu.menu_price[menu_number-1])
                    # check_menu == " "
                    break
                else:
                    print("คุณต้องเลือก Y ไปละ")
                    menu.set_price(menu.price_use() - menu.menu_price[menu_number-1])
                    break
                break
            if check_menu == "n" or check_menu == "N":
                continue

            else :break

            
    

print("รายการสินค้า >>>> = " ,menu.price_use() , " ฿")
print("****ขอบคุณที่ใช้บริการ****")


















