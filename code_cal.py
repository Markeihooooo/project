##################################
import menu
import time
current_price = menu.price_use()
topping_item = " "
topping_numberall = [] #ทำให้ท๊อปปิ้งสีดำ
result = 0
countdown = 10 


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

def finish_allmenu():
    print(f"Menu you choice : {menu.menu_list[menu_number-1]}",f"Price : {menu.menu_price[menu_number-1]}")
    if topping_numberall:
        print("Topping you choice :", end=" ")
        for number in topping_numberall:
            # print("Topping you choice : ",menu.topping_list[number-1],end=" ")
            print(menu.topping_list[number-1], end=" ")
    else:print("No Topping")
    if topping_numberall:print("\nรวมราคา topping : ",result," ฿")
    print("ความหวาน : ",menu.sugar_selected)
    print("ขนาดแก้ว : ",menu.cup_size[int(cup_check)-1],end=" ")
    if cup_check == "1":print("free cup")
    else:print("ราคา ",menu.cup_price[int(cup_check)-1]," ฿")
    print("ความหวาน : ",menu.sugar_selected)
    print(".\n.\n.\n.\n.\nราคารวมทั้งหมด : ",menu.menu_price[menu_number-1]+result+menu.cup_price[int(cup_check)-1]," ฿")
    


