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

def create():
	name = request.post_vars.name
	db.project.insert(name = name, user_id = current.userId)
	redirect(URL('projects', ' '))