users_list = {"users": [{"name": "mouse"}, {"name": "cat"}]}

value_to_look = 'mouse'


for i in users_list["users"]:
    if i["name"] == value_to_look:
        print(i)
