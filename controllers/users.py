from applications.todo.models.dao.userdao import UserDao

def index():
    rows = UserDao.getAllUsers();#db(db.user.id > 0).select(db.user.ALL);
    return dict(users = rows)
