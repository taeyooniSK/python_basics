members = ['heyo', 'gayoung', 'taeyoon']
# for member in members:
#     print(member)

# if you want to print elements of list in a particular range
# for member in members[1:3]:
#     print(member)  # 'heyo', 'gayoung'


for member in members:
    if member == 'gayoung':
        print(f'{member} - vegetarian')
        break  # after printing the above, for loop stops
    else:
        print(member)