while True:
    menu.menu()
    menu_number = input("\n\033[1;34mPlease choose the menu you want. : \033[0m")
    print("\n\n###########################################################")
    if menu_number.isdigit():#.isdigit คือ ตรวจสอบว่าstrที่รับมาเป็นตัวเลขไหม
        menu_number = int(menu_number)
        if 1 <= menu_number <= 11:
            menu.name_menu = menu.menu_list[menu_number-1]

            print("\n\n\033[1;34mYour chosen menu is\033[0m\n\n",menu.menu_list[menu_number-1],"ราคา ",menu.menu_price[menu_number-1]," ฿\n")#+ menu.menu_price[menu_number-1]

            while True:
                check_menu = input("\033[1;34mคุณต้องการดำเนินการต่อหรือไม่\033[0m\n\n\033[1;32mY = ดำเนินการต่อ\033[0m\n\033[1;33mN = แก้ไขรายการเมนู\033[0m\n\033[1;31m0 = ยกเลิก\033[0m\n\n\033[1;34m[Y/N] :\033[0m ")#
                if check_menu == "Y" or check_menu == "y" or check_menu == "1":
                    menu.set_price(menu.price_use() + menu.menu_price[menu_number-1])

                    while True:###################################################
                                menu.topping_showall()
                                topping_yn = input("\033[1;34m\nDo you want to add toppings ?\n\033[0m \n\033[1;32mY.ต้องการเพิ่ม\033[0m\n\033[1;31mN.ไม่ต้องการ(ดำเนินการต่อ) \033[0m\n\n\033[1;34mY/N >>>:\033[0m ")
                                #ไม่ต้องการ ต้องไปที่เลือกแก้ว
                                if topping_yn == ("Y") or topping_yn == ("y"): 

                                    while True: #ต้องNไปเลือกแก้ว
                                        topping_want = input("\n\033[1;34mHow many toppings do you want to add? Maximum is 3\033[0m\n\n\033[1;31m0 = ยกเลิกท๊อปปิ้ง(ดำเนินการต่อ) \033[0m\n\n\033[1;34mต้องการใส่กี่อย่าง >>>:\033[0m " )

                                        if topping_want.isdigit():
                                            while True:
                                                topping_want = int(topping_want)  
                                                if 1 <= topping_want <= 3:
                                                        if topping_want == "0" or 0 :break
                                                        if topping_want <=3 :
                                                            topping_showall = menu.topping_showall()
                                                            if topping_want == 1 :  # ต้องการท๊อปปิ้ง 1 อย่าง
                                                                while True:
                                                                    topping_number1 = input("\n\033[1;34mรายการท๊อปปิ้งที่คุณต้องการ\033[0m  ") ## แก้ไข
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
                                                                        print("\n\033[1;34mรายการที่คุณเลือก :\033[0m ",topping_select,"\n")
                                                                        topping_numberall.append(topping_number1)
                                                                        topping_check(topping_numberall)
                                                                        break
                                                                    else:
                                                                        print("\n\033[1;31m======= โปรดป้อนตัวเลขเท่านั้น =======\033[0m\n")
                                                                        menu.topping_showall()

                                                                
                                                                while True:#check topping
                                                                    cheack_topping = input("\033[1;34mคุณต้องการดำเนินการต่อหรือไม่\033[0m\n\033[1;32m1.ดำเนินการต่อไป\033[0m   \033[1;33m2.เปลี่ยนท็อปปิง\033[0m \033[1;36m 9.เลือกจำนวนท็อปปิงใหม่\033[0m   \033[1;31m0.ยกเลิกท็อปปิง(เเละดำเนินการต่อไป)\033[0m \n\n>>>: ")
                                                                    
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
                                                            
                                                            elif topping_want == 2 : # ต้องการท๊อปปิ้ง 2 อย่าง
                                                                while True:
                                                                    topping_number1 = (input("\n\033[1;34mรายการท๊อปปิ้ง ที่ 1 : \033[0m"))
                                                                    if topping_number1.isdigit():
                                                                        topping_number1 = int(topping_number1)
                                                                        if topping_number1 > 10 or topping_number1 < 1:
                                                                            menu.topping_showall()
                                                                            continue
                                                                        
                                                                        elif topping_want == " ":
                                                                            print("\033[1;31mคุณยังไม่ได้กรอกข้อมูล\033[0m")
                                                                            menu.topping_showall()
                                                                            continue

                                                                        else:
                                                                            #menu.topping_showall()#เเสดงเมนูอีกรอบ
                                                                            pass

                                                                        topping_select = menu.topping_list[topping_number1-1]
                                                                        print("\n\033[1;34mรายการที่คุณเลือก :\033[0m ",topping_select,"\n")
                                                                        topping_numberall.append(topping_number1)
                                                                        topping_check(topping_numberall)
                                                                        break
                                                                    else:
                                                                        print("\n\033[1;31m======= โปรดป้อนตัวเลขเท่านั้น =======\033[0m\n ")
                                                                        menu.topping_showall()
                                                                while True:
                                                                    
                                                                    topping_number2 = (input("\033[1;34mรายการท๊อปปิ้ง ที่ 2 : \033[0m"))
                                                                    if topping_number2.isdigit():
                                                                        topping_number2 = int(topping_number2)
                                                                        if topping_number2 > 10 or topping_number2 < 1 :
                                                                            topping_check(topping_numberall)
                                                                            print("\033[1;31mคุณกรอกรายการที่ไม่ถูกต้อง\033[0m")
                                                                            continue
                                                                        
                                                                        elif topping_number2 == topping_number1:
                                                                            print("\n\033[1;31mกรุณาเลือกรายการที่ไม่เหมือนกัน กรุณาเลือกรายการที่ 2 ใหม่\033[0m \n")
                                                                            topping_check(topping_numberall)
                                                                            continue
                                                                    elif topping_want == " ":
                                                                            print("\033[1;31mคุณยังไม่ได้กรอกข้อมูล\033[0m")
                                                                            topping_check(topping_numberall)
                                                                            continue
                                                                    else:
                                                                        topping_check(topping_numberall)
                                                                        continue
                                                                    break
                                                                
                                                                
                                                                topping_select = topping_select +" "+ menu.topping_list[topping_number2-1]
                                                                print("\n\033[1;34mรายการที่คุณเลือก :\033[0m  ", end='')
                                                                print(topping_select,"\n")
                                                                topping_numberall.append(topping_number2)
                                                                topping_check(topping_numberall)
                                                                result = result + menu.topping_price[topping_number1 - 1] + menu.topping_price[topping_number2 - 1]
                                                                
                                                                

                                                                                                                                
                                                                while True:
                                                                    cheack_topping = input("\033[1;34mคุณต้องการดำเนินการต่อหรือไม่\033[0m\n\033[1;32m1.ดำเนินการต่อไป\033[0m   \033[1;33m2.เปลี่ยนท็อปปิง\033[0m \033[1;36m 9.เลือกจำนวนท็อปปิงใหม่\033[0m   \033[1;31m0.ยกเลิกท็อปปิง(เเละดำเนินการต่อไป)\033[0m \n\n>>>: ")
                                                                    
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
                                                                    topping_number1 = input("\n\033[1;34mรายการท๊อปปิ้ง ที่ 1 : \033[0m")
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
                                                                        print("\n\033[1;34mรายการที่คุณเลือก :\033[0m ",topping_select,"\n")
                                                                        topping_numberall.append(topping_number1)
                                                                        topping_check(topping_numberall)
                                                                        break
                                                                    else:
                                                                        print("\033[1;31mโปรดป้อนตัวเลขเท่านั้น \033[0m")
                                                                        menu.topping_showall()
                                                                    
                                                                # topping_numberall.append(topping_number1)
                                                                
                                                                while True:
                                                                    topping_number2 = (input("\n\033[1;34mรายการท๊อปปิ้ง ที่ 2 : \033[0m"))
                                                                    if topping_number2.isdigit():
                                                                        topping_number2 = int(topping_number2)
                                                                        if topping_number2 > 10 or topping_number2 < 1 :
                                                                            topping_check(topping_numberall)
                                                                            print("\033[1;31mคุณกรอกรายการที่ไม่ถูกต้อง\033[0m")
                                                                            continue
                                                                            
                                                                        elif topping_number2 == topping_number1:
                                                                            print("\033[1;31mกรุณาเลือกรายการที่ไม่เหมือนกัน กรุณาเลือกรายการที่ 2 ใหม่\033[0m ")
                                                                            topping_check(topping_numberall)
                                                                            continue
                                                                    elif topping_want == " ":
                                                                            print("\033[1;31mคุณยังไม่ได้กรอกข้อมูล\033[0m")
                                                                            topping_check(topping_numberall)
                                                                            continue
                                                                    

                                                                    else:
                                                                        topping_check(topping_numberall)
                                                                        continue

                                                                    break
                                                                    
                                                                    
                                                                topping_select = topping_select +" "+ menu.topping_list[topping_number2-1]
                                                                print("\n\033[1;34mรายการที่คุณเลือก :\033[0m: ", end='')
                                                                print(topping_select,"\n")
                                                                topping_numberall.append(topping_number2)
                                                                topping_check(topping_numberall)
                                                                result = result + menu.topping_price[topping_number1 - 1] + menu.topping_price[topping_number2 - 1]

                                                                while True:
                                                                    topping_number3 = (input("\033[1;34mรายการท๊อปปิ้ง ที่ 3 :\033[0m "))
                                                                    if topping_number3.isdigit():
                                                                        topping_number3 = int(topping_number3)
                                                                        if topping_number3 > 10 or topping_number3 < 1 :
                                                                            topping_check(topping_numberall)
                                                                            print("\033[1;31mคุณกรอกรายการที่ไม่ถูกต้อง\033[0m")
                                                                            continue

                                                                        elif topping_number3 == topping_number1 or topping_number3 == topping_number2 :
                                                                            print("\n\033[1;31mกรุณาเลือกรายการที่ไม่เหมือนกัน กรุณาเลือกรายการที่ 2 ใหม่\033[0m ")
                                                                            topping_check(topping_numberall)
                                                                            continue
                                                                    elif topping_want == " ":
                                                                            print("\033[1;31mคุณยังไม่ได้กรอกข้อมูล\033[0m")
                                                                            topping_check(topping_numberall)
                                                                            continue
                                                                    else:
                                                                        topping_check(topping_numberall)
                                                                        continue
                                                                    break

                                                                topping_select = topping_select +" "+ menu.topping_list[topping_number3-1]
                                                                print("\n\033[1;34mรายการที่คุณเลือก :\033[0m: ", end='')
                                                                print(topping_select,"\n")
                                                                topping_numberall.append(topping_number3)
                                                                topping_check(topping_numberall)
                                                                result = result + menu.topping_price[topping_number3 - 1]                                                        
                                                                
                                                                while True:
                                                                    cheack_topping = input("\033[1;34mคุณต้องการดำเนินการต่อหรือไม่\033[0m\n\033[1;32m1.ดำเนินการต่อไป\033[0m   \033[1;33m2.เปลี่ยนท็อปปิง\033[0m \033[1;36m 9.เลือกจำนวนท็อปปิงใหม่\033[0m   \033[1;31m0.ยกเลิกท็อปปิง(เเละดำเนินการต่อไป)\033[0m \n\n>>>: ")
                                                                        
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

                                                        elif cheack_topping == "9" or cheack_topping == 9: #เปลี่ยนเลือกท๊อปปิ้งใหม่
                                                            topping_select = " "
                                                            topping_numberall = []
                                                            topping_want = " "
                                                            break
                                                            
                                                elif topping_want > 3 : #เลือกท๊อปปิ้งใหม่
                                                    topping_want = " "
                                                    print("\n\033[1;31m***ใส่สูงสุดได้แค่ 3 รายการ***\033[0m")
                                                    break


                                                        

                                                                                        
                                                elif topping_want == 0 or topping_want == "0": #หยุดเมื่อเลือกท๊อป 0 คือไม่ใส่
                                                    break
                                                
                                            if topping_want != " ":    
                                                break

                                        else:
                                            print("\n\033[1;31m***กรุณาใส่เลือกรายการเฉพาะตัวเลข***\033[0m")

                                    break#หาทางออกจากท๊อปิ้ง
                                

 
                                elif topping_yn == "N" or topping_yn == "n": #ออกจากเลืกท๊อปปิ้งและไปเลือกแก้ว
                                    break



                    while True:
                        menu.sugar_choice()
                        sugar_check = input("\033[1;34mกรุณาเลือกความหวานที่คุณต้องการ \033[0m : ") 
                        if sugar_check == "1" :
                            print("คุณเลือกความหวาน : ",menu.sugar_list[int(sugar_check)-1])
                            sugar_sure = input("คุณต้องการเลือกความหวานนี้หรือไม่ (Y/N) : ")
                            if sugar_sure == "Y" or sugar_sure == "y":
                                print("คุณเลือกความหวาน : ",menu.sugar_list[int(sugar_check)-1])
                                menu.sugar_selected.append(menu.sugar_list[int(sugar_check)-1])
                                break
                            else:
                                continue
                            
                        elif sugar_check == "2" :
                            print("คุณเลือกความหวาน : ",menu.sugar_list[int(sugar_check)-1])
                            sugar_sure = input("คุณต้องการใช้ความหวานนี้หรือไม่ (Y/N) : ")
                            if sugar_sure == "Y" or sugar_sure == "y":
                                print("คุณเลือกความหวาน : ",menu.sugar_list[int(sugar_check)-1])
                                menu.sugar_selected.append(menu.sugar_list[int(sugar_check)-1])
                                break
                            else:
                                continue
                            
                        elif sugar_check == "3" :
                            print("คุณเลือกความหวาน : ",menu.sugar_list[int(sugar_check)-1])
                            sugar_sure = input("คุณต้องการใช้ความหวานนี้หรือไม่ (Y/N) : ")
                            if sugar_sure == "Y" or sugar_sure == "y":
                                print("คุณเลือกความหวาน : ",menu.sugar_list[int(sugar_check)-1])
                                menu.sugar_selected.append(menu.sugar_list[int(sugar_check)-1])
                                break
                            else:
                                continue

                        elif sugar_check == "4" :
                            print("คุณเลือกความหวาน : ",menu.sugar_list[int(sugar_check)-1])
                            sugar_sure = input("คุณต้องการใช้ความหวานนี้หรือไม่ (Y/N) : ")
                            if sugar_sure == "Y" or sugar_sure == "y":
                                print("คุณเลือกความหวาน : ",menu.sugar_list[int(sugar_check)-1])
                                menu.sugar_selected.append(menu.sugar_list[int(sugar_check)-1])
                                break
                            else:
                                continue
                        else:
                            print("\n\033[1;31m***กรุณาใส่เลือกรายการเฉพาะตัวเลข***\033[0m")
                            continue


                    menu.size_cup()
                    while True:
                        cup_check = input("คุณต้องการใช้แก้วขนาดเท่าไหร่ (ใส่ตัวเลข) : ")
                        if cup_check == "1" or cup_check == "2" or cup_check == "3" or cup_check == "4":
                            menu.set_price(menu.price_use() + menu.cup_price[int(cup_check) - 1])
                            check_cup = input(f"\033[1;34mยืนยันที่จะเลือกแก้วขนาด  {menu.cup_size[int(cup_check)-1]} (Y/N)\033[0m : ")
                            if check_cup == "Y" or check_cup == "y":
                                
                                finish_allmenu()

                                check_last = input("ยันยันการสั่งเมูนูนี้หรือไม่ (Y/N) : ")
                                if check_last == "Y" or check_last == "y":
                                    while countdown > 0:
                                        print (countdown," วินาที")
                                        (time.sleep(1))
                                        countdown -= 1
                                    break
                                else:continue


                                

                                
                                break
                            elif check_cup == "n" or check_cup =="N":
                                menu.set_price(menu.price_use() - menu.cup_price[int(cup_check) - 1])
                                continue
                            else:continue
                        elif cup_check == "0":break 
                        
                        else:print("\n\033[1;31m***กรุณาใส่ตัวเลข 1, 2, 3, 4 หรือขนาดSize ที่ต้องการ***\033[0m")
                    break





                    
                elif check_menu == "N" or check_menu == "n":
                    
                    # check_menu == " "
                    break
                elif check_menu == "0":
                    break
                else:
                    print("\033[1;31mคุณต้องเลือก Y ไปละ\033[0m")
                    
                    continue
                


            if check_menu == "n" or check_menu == "N":
                continue

            else :break
        break
    break
