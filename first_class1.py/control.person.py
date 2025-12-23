from person import UserAccount
user = UserAccount("Sergiu", "sergiu@mail.com")

print(user)

user.login()
user.login()

print(user.get_info())

user.deactivate()
print(user.can_login())

user.activate()
user.login()

print(user.get_info())