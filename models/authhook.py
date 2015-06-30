from gluon import current
import applications.todo.models.util.authservice as authservice

isAuthPage = (current.request.controller == 'auth')

if (not(isAuthPage)):
	authservice.checkIfAuthorized()