import gluon.http as http
import gluon.html as html
from gluon import current

def checkIfAuthorized():
    if (current.request.cookies.has_key('userid')):
        return current.request.cookies['userid'].value
    else:
        http.redirect(html.URL('auth', 'login'))

def tryToLogin(email, password):
    db = current.db
    query = (db.user.mail == email) & (db.user.password == password)
    rows = db(query).select()
    if (len(rows.as_list()) > 0):
        current.response.cookies['userid'] = rows[0].id
        current.response.cookies['userid']['path'] = '/'
        http.redirect(html.URL('projects', ' '))
    else:
        http.redirect(html.URL('auth', 'login'))
