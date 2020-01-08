from flask import redirect, request, url_for
from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_security import current_user


class AdminMixin:
    def is_accessible(self):
        return current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next=request.url))


class BaseModelView(ModelView):
    def on_model_change(self, form, model, is_created):
        model.generate_slug()
        return super(BaseModelView, self).on_model_change(form, model, is_created)


class UserAdminView(AdminMixin, ModelView):
    can_view_details = ['user_name']
    column_list = ['user_name', 'email', 'phone', 'created_date']


class RoleAdminView(AdminMixin, ModelView):
    can_view_details = ['name']


class PostAdminView(AdminMixin, BaseModelView):
    form_columns = ['title', 'body', 'tags']
    can_view_details = ['title']
    column_editable_list = ['title']
    column_list = ['title', 'slug', 'created_date']


class TagAdminView(AdminMixin, BaseModelView):
    form_columns = ['name', 'posts']


class HomeAdminView(AdminMixin, AdminIndexView):
    pass
