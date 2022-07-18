from django.utils.translation import gettext as _

# Context elements
SIGNUP_TITLE = _('New user sign up')
UPDATE_USER_TITLE = _('Update user')
DELETE_USER_TITLE = _('Delete user')

CREATE_STATUS_TITLE = _('Create status')
UPDATE_STATUS_TITLE = _('Update status')
DELETE_STATUS_TITLE = _('Delete status')

CREATE_TASK_TITLE = _('Create task')
UPDATE_TASK_TITLE = _('Update task')
DELETE_TASK_TITLE = _('Delete task')

CREATE_LABEL_TITLE = _('Create label')
UPDATE_LABEL_TITLE = _('Update label')
DELETE_LABEL_TITLE = _('Delete label')

SIGNUP_BTN = _('Sign up')
UPDATE_BTN = _('Update')
DELETE_BTN = _('Yes, delete')
CREATE_BTN = _('Create')

FILTER_BTN = _('Show')
FILTER_MY_TASKS = _('Only my tasks')

STATUS_LIST_TITLE = _('Statuses')
STATUS_LIST_NEW = _('New status')

LABEL_LIST_TITLE = _('Labels')
LABEL_LIST_NEW = _('New label')

# Messages
LOGIN_SUCSESS = _("You are logged in.")
LOGOUT_SUCSESS = _("You are logged out.")
SIGNUP_SUCSESS = _("The user is created.")
UPDATE_USER_SUCSESS = _("The user is updated.")
UPDATE_USER_FAIL = _("You don't have permissions to edit other users.")
DELETE_USER_SUCSESS = _("The user is deleted.")
DELETE_USER_FAIL = _("You don't have permissions to edit other users.")
USER_IN_USE = _('Can\'t delete the user because it\'s in use')

NOT_LOGGED_IN = _('You are not authorized! Please log in.')

CREATE_STATUS_SUCSESS = _('The status is created.')
UPDATE_STATUS_SUCSESS = _('The status is updated.')
DELETE_STATUS_SUCSESS = _('The status is deleted.')
STATUS_IN_USE = _('Can\'t delete the status because it\'s in use')

CREATE_TASK_SUCSESS = _('The task is created.')
UPDATE_TASK_SUCSESS = _('The task is updated.')
DELETE_TASK_SUCSESS = _('The task is deleted.')
DELETE_TASK_FAIL = _('The task can only be deleted by it\'s author.')

CREATE_LABEL_SUCSESS = _('The label is created.')
UPDATE_LABEL_SUCSESS = _('The label is updated.')
DELETE_LABEL_SUCSESS = _('The label is deleted.')
LABEL_IN_USE = _('Can\'t delete the label because it\'s in use')
