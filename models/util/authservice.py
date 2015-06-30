import gluon.http as http
import gluon.html as html
from gluon import current
from applications.todo.models.dao.userdao import UserDao

def checkIfAuthorized():
    if (current.request.cookies.has_key('userid')):
        userId = current.request.cookies['userid'].value
        userName = current.request.cookies['username'].value
        current.userName = userName
        current.userId = 1
        return userId
    else:
        http.redirect(html.URL('auth', 'login'))

def tryToLogin(email, password):
    user = UserDao.authorizeByEmail(email, password)
    if (user.id > 0):
        current.response.cookies['userid'] = user.id
        current.response.cookies['userid']['path'] = '/'
        current.response.cookies['username'] = user.name
        current.response.cookies['username']['path'] = '/'
        http.redirect(html.URL('projects', ' '))
    else:
        http.redirect(html.URL('auth', 'login'))

def logout():
    current.response.cookies['userid'] = ""
    current.response.cookies['userid']['expires'] = -10
    current.response.cookies['username'] = ""
    current.response.cookies['username']['expires'] = -10
