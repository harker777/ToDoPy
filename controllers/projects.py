from applications.todo.models.dao.userdao import UserDao
from applications.todo.models.dao.taskdao import TaskDao
from applications.todo.models.dao.projectdao import ProjectDao
from gluon import current

def index():
    rows = UserDao.getProjectsForUser(current.userId)
    return dict(projects = rows)

def details():
	projectId = request.args[0]
	tasks = TaskDao.getTasksForProject(projectId)
	project = ProjectDao.getProjectById(projectId)
	return dict(tasks = tasks, project = project)

def create():
	name = request.post_vars.name
	db.project.insert(name = name, user_id = current.userId, color = "ffffff")
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

def setcolor():
	projectId = request.post_vars.projectId
	color = request.post_vars.color
	project = ProjectDao.getProjectById(projectId)
	project.update_record(color = color)
	return dict()	