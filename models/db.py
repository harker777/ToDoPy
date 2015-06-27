db = DAL('mysql://root:root@localhost:3306/todo', migrate_enabled = False)

db.define_table('user',
                Field('id', 'integer'),
                Field('login','string'))
