import random   #랜덤값 지정
from datetime import datetime       #시간지정

i = 0           #while문 만들기
total_point = 0           #점수
time_diff = 0
list_word = ['aa', 'bb', 'cc', 'dd', 'ee',]  #리스트

while i < 3:    #반복문 지정
    i = i + 1
    rand_val = (random.choice(list_word))               #리스트 안에 랜덤 지정
    print(rand_val)                             #랜덤 프린트
    start_time = datetime.now()                  #시간
    input_val = input()                         #입력
    
    if input_val == rand_val:                           #정답일 경우
        total_point = total_point + 10                      #점수추가
        end_time = datetime.now()              #지난 시간
        time_diff = end_time - start_time                       #몇초인지
        timediff_sec = time_diff.seconds                   
        print("당신의 점수는 %d 입니다 당신의 시간은 %d 입니다" %(total_point, timediff_sec))   #결과
    else:
        print("틀림")                                                   #결과
