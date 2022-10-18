from general import con

class User:
    def __init__(self, username) -> None:
        if type(username) != str or not len(username.strip()):
            raise Exception()
        self.username = username; self.__score = 0
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, x):
        self.__score = x if x >= 0 else 0
    @property
    def status(self):
        try:
            return bool(con.execute('SELECT auth FROM users WHERE username == ?', [self.username]).fetchone()[0])
        except:
            return None
    def check(self, password):
        return con.execute('SELECT (password == ?) FROM users WHERE username == ?', [password, self.username]).fetchone()[0]
    def create(self, password):
        with con: con.execute('INSERT INTO users(username, password, auth) VALUES(?, ?, TRUE)', [self.username, password])
    def singIn(self):
        with con: con.execute('UPDATE users SET auth = TRUE WHERE username == ?', [self.username])
    def singOut(self):
        with con: con.execute('UPDATE users SET auth = FALSE WHERE username == ?', [self.username])