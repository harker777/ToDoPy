from applications.todo.models.dao.userdao import UserDao
import re

def login():
    method = request.env.request_method
    if (method == 'GET'):
        return dict();
    if (method == 'POST'):
        email = request.post_vars.email
        password = request.post_vars.password
        result = authservice.tryToLogin(email, password)
        return dict(success = result);

def register():
    method = request.env.request_method
    if (method == 'GET'):
        return dict();
    if (method == 'POST'):
        success = True
        errorFields = []

        name = request.post_vars.name
        login = request.post_vars.login
        password = request.post_vars.password
        email = request.post_vars.email

        if (name == ""):
            success = False
            errorFields.append("name")
        if ((login == "") | (UserDao.userWithLoginExists(login))):
            success = False
            errorFields.append("login")
        if ((not re.match("[^@]+@[^@]+\.[^@]+", email)) | (UserDao.userWithEmailExists(email))):
            success = False
            errorFields.append("email")
        if (password == ""):
            success = False
            errorFields.append("password")

        if (success):
            db.user.insert(name = name, login = login, password = password, mail = email)

        return dict(success = success, errorFields = errorFields)

def logout():
    authservice.logout()
    redirect(URL('auth', 'login'))