##########################################################

# if menu_number!= 0 or check_menu != "0" or check_menu != "N" or check_menu != "n":
#     while True:
#         print(check_menu)
#         print("\n\n\033[1;34mYour chosen menu is\033[0m\n\n",menu.menu_list[menu_number-1],"ราคา ",menu.price_use()," ฿\n")
#         menu.size_cup()
#         cup_check = input("คุณต้องการใช้แก้วขนาดเท่าไหร่ (ใส่ตัวเลข) : ")
#         if cup_check == "s" or cup_check == "S" or cup_check == "1":
#                 menu.set_price(menu.price_use() + 0)
#                 break
#         elif cup_check == "m" or cup_check == "M" or cup_check == "2":
#                 menu.set_price(menu.price_use() + 5)
#                 break
#         elif cup_check == "l" or cup_check == "L" or cup_check == "3":
#                 menu.set_price(menu.price_use() + 10)
#                 break
#         elif cup_check == "xl" or cup_check == "XL" or cup_check == "4":
#                 menu.set_price(menu.price_use() + 15)
#                 break
#         else:
#                 print("\n\033[1;31m***กรุณาใส่เลือกรายการเฉพาะตัวเลือกขนาดที่กำหนด ***\033[0m")
#                 continue
        
    

    

            
    

print("\n เมนูที่สั่งเสร็จเรียบร้อยแล้ว\n")
(time.sleep(1))
print("\n\033[1;34m****ขอบคุณที่ใช้บริการ****\033[0m")


















