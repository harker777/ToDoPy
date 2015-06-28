from applications.todo.models.dao.projectdao import ProjectDao
from applications.todo.models.dao.userdao import UserDao

def index():
    #rows = ProjectDao.getAllProjects();#db(db.project.id > 0).select(db.project.ALL)
    rows = UserDao.getUsersProjects(1);
    return dict(projects = rows)