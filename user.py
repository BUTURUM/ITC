from general import con

class User:
    def __init__(self, username) -> None:
        if type(username) != str or not len(username.strip()):
            raise Exception()
        self.username = username
    @property
    def registered(self):
        try:
            return con.execute('SELECT auth FROM users WHERE username == ?', [self.username]).fetchone()[0]
        except:
            return False
    @property
    def exists(self):
        return con.execute('SELECT COUNT(*) FROM users WHERE username == ?', [self.username]).fetchone()[0]
    def check(self, password):
        return con.execute('SELECT (password == ?) FROM users WHERE username == ?', [password, self.username]).fetchone()[0]
    def create(self, password):
        with con: con.execute('INSERT INTO users(username, password, auth) VALUES(?, ?, TRUE)', [self.username, password])
    def singIn(self):
        with con: con.execute('UPDATE users SET auth = TRUE WHERE username == ?', [self.username])
    def singOut(self):
        with con: con.execute('UPDATE users SET auth = FALSE WHERE username == ?', [self.username])
    # def singIn(self, password):
    #     if con.execute('SELECT password FROM users WHERE username == ?', [self.username]).fetchone()[0] != password:
    #         return False
    #     with con:
    #         con.execute('UPDATE users SET auth = TRUE WHERE username == ?', [self.username])
    #     return True
    # def singOut(self):
    #     with con: con.execute('UPDATE users SET auth = FALSE WHERE username == ?', [self.username])
