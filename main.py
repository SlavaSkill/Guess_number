import random

number = random.randint(1, 100)
#print(number)

user_number = None
count = 0
levels = {1: 10, 2: 5, 3: 3}

level = int(input("Please, enter difficulty level: "))
max_count = levels[level]

user_count = int(input("Please, enter users amount: "))
users = []
for i in range(user_count):
    user_name = input(f'Please, enter user name {i}')
    users.append(user_name)
is_winner = False
winner_name = None
while not is_winner:
    count += 1
    if count > max_count:
        print("All users lost!")
        break
    print(f'Shoot number {count}')
    for user in users:
        print(f'{user} turn')
        user_number = int(input("Please, enter your number: "))
        if user_number == number:
            is_winner = True
            winner_name = user
            break
        elif number < user_number:
            print("Your number is bigger")
        else:
            print('Your number is lower')
else:
    print(f'{winner_name} You WON!')
