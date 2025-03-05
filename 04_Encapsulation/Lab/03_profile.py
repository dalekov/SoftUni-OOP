class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username


    @username.setter
    def username(self, username: str):
        if not 5 <= len(username) <= 15:
            raise ValueError("The username must be between 5 and 15 characters.")

        self.__username = username

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password: str):
        if not (len(password) >= 8 and sum(1 for ch in password if ch.isupper()) >= 1 and sum(1 for ch in password if ch.isnumeric()) >= 1):
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

        self.__password = password

    def __str__(self):
        return f'You have a profile with username: "{self.__username}" and password: {"*" * len(self.__password)}'