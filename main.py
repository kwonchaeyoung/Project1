'''
일자 : 2024년 09월 30일 월요일
교재 : 깃특강2-깃 버전 관리 기본(Ver1.3.1)p.pdf p.36
'''

# 함수 선언부
def add_func(n1, n2):
    return n1 + n2

def sub_func(n1, n2):
    return n1 - n2

def mul_func(n1, n2):
    return n1 * n2

def div_func(n1, n2):
    return n1 / n2

def squ_func(n1, n2):
    return n1 ** n2

# 전역 변수부
num1, num2, res = 100, 200, 0

# 메인 코드부
res = add_func(num1, num2)
print(num1, '+', num2, '=', res)

res = sub_func(num1, num2)
print(num1, '-', num2, '=', res)

res = mul_func(num1, num2)
print(num1, '*', num2, '=', res)

res = div_func(num1, num2)
print(num1, '/', num2, '=', res)

res = squ_func(num1, num2)
print(num1, '^', num2, '=', res)
