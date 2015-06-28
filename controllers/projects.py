from applications.todo.models.dao.projectdao import ProjectDao

def index():
    rows = ProjectDao.getAllProjects();#db(db.project.id > 0).select(db.project.ALL)
    return dict(projects = rows)
