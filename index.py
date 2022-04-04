from dataset import users, countries
from pprint import pprint

# pprint(users)

users_wrong_password = []
dict_bad_password = {}
girls_drivers = []
best_occupation = {}

avg_flights = 0
count_flight_in_friends = 0
count_friends_with_cars = 0

max_salary = 0
max_friends_salary = 0

for user in users:
    # point 1
    try:
        password_int = int(user['password'])
        dict_bad_password = {'name' : user['name'], 'mail': user['mail']}
        users_wrong_password.append(dict_bad_password)

    except:
        pass

    sum_friends_salary = 0

    if user.get('friends'):
        for friend in user['friends']:
            # point 2
            if friend.get('cars'):
                if friend['sex'] == 'F': girls_drivers.append(friend['name'])
                if friend['cars']:
                    count_friends_with_cars += 1  # point 5
                        # point 5
                    if friend.get('flights'):
                        count_flight_in_friends += len(friend.get('flights', []))

            # point 3
            if friend['job']['salary'] > max_salary:
                best_occupation = friend['job'].copy()
                max_salary = friend['job']['salary']
                
            sum_friends_salary += friend['job']['salary']

    # point 4
    if max_friends_salary < sum_friends_salary:
        vip_user = user['name']
        max_friends_salary = sum_friends_salary

    
# point 6
len_users_before_detele = len(users)

i = 0
while i < len(users):
    need_remove = False
    # if user.get('friends'):
       # for friend in user['friends']:
    friends = users[i].get('friends', [])
    for friend in friends:   
        if friend.get('flights'):
            for flight in friend['flights']:
                if flight['country'] in countries:
                    need_remove = True
                    break
            if need_remove:
                    break
        
    if need_remove:
        del users[i]
    else:
        i += 1

avg_flights = round(count_flight_in_friends / count_friends_with_cars, 5)

print('users_wrong_password:', users_wrong_password)
print('Girls drivers:', girls_drivers)
print('Best occupation:', best_occupation)
print('Vip user:', vip_user)
print('avg_flights:', avg_flights)

print('Количество записей в users до удаления:', len_users_before_detele)
print('Количество записей в users после удаления:', len(users))