# list 에서 마이너스 인덱스 숫자로도 각 요소에 접근할 수 있음
list = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9]
totalList = list + list2
print(list[0])
print(list[-1])
print(list[3:-1])
print(list + list2)  # can concatenate two lists with '+' operator

totalList.append(10)  # add an element to the end of the list
totalList.append(10)
print(totalList)
# totalList.pop()
# print(totalList)  # delete an element at the end of the list

totalList.remove(10)  # 만약 중복되는 숫자가 해당 리스트에 있으면 중복되는 숫자의 가장 첫번재 숫자를 제거함
print(totalList)
del(totalList[9])  # 내가 원하는 인덱스 위치에 있는 숫자를 지우고 싶을때 del() 함수를 써도 됨
print(totalList)
