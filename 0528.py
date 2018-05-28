import random

def Sum(num,leng):
    result=0
    i=0
    
    while i<leng:
        result=result+num[i]
        i=i+1
        
    return result

def Average(num,leng):
    sum1=0
    i=0

    while i<leng:
        sum1 = sum1 + num[i]
        i = i + 1

    result = sum1/5
    
    return result

def maximum(num,leng):
    result = 0
    i = 0
    
    for i in num:
        if result<i:
            result = i
            
    return result
    
def minimum(num,leng):
    result = 0
    i = 0
    
    result = 100
    
    for i in num:
        if result>i:
            result = i
            
    return result

t1 = random.randint(1,100)
t2 = random.randint(1,100)
t3 = random.randint(1,100)
t4 = random.randint(1,100)
t5 = random.randint(1,100)

num=(t1, t2, t3, t4, t5)
print(num)
print('합계 :',Sum(num,5))
print('평균 :',Average(num,5))
print('최대값 :',maximum(num,5))
print('최소값 :',minimum(num,5))
