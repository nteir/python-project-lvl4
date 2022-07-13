from django.utils.translation import gettext as _

# Context elements
SIGNUP_TITLE = _('New user sign up')
SIGNUP_BTN = _('Sign up')
UPDATE_TITLE = _('Update user')
UPDATE_BTN = _('Update')
DELETE_TITLE = _('Delete user')
DELETE_BTN = _('Yes, delete')

# Messages
USER_IN_USE = _('Can\'t delete the user because it\'s in use')
LOGIN_SUCSESS = _("You are logged in.")
LOGOUT_SUCSESS = _("You are logged out.")
SIGNUP_SUCSESS = _("The user is created.")
UPDATE_USER_SUCSESS = _("The user is updated.")
UPDATE_USER_FAIL = _("You don't have permissions to edit other users.")
DELETE_USER_SUCSESS = _("The user is deleted.")
DELETE_USER_FAIL = _("You don't have permissions to edit other users.")
