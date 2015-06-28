from applications.todo.models.dao.taskdao import TaskDao

def index():
    rows = TaskDao.getAllTasks();#db(db.task.id > 0).select(db.task.ALL)
    return dict(tasks = rows)

