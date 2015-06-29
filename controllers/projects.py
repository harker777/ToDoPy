from applications.todo.models.dao.userdao import UserDao
from gluon import current
import applications.todo.models.util.auth as auth


def index():
    userid = auth.checkIfAuthorized()
    rows = UserDao.getUsersProjects(userid)
    return dict(projects = rows)