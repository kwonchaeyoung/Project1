'''
교재 : 깃특강2-깃 버전 관리 기본(Ver1.3.1)p.pdf p.36

'''

# 함수 선언부
def add_func(n1, n2):
    return n1 + n2

# 전역 변수부
num1, num2, res = 100, 200, 0

# 메인 코드부
res = add_func(num1, num2)
print(num1, '+', num2, '=', res)