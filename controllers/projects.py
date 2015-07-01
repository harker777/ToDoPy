from applications.todo.models.dao.userdao import UserDao
from applications.todo.models.dao.taskdao import TaskDao
from gluon import current

def index():
    rows = UserDao.getProjectsForUser(current.userId)
    return dict(projects = rows)

def details():
	projectId = request.args[0]
	tasks = TaskDao.getTasksForProject(projectId)
	return dict(tasks = tasks, projectId = projectId)

def create():
	name = request.post_vars.name
	db.project.insert(name = name, user_id = current.userId)
	redirect(URL('projects', ' '))

def addtask():
	projectId = request.post_vars.projectId
	name = request.post_vars.name
	db.task.insert(name = name, project_id = projectId)
	redirect(URL('projects', 'details', args = [projectId]))

def delete():
	projectId = request.post_vars.projectId
	projects = db(db.project.id == projectId)
	projects.delete()
	redirect(URL('projects', ' '))

def deletetask():
	projectId = request.post_vars.projectId
	taskId = request.post_vars.taskId
	tasks = db(db.task.id == taskId)
	tasks.delete()
	redirect(URL('projects', 'details', args = [projectId]))