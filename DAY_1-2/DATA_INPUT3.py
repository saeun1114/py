a = input('입력:')
print(a, 3 * ("\n")) # a 출력 후 줄 바꿈 x 3
print(a, a, a) # a를 연속 3번 출력

b, c = input('문자 2개를 입력해주세요 : ').split() # 문자 2개 입력, 공백 기준 분리, 입력에 메시지 삽입
print(b + c + '\n') # b와 c를 합쳐 출력 후 줄바꿈
print(b, '\n' + c) # b 출력 및 줄바꿈에 c를 합쳐 출력

d, e = input('문자 2개를 입력해주세요, 콤마 구분 : ').split(',') # 문자 2개 입력, 콤마 기준 분리, 입력에 메시지 삽입
print(d, e)

f, g = input('문자 2개를 입력해주세요, 콤마 구분, 1개 제한 : ').split(',', 1) # 문자 2개 입력, 콤마 기준 분리, 1개 제한, 입력에 메시지 삽입
print(f, g, sep = ',') # , 로 구분하여 출력

