from applications.todo.models.dao.userdao import UserDao
from gluon import current

def index():
    rows = UserDao.getUsersProjects(1);
    return dict(projects = rows)