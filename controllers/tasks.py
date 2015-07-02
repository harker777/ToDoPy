from applications.todo.models.dao.taskdao import TaskDao
from datetime import datetime

def index():
    rows = TaskDao.getAllTasks();
    return dict(tasks = rows)

def details():
	taskId = request.args[0]
	task = TaskDao.getTaskById(taskId)
	if not task.deadline is None:
		deadline = datetime.strftime(task.deadline, "%m/%d/%Y %H:%M")
		return dict(task = task, deadline = deadline)
	else:
		return dict(task = task)

def save():
	projectId = request.post_vars.projectid
	taskId = request.post_vars.taskid
	name = request.post_vars.name
	priority = request.post_vars.priority
	deadline = request.post_vars.deadline

	task = TaskDao.getTaskById(taskId)
	if not name == "":
		task.update_record(name = name)
	if not deadline == "":
		task.update_record(deadline = datetime.strptime(deadline, "%m/%d/%Y %H:%M"))
	if not priority == "":
		task.update_record(priority = priority)

	redirect(URL('projects', 'details', args = [projectId]))