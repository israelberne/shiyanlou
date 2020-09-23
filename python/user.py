from werkzeug import generate_password_hash, check_password_hash


class User:
    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password_hash = self.save_password(password)

    def save_password(self,password):
        return generate_password_hash(password)

    def check_email(self,email):
        return self.email == email

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

def main():
    userList = []
    print('Welcome')
    while 1:
        choose = int(input('''
        1.register
        2.login
        3.exit
        '''))

        if choose == 1:
            print('Please input: ')
            name = input('name: ')
            email = input('email: ')
            password = input('password: ')
            newUser = User(name,email,password)
            userList.append(newUser)

        if choose == 2:
            print('Please input: ')
            email = input('email: ')
            password = input('password: ')
            inList = False
            for user in userList:
                if user.check_email(email):
                    inList = True
                    if user.check_password(password):
                        print('login success')
                    else:
                        print('password error')
            if inList = False:
                print('Please input the right email')

        if choose == 3:
            break

if __init__ == '__main__':
    main()
