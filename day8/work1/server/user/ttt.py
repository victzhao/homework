import  json
with open('user_info.db','r') as rf:
    for i in rf:
        user_info = json.loads(i.strip())
        print(type(user_info))

