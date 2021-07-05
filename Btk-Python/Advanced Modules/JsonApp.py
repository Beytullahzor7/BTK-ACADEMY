import json
import os

class User:
    def __init__(self, username, password, email):

        self.username = username
        self.password = password
        self.email = email
        
class UserRepository:

    def __init__(self):
        self.users = []
        self.isLoggedIn = False #kullanıcı varsayılan olarak login olmamıs diyecegiz
        self.currentUser = {}

        #load users from .json file
        self.loadUsers()

    def loadUsers(self):
        if os.path.exists('users.json'):
            with open('users.json', 'r', encoding='utf-8') as file:
                users = json.load(file)
                for user in users:
                    user = json.loads(user)
                    newUser = User(username = user['username'], password = user['password'], email = user['email'])
                    self.users.append(newUser)
        
            print(self.users)
        

    def register(self, user: User):
        self.users.append(user)
        self.savetofile()
        print("Kullanıcı Olusturuldu")
        
    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user

                print('Login Yapıldı.')
                break
        
    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print('Cıkıs Yapıldı')

    def identity(self):
        if self.isLoggedIn:
            print(f'Username: {self.currentUser.username}')
        else:
            print('Giriş Yapılmadı')


    def savetofile(self):
        list = []

        for user in self.users:
            list.append(json.dumps(user.__dict__)) #user clasını sözlük yapısına cevirin .json ile kayıt edebiliriz

        with open('users.json','w') as file:
            json.dump(list, file)
        

repository = UserRepository()


while True:
    print('Menü' .center(50, '*'))
    secim = input('1- Register\n2- Login\n3- Logout\n4- Identity\n5- Exit\nSeçiminiz: ')

    if secim == '1':
            username = input('Username : ')
            password = input('Password : ')
            email = input('Email : ')
            
            user = User(username=username, password=password, email=email)
            repository.register(user)

            print(repository.users)
    elif secim == '2':

        if repository.isLoggedIn:
            print('Zaten Login Oldunuz')

        else:

            username = input('Username : ')
            password = input('Password : ')
            
            repository.login(username, password)
        
    elif secim == '3':
        repository.logout()
        pass
    elif secim == '4':
        repository.identity()
        
    elif secim == '5':
        print('Cıkıs Yapılıyor')
        break
    else:
        print('Yanlıs')
    

        

       