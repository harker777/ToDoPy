from applications.todo.models.dao.userdao import UserDao
from gluon import current
import applications.todo.models.util.auth as auth

def index():
    rows = UserDao.getProjectsForUser(current.userId)
    return dict(projects = rows)