
# # Bascially, dictionary is quite similar to object in JS

# # The first way to make a dictionary
# member_favoriteColors = {
#     'taeyoon': 'blue',
#     'cheolsu': 'black'
# }


# print(member_favoriteColors)


# print(member_favoriteColors['taeyoon'])

# # you can check if there is a property in dictionary using 'in' keyword

# print('taeyoon' in member_favoriteColors)
# print('cheolsu' in member_favoriteColors)

# # Get properties(=keys) of a dictionary
# print(member_favoriteColors.keys())
# # result: dict_keys(['taeyoon', 'cheolsu'])

# # Turn a dictinary to a list(= typecastuing)  : list()
# print(list(member_favoriteColors.keys()))
# # result:['taeyoon', 'cheolsu']

# # Get values of a dictionary
# print(member_favoriteColors.values())
# # result: dict_values(['blue', 'black'])

# vals = list(member_favoriteColors.values())
# print(vals)
# # result: ['blue', 'black']

# # count method: tells you how many values of the argument for the count method in the list
# print(vals.count('black'))

# # To change the value of the dictionary
# member_favoriteColors['cheolsu'] = 'green'
# print(member_favoriteColors['cheolsu'])

# print('updated dictionary:', member_favoriteColors)

# # Another way to make a dicitonary
# person = dict(name='jawoorim', age=39, height=165)
# print(person)


def people_intro(dict):
    for key, val in dict.items():
        print(f'I am {key} and I like {val}')


print(people_intro(member_favoriteColors))
