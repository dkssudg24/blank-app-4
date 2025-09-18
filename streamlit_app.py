import streamlit as st

st.title("간단한 계산기")
num1 = st.number_input("첫 번째 숫자를 입력하세요", format="%.2f")
num2 = st.number_input("두 번째 숫자를 입력하세요", format="%.2f")
operator = st.selectbox("원하는 연산을 선택하세요", ('+', '-', '*', '/'))

if st.button("계산하기"):
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
    st.write("결과:", result)

