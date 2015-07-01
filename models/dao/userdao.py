from gluon import current

class UserDao:
    @staticmethod
    def getAllUsers():
        db = current.db
        return db().select(db.user.ALL)

    @staticmethod
    def getProjectsForUser(userId):
        db = current.db
        return db(db.project.user_id == userId).select()

    @staticmethod
    def authorizeByEmailOrLogin(email, password):
        db = current.db
        query = ((db.user.mail == email) & (db.user.password == password)) | ((db.user.login == email) & (db.user.password == password))
        rows = db(query).select()
        if (len(rows.as_list()) > 0):
            return rows[0]

    @staticmethod
    def userWithEmailExists(email):
        db = current.db
        query = (db.user.mail == email)
        rows = db(query).select()
        if (len(rows.as_list()) > 0):
            return True
        else:
            return False

    @staticmethod
    def userWithLoginExists(login):
        db = current.db
        query = (db.user.login == login)
        rows = db(query).select()
        if (len(rows.as_list()) > 0):
            return True
        else:
            return False