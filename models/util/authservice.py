import gluon.http as http
import gluon.html as html
from gluon import current
from applications.todo.models.dao.userdao import UserDao

def checkIfAuthorized():
    if (current.request.cookies.has_key('userid')):
        return current.request.cookies['userid'].value
    else:
        http.redirect(html.URL('auth', 'login'))

def tryToLogin(email, password):
    userId = UserDao.authorizeByEmail(email, password)
    if (userId > 0):
        current.response.cookies['userid'] = userId
        current.response.cookies['userid']['path'] = '/'
        http.redirect(html.URL('projects', ' '))
    else:
        http.redirect(html.URL('auth', 'login'))