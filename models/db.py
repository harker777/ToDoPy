db = DAL('mysql://root:1111@localhost:3306/todo', migrate_enabled = False)

db.define_table('user',
                Field('id', 'integer'),
                Field('login','string'),
		Field('password', 'string'),
		Field('name', 'string'),
		Field('mail', 'string'))

db.define_table('project',
                Field('id', 'integer'),
                Field('name','string'),
		Field('color', 'integer'),
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
