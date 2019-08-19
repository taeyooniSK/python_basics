num1 = 3.1425467389
num2 = 10.2903948

# Previous
# print('num1 is', num1, 'and num2 is', num2)

# Format Method
print('num1 is {0} and num 2 is {1}'.format(num1, num2))

# 위 num1과 num2의 출력될 소수 자리를 정해주고싶다면
# 0:.3의 뜻은 0번째 argument에서 숫자를 세자리까지 (3 digits) 출력

print('num1 is {0:.3} and num 2 is {1:.3}'.format(num1, num2))
# result: num1 is 3.14 and num 2 is 10.3

# ----------------------------------------------------------

# 만약 또 그뒤에 f를 붙인다면 소수 셋째짜리까지 출력
print('num1 is {0:.3f} and num 2 is {1:.3f}'.format(num1, num2))
# result: num1 is 3.143 and num 2 is 10.290

# ----------------------------------------------------------

# Using F-strings
# num1과 num2의 값에서 소수 넷째자리까지 출력
print(f'num1 is {num1:.4f} and num2 is {num2:.4f}')
