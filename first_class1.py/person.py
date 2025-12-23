class UserAccount:
    def __init__(self, username:str, email:str):
        
        self.username = username
        self.email = email
        self.is_active = True
        self.login_count = 0
    def __str__(self):
            return f'Name {self.username}, email {self.email}'
        
    def login(self):
            self.login_count += 1
        
    def deactivate(self):
            self.is_active = False
            
    def activate(self):
            self.is_active = True
            
    def can_login(self):
           return self.is_active
        
    def get_info(self) :
            return f'User {self.username} ({self.email}) | logins : {self.login_count} | active : {self.is_active}'            