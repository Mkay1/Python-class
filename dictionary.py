my_dict = {}
my_dict = {'name': 'Jack', 'age': 26}
print(my_dict['name'])
print(my_dict.get('age'))
my_dict['age'] = 27
print(my_dict)
my_dict['address'] = 'Downtown'
print(my_dict)
my_dict.pop('age')
print(my_dict)
print("Address :", my_dict.get('address'))
my_dict.clear()
print(my_dict)

user = input("Enter a key")
if user in my_dict:
    print(my_dict[user])

