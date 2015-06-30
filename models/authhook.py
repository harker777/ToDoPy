from gluon import current
import applications.todo.models.util.authservice as authservice

isLoginPage = (current.request.controller == 'auth') & (current.request.function == 'login')

if (not(isLoginPage)):
	current.userId = authservice.checkIfAuthorized()