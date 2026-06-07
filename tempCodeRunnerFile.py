
create_password = ''.join(random.choices(choice,k = length))
random.shuffle(create_password)
print('Your password is :',create_password)