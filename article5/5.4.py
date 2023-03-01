users = ['admin', 'jim', 'tom', 'jeff', 'bob']

for user in users:
    if user == 'admin':
        print('Hello admin. would you like see a report?')
    else:
        print('Hello %s' % user)