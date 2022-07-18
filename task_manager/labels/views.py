from .models import Label
from django.urls import reverse_lazy
from .forms import LabelCreateForm
import task_manager.text_constants as txt

# Re-using the List, Create, Update and Delete
# views from statuses, passing new attributes in as_view()
# Common attributes for Create and Update Views
common_attr = {
    'model': Label,
    'form_class': LabelCreateForm,
    'template_name': "form.html",
    'success_url': reverse_lazy('labels:obj_list'),
    'redirect_url': reverse_lazy('login'),
    'error_message': txt.NOT_LOGGED_IN,
}

list_view_attr = {
    'model': Label,
    'app_name': 'labels',
    'title': txt.LABEL_LIST_TITLE,
    'new_obj_text': txt.LABEL_LIST_NEW,
}

create_view_attr = {
    'success_message': txt.CREATE_LABEL_SUCSESS,
    'title_text': txt.CREATE_LABEL_TITLE,
    'btn_text': txt.CREATE_BTN,
}
create_view_attr.update(common_attr)

update_view_attr = {
    'success_message': txt.UPDATE_LABEL_SUCSESS,
    'title_text': txt.UPDATE_LABEL_TITLE,
    'btn_text': txt.UPDATE_BTN,
}
update_view_attr.update(common_attr)

delete_view_attr = {
    'model': Label,
    'success_url': reverse_lazy('labels:obj_list'),
    'success_message': txt.DELETE_LABEL_SUCSESS,
    'title_text': txt.DELETE_LABEL_TITLE,
    'in_use_text': txt.LABEL_IN_USE,
}


# Create your views here.
