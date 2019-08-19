# for n in range(5):
#     print(n)


# for n in range(3, 10):  # you can set a starting point of range( not inclusive of 10)
#     print(n)


# for n in range(0, 20, 4):  # add 4 from 0 to 20
#     print(n)

# result:
# 0
# 4
# 8
# 12
# 16


burgers = ['beef', 'chicken', 'veg', 'supreme', 'double']

# for n in range(len(burgers)):
#     print(n, burgers[n])

# len(burgers)-1의 값은 4, -1은 starting point, 마지막 -1은 4에서 1씩 빼는 값 (즉, loop을 backwards)
for n in range(len(burgers) - 1, -1, -1):
    print(n, burgers[n])


# result:
# 4 double
# 3 supreme
# 2 veg
# 1 chicken
# 0 beef
