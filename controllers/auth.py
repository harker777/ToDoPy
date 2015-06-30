def login():
    method = request.env.request_method
    if (method == 'GET'):
        return dict();
    if (method == 'POST'):
        email = request.post_vars.email
        password = request.post_vars.password
        authservice.tryToLogin(email, password)
        return dict();

def register():
    method = request.env.request_method
    if (method == 'GET'):
        return dict();
    if (method == 'POST'):
        name = request.post_vars.name
        login = request.post_vars.login
        password = request.post_vars.password
        email = request.post_vars.email
        id = db.user.insert(name = name, login = login, password = password, mail = email)
        redirect(URL('auth', 'login'))

def logout():
    authservice.logout()
    redirect(URL('auth', 'login'))