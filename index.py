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

for user in users:
    # point 1
    try:
        password_int = int(user['password'])
        dict_bad_password = {'name' : user['name'], 'password': user['password']}
        users_wrong_password.append(dict_bad_password)

    except:
        pass
    
    max_salary = 0

    sum_friends_salary = 0
    max_friends_salary = 0

    if user.get('friends'):
        for friend in user['friends']:
            # point 2
            if friend.get('cars'):
                if friend['sex'] == 'F': girls_drivers.append(friend['name'])
                count_friends_with_cars += 1  # point 5

            # point 3
            if friend['job']['salary'] > max_salary:
                best_occupation = {'occupation' : friend['job']['occupation'], 'salary': friend['job']['salary']}
                max_salary = friend['job']['salary']

            sum_friends_salary += friend['job']['salary']

    # point 4
    if max_friends_salary < sum_friends_salary:
        vip_user = user['name']
        max_friends_salary = sum_friends_salary

    # point 5
    if friend.get('flights'):
        for flight in friend['flights']:
            count_flight_in_friends += 1
    
    # point 6
list_users_for_delete = []
for user in users:
    for country in countries:
        if friend.get('flights'):
            for flight in friend['flights']:
                if country == flight['country']:
                    if user['name'] not in list_users_for_delete:
                        list_users_for_delete.append(user['name'])

pprint(len(users))

count_of_deletes = 0
for user in users:
    for user_for_delete in list_users_for_delete:
        if user['name'] == user_for_delete:
            user.clear()
            count_of_deletes += 1
            break
    

avg_flights = round(count_flight_in_friends / count_friends_with_cars, 5)

print('Bad passwords:', users_wrong_password)
print('Girls drivers:', girls_drivers)
print('Best occupation:', best_occupation)
print('Vip user:', vip_user)
print('avg_flights:', avg_flights)

print('len list_users_for_delete:', len(list_users_for_delete))
print('count_of_deletes:', count_of_deletes)

pprint(len(users))