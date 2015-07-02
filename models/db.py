from gluon import current

db = DAL('mysql://root:root@localhost:3306/todo', migrate_enabled = False)
current.db = db;

db.define_table('user',
                Field('id', 'integer'),
                Field('login','string'),
		Field('password', 'string'),
		Field('name', 'string'),
		Field('mail', 'string'))

db.define_table('project',
                Field('id', 'integer'),
                Field('name','string'),
		Field('color', 'string'),
		Field('parent_id', 'integer'),
		Field('user_id', 'integer'))

db.define_table('tag',
                Field('id', 'integer'),
                Field('name','string'),
		Field('user_id', 'integer'))

db.define_table('task',
                Field('id', 'integer'),
                Field('name','string'),
		Field('project_id', 'integer'),
		Field('time', 'date'),
		Field('deadline', 'date'),
		Field('priority', 'integer'),
		Field('status', 'integer'),
		Field('parent', 'integer'))
