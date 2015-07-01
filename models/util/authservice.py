import gluon.http as http
import gluon.html as html
from gluon import current
from applications.todo.models.dao.userdao import UserDao

def checkIfAuthorized():
    if (current.request.cookies.has_key('userid')):
        userId = current.request.cookies['userid'].value
        userName = current.request.cookies['username'].value
        current.userName = userName
        current.userId = userId
        return userId
    else:
        http.redirect(html.URL('auth', 'login'))

def tryToLogin(email, password):
    user = UserDao.authorizeByEmailOrLogin(email, password)
    if (hasattr(user, 'id')):
        current.response.cookies['userid'] = user.id
        current.response.cookies['userid']['path'] = '/'
        current.response.cookies['userid']['expires'] = 3600
        current.response.cookies['username'] = user.name
        current.response.cookies['username']['path'] = '/'
        current.response.cookies['username']['expires'] = 3600
        return True
    else:
        return False

def logout():
    current.response.cookies['userid'] = ""
    current.response.cookies['userid']['path'] = "/"
    current.response.cookies['userid']['expires'] = -10
    current.response.cookies['username'] = ""
    current.response.cookies['username']['path'] = "/"
    current.response.cookies['username']['expires'] = -10
