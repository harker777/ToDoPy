from applications.todo.models.dao.userdao import UserDao
from applications.todo.models.dao.taskdao import TaskDao
from gluon import current

def index():
    rows = UserDao.getProjectsForUser(current.userId)
    return dict(projects = rows)

def details():
	projectId = request.args[0]
	tasks = TaskDao.getTasksForProject(projectId)
	return dict(tasks = tasks)