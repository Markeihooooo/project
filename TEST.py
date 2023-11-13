import random
import time
score = 0
nameplayer = []
scoreplayer = []
def countdowmprint(t):
    while t > 0:
        print(t)
        t = t - 1
        time.sleep(1)
seconds = 7
def countdowm(t):
    while t > 0:
        t = t - 1
        time.sleep(1)
seconds = 3

def winner():
    global i
    global ss
    global sss
    # print(nameplayer)
    # print(scoreplayer)
    print("-------------------------------------------------")
    print("     ชื่อ              คะแนน             ลำดับ         ")
    print("-------------------------------------------------")
    for i in range(0,numpy):
        ss = nameplayer[i-1]
        sss = scoreplayer[i-1]
        i = i + 1
        print(i,end="   ")
        print(ss,end="             ")
        print(sss)
        
# winner()

def plus():
    global a
    score1 = 0
    c = 1
    print("********************")
    print("       level 1      ")
    print("********************\n")
    while c <=1:
        x=random.randint(1,9)
        y=random.randint(1,9)
        print(c,") ",x," + ",y)
        z=int(input("ตอบ : "))
        if(x+y==z):
            print("Correct")
            score1 = score1 + 3
            # print("คะแนนของคุณ ",score1,"\n")
        else:
            print("Game Over")
            score1 = score1 - 5
            # print("คะแนนของคุณ ",score1,"\n")
        c +=1
    a = score1 
    # print("-- ด่านที่ 1 คุณมีคะแนนรวมทั้งหมด ",a,"\n") 
# plus()
def minus():
    global b
    c = 1
    score2 = 0
    print("********************")
    print("       level 2      ")
    print("********************\n")
    while c <=5:
        x=random.randint(1,9)
        y=random.randint(1,9)
        print(c,") ",x," - ",y)
        z=int(input("ตอบ : "))
        if(x-y==z):
            print("Correct")
            score2 = score2 + 3
            # print("คะแนนของคุณ ",score2,"\n")
        else:
            print("Game Over")
            score2 = score2 - 5
            # print("คะแนนของคุณ ",score2,"\n")
        c +=1
    b = score2
    # print("-- ด่านที่ 2 คุณมีคะแนนรวมทั้งหมด ",b,"\n") 
# minus()
def plusminus():
    global d
    c = 1
    score3 = 0
    print("********************")
    print("       level 3      ")
    print("********************\n")
    while c <=5:
        mark = random.choice(['+', '-'])
        v=random.randint(1,9)
        x=random.randint(1,9)
        y=random.randint(1,9)
        print(c,") ",x,mark,y,mark,v)
        z=int(input("ตอบ : "))
        if(x-y-v==z):
            print("Correct")
            score3 = score3 + 3
            # print("คะแนนของคุณ ",score3,"\n")
        elif(x-y+v==z):
            print("Correct")
            score3 = score3 + 3
            # print("คะแนนของคุณ ",score3,"\n")
        elif(x+y-v==z):
            print("Correct")
            score3 = score3 + 3
            # print("คะแนนของคุณ ",score3,"\n")
        elif(x+y+v==z):
            print("Correct")
            score3 = score3 + 3
            # print("คะแนนของคุณ ",score3,"\n")
        else:
            print("Game Over")
            score3 = score3 - 5
            # print("คะแนนของคุณ ",score3,"\n")
        c +=1
    d = score3
# plusminus()
def multiply():
    global e
    c = 1
    score4 = 0
    print("********************")
    print("       level 4      ")
    print("********************\n")
    while c <=5:
        x=random.randint(1,9)
        y=random.randint(1,9)
        print(c,") ",x," x ",y)
        z=int(input("ตอบ : "))
        if(x*y==z):
            print("Correct")
            score4 = score4 + 4
            # print("คะแนนของคุณ ",score4,"\n")
        else:
            print("Game Over")
            score4 = score4 - 5
            # print("คะแนนของคุณ ",score4,"\n")
        c +=1
    e = score4
# multiply()
def plusminusmulti():
    global f
    c = 1
    score5 = 0
    print("********************")
    print("       level 5      ")
    print("********************\n")
    while c <=5:
        mark = random.choice(['+', '-'])
        v=random.randint(1,9)
        x=random.randint(1,9)
        y=random.randint(1,9)
        print(c,") ", "(",x,"x",y, ")",mark,v)
        z=int(input("ตอบ : "))
        if(x*y-v==z):
            print("Correct")
            score5 = score5 + 4
            # print("คะแนนของคุณ ",score5,"\n")
        elif(x*y+v==z):
            print("Correct")
            score5 = score5 + 4
            # print("คะแนนของคุณ ",score5,"\n")
        else:
            print("Game Over")
            score5 = score5 - 5
            # print("คะแนนของคุณ ",score5,"\n")
        c +=1
    f = score5
