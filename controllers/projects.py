from applications.todo.models.dao.userdao import UserDao
from gluon import current

def index():
    rows = UserDao.getProjectsForUser(current.userId)
    return dict(projects = rows)