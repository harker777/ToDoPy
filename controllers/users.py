from applications.todo.models.dao.userdao import UserDao

def index():
    rows = UserDao.getAllUsers();
    return dict(users = rows)