# plusminusmulti()
    

print("*******************************************************************\n")
print("                     welcome to my game !!\n                     ")
print("*******************************************************************")
print("                       ชื่อเกมคณิตคิดไวมั้ย                             ")
print("   จะมีด่านให้เลือกเล่น จำนวน 5 ด่าน ดังนี้                                 ")
print("     1) การบวก          จำนวน 5 ข้อ     ข้อละ 3 คะแนน                ")
print("     2) การลบ           จำนวน 5 ข้อ     ข้อละ 3 คะแนน                ")
print("     3) การบวกและลบ     จำนวน 10 ข้อ    ข้อละ 3 คะแนน                ")
print("     4) การคูณ           จำนวน 5 ข้อ     ข้อละ 4 คะแนน                ")
print("     5) การบวกลบและคูณ   จำนวน 5 ข้อ     ข้อละ 4 คะแนน            \n ")
print("  เวลาในการเล่นแต่ละข้อ คือ 7 วินาที หากไม่ตอบหรือตอบผิด คะแนนจะลบ 5     ")
print("                                                                 ")
print("*******************************************************************")



global numpy
while True:
    level =(input("\nด่านสูงสุดที่ต้องการเล่น (1-5): "))
    if level.isdigit():
        level = int(level)
        if level <= 5 and not level <= 0:
            while True:

                if level <= 5 and not level <= 0:

                    while True:
                        numpy = input("จำนวนผู้เล่นที่ต้องการเล่น (1-3): ")
                        if numpy.isdigit():
                            numpy = int(numpy)
                            count = 1
                            while count <= numpy :
                                if numpy <= 3 and not numpy <= 0:
                                    print("-----------------------------------")
                                    print("     ด่านสูงสุดที่ต้องการเล่น  : ",level)
                                    print("     จำนวนผู้เล่น          : ",numpy)
                                    print("-----------------------------------")
                                    namepy = input(f"\nชื่อผู้เล่น {count}: ")
                                    print("")
                                    nameplayer.append(namepy) 
                                    print("เกมจะเริ่มต้นใน ") 
                                    countdowmprint(seconds)
                                    print("       เริ่ม!!!!")
                                    print(nameplayer)
                                    # print(scoreplayer)
                                    if level == 1:
                                        plus()
                                        print("รวมคะแนน ด่าน 1 ... ",a)
                                        scoreplayer.append(a)
                                    elif level == 2:
                                        plus()
                                        minus()
                                        print("รวมคะแนน ด่าน 2 ... ",a+b)
                                        scoreplayer.append(a+b)
                                    elif level == 3:
                                        plus()
                                        minus()
                                        plusminus()
                                        print("รวมคะแนน ด่าน 3 ... ",a+b+d)
                                        scoreplayer.append(a+b+d)
                                    elif level == 4:
                                        plus()
                                        minus()
                                        plusminus()
                                        multiply()
                                        print("รวมคะแนน ด่าน 4 ... ",a+b+d+e)
                                        scoreplayer.append(a+b+d+e)
                                    elif level == 5:
                                        plus()
                                        minus()
                                        plusminus()
                                        multiply()
                                        plusminusmulti()
                                        print("รวมคะแนน ด่าน 5 ... ",a+b+d+e+f)
                                        scoreplayer.append(a+b+d+e+f)
                                    count = count + 1
                                else:
                                    print("\nเลือกใหม่อีกครั้ง สามารถมีจำนวนผู้เล่นสูงสุด จำนวน 1-3 คน เท่านั้น!!\n")
                                    print("-----------------------------------------------------------")
                                
                        
                        else:print("เลือกใหม่อีกครั้ง สามารถมีจำนวนผู้เล่นสูงสุด จำนวน 1-3 คน เท่านั้น!!")
                        break
                else:print("เลือกใหม่อีกครั้ง ด่านมีจำนวน  1-5 ด่าน เท่านั้น!!")  
                
                break  

        else:print("เลือกใหม่อีกครั้ง ด่านมีจำนวน  1-5 ด่าน เท่านั้น!!")
    else:print("กรุณาใส่เฉพาะตัวเลข")
    
    break
winner()
