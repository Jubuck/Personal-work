def School(time):
    if(time < 7.0):
        print("학교 가야지")
    elif(time >= 7.0 and total <= 8.0):
        print("학교 갈까 말까")
    else:
        print("포기, 더 자자")

def Class(time, ctime):
    total = 0
    ctotal = 0
    
    t = int(time)
    m = (time * 100) % 100
    total = t * 60 + m
    
    ct = int(ctime)
    cm = (ctime * 100) % 100
    ctotal = ct * 60 + cm
    
    totals = ctotal - total

    if(totals >= 120):
        print("학교 가야지")
    elif(totals >= 20 and totals < 120):
        print("학교 가야겟지...")
    else:
        print("포기, 더 자자 난 틀렸어")
    return totals

def chrd(money):
    i = 0
    print(' ')
    print("==탈수 있는 목록==")
    if(money >= 10000):
        while i <= 3:
            print(ride[i])
            i = i + 1
    elif(money >= 3000):
        while i <= 2:
            print(ride[i])
            i = i + 1
    elif(money >= 2000):
        while i <= 1:
            print(ride[i])
            i = i + 1
    else:
        print(ride[0])
    print(' ')
def Goto(time,money):
    print("수업까지 남은 시간 : ",int(time),"분")
    chrd(money)
    if(time > 60):
        HowTo(money,time)

    elif(time > 40):
        HowTo(money,time)
        if((money < 2000)):
             print("지각입니다. 화이팅!")
    elif(time >= 30):
        HowTo(money,time)
        if((money < 3000)):
            print("지각입니다. 화이팅!")

    elif(time < 30):
        HowTo(money,time)
        
        if(money < 10000):
            print("지각입니다. 화이팅!")

def HowTo(money, time):
    if(money < 2000 or time > 60):
        print("자전거를 추천드립니다.")
    elif(money > 3000 and time > 40):
         print("버스를 추천드립니다.")
    elif(money > 1000 and time > 30):
         print("전철을 추천드립니다.")
    else:
         print("택시를 추천드립니다.")

def Select(rides):
    money = 0
    if(rides == '버스'):
        money = 2000
    elif(rides == '전철'):
        money = 3000
    elif(rides == '택시'):
        money = 10000
    
    return money

def menu_list(): #메뉴 차림표
    menu_list = ('라면', '우동', '비빔밥')
    money = (2000 ,2500, 3000)
    print("메뉴의 종류는", menu_list, "(이)가 있습니다.")
    print("가격은 각각",money,"입니다.")

def menu_money(money): #메뉴와 인원 계산
    pay = 0
    
    if (money >= 3000):
        print("비빔밥을 추천합니다.")
    elif (money >= 2000):
        print("우동을 추천합니다.")
    elif (money >= 1000):
        print("라면을 추천합니다.")
    else:
        print("돈좀 아끼지 그랬어요")

    eat = input("무엇을 먹을지 입력해주십시오 (안먹으면 x): ")

    if (eat == '라면'):
        moneys = 2000
    elif (eat == '우동'):
        moneys = 2500
    elif (eat == '비빔밥'):
        moneys = 3000    
    elif (eat == 'x'):
        moneys = money - 0
    return moneys
        
ride = ('자전거(0원)', '버스(2000원)', '전철(3000원)', '택시(10000원)')    
        
time = float(input("일어난 시간을 입력해 주십시오(ex_ 7.30) : "))

ctime = float(input("첫수업의 시간을 입력해 주십시오(ex_ 9.00) : "))


#School(time)
times = Class(time, ctime)

money = int(input("소지 금액을 입력해주십시오 : "))

Goto(times,money)

rides = input("무엇을 탈지 입력해주십시오 : ")

pay1 = Select(rides)

money = money - pay1
print("잔액 : ",money )

menu_list()
pay2 = menu_money(money)
money = money - pay2
print("잔액 : ",money )

print("집에 가야합니다.")
chrd(money)

rides2 = input("무엇을 탈지 입력해주십시오 : ")

pay3 = Select(rides2)

fmoney = money - pay3

print(rides2, "를 타고 집에 잘 왔습니다.")

print("교통비 : ",pay1+pay3 , "식비 : ",pay2)

print("총 남은용돈은",fmoney,"원 입니다.")

