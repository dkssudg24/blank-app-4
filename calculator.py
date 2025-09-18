# calculator.py

# 두 숫자를 입력받습니다.
num1 = input("첫 번째 숫자를 입력하세요: ")
num2 = input("두 번째 숫자를 입력하세요: ")

# 입력받은 값은 문자열이므로, 숫자로 변환합니다.
num1 = float(num1)
num2 = float(num2)

# 연산자를 입력받습니다.
operator = input("원하는 연산을 입력하세요 (+, -, *, /): ")

# 연산에 따라 계산을 수행합니다.
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 == 0:
        result = '0으로 나눌 수 없습니다.'
    else:
        result = num1 / num2
else:
    result = '지원하지 않는 연산자입니다.'

# 결과를 출력합니다.
print("결과:", result)