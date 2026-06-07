# Password Generator....

import secrets
import string


print('What kind of password do you want? \n(weak/strong/too strong):')


max_attempts = 3
def get_password():


    for _ in range(max_attempts):
        password = input("Enter your password strength : ").lower()
        if password == 'weak':

            print("Generating weak password...")
            choice = string.ascii_lowercase
            length = 6
            return choice,length
            
            

        elif password == 'strong':
            print("Generating strong password...")
            choice = string.ascii_letters + string.digits
            length = 9
            return choice,length
            

        elif password == 'too strong':
            print("Generating too strong password...")
            choice = string.ascii_letters + string.digits + string.punctuation
            length = 12
            return choice,length
            

        else:
            print("Invalid choice!!..please enter a valid password... ")
        
    return None,None


choice,length = get_password()
if choice is None:
    print("Too many Invalid attempts...")

else:
    create_password = [secrets.choice(choice) for _ in range(length)]
    made_password = ''.join(create_password)
    print('Your password is :',made_password